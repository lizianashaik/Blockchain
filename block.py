import hashlib
import time
import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, ["Genesis Block"], time.time(), "0")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self):
        if not self.pending_transactions:
            return None
        index = len(self.chain)
        previous_hash = self.get_latest_block().hash
        new_block = Block(index, self.pending_transactions, time.time(), previous_hash)
        new_block.hash = self.mine_block(new_block)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def mine_block(self, block):
        target = "0" * self.difficulty
        while block.hash[:self.difficulty] != target:
            block.nonce += 1
            block.hash = block.calculate_hash()
        return block.hash

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash() or \
               current_block.previous_hash != previous_block.hash or \
               block.hash[:self.difficulty] != "0" * self.difficulty:
                return False
        return True

    def to_dict(self):
        return [{"index": b.index, "timestamp": b.timestamp, "transactions": b.transactions,
                 "previous_hash": b.previous_hash, "hash": b.hash, "nonce": b.nonce}
                for b in self.chain]

# Initialize blockchain
blockchain = Blockchain()

# Web routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.json
    transaction = data.get('transaction')
    if transaction:
        blockchain.add_transaction(transaction)
        return jsonify({"message": "Transaction added"}), 200
    return jsonify({"error": "No transaction provided"}), 400

@app.route('/mine', methods=['POST'])
def mine():
    block = blockchain.mine_pending_transactions()
    if block:
        return jsonify({"message": f"Block {block.index} mined", "block": {
            "index": block.index, "hash": block.hash}}), 200
    return jsonify({"error": "No transactions to mine"}), 400

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain.to_dict()), 200

@app.route('/validate', methods=['GET'])
def validate():
    return jsonify({"valid": blockchain.is_chain_valid()}), 200

if __name__ == '__main__':
    app.run(debug=True)
