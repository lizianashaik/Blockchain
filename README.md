# Blockchain
# Real-Time Blockchain Simulation

## Overview
This project is a simple blockchain simulation implemented in Python with a real-time web interface using Flask. It demonstrates core blockchain concepts such as block creation, hashing, proof-of-work, and chain validation. Users can interactively add transactions, mine blocks, and view the blockchain through a web browser.

## Features
- **Block Structure**: Each block contains an index, timestamp, transactions, previous hash, current hash, and nonce.
- **Hashing**: Uses SHA-256 for block hashing.
- **Proof of Work**: Requires hashes to start with a set number of zeros (difficulty = 4).
- **Real-Time Interaction**: Web interface allows adding transactions and mining blocks with instant updates.
- **Chain Validation**: Checks the integrity of the blockchain.
- **Dynamic Display**: View the entire chain and validate it on demand.

## Prerequisites
- **Python 3.x**: Ensure Python is installed (download from [python.org](https://www.python.org/)).
- **Flask**: Python web framework for the real-time interface.
- **Internet Connection**: Required for loading jQuery via CDN in the web interface.

## Setup Instructions

### 1. Clone or Download
Clone this repository or download the files:
```bash
# Blockchain Simulation with Flask

## 1. Clone the Repository
```bash
git clone <repository-url>
cd blockchain_sim
```

## 2. Install Dependencies
Install Flask using pip:
```bash
pip install flask
```
Verify installation:
```bash
# Linux/Mac
pip list | grep Flask  
# Windows
pip list | findstr Flask  
```

## 3. Project Structure
Ensure your directory looks like this:
```
blockchain_sim/
├── blockchain.py       # Main Python script
└── templates/
    └── index.html      # Web interface template
```
- **blockchain.py**: Contains the blockchain logic and Flask server.
- **templates/index.html**: HTML template for the web UI.

## 4. Run the Application
Start the Flask server:
```bash
python blockchain.py
```
On some systems, use:
```bash
python3 blockchain.py
```
You’ll see output like:
```
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Open a browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## 5. Usage
### Add Transactions
- Enter a transaction (e.g., "Alice sends 10 BTC to Bob") in the input field.
- Click **Add** to queue it for mining.

### Mine Blocks
- Click **Mine** to create a new block with all pending transactions.
- Mining includes a proof-of-work process.

### View Blockchain
- Click **Refresh** to display the current blockchain state.

### Validate Chain
- Click **Validate** to check if the chain is intact (returns `true` or `false`).

## 6. Example Interaction
1. **Add**: "Alice sends 10 BTC to Bob"
2. **Add**: "Bob sends 5 BTC to Charlie"
3. **Mine**: Creates Block 1 with both transactions
4. **Refresh**: Shows Genesis Block (0) and Block 1
5. **Validate**: Confirms chain integrity

## 7. Troubleshooting
- **Flask Not Found**: Run `pip install flask` or check your Python environment.
- **TemplateNotFound**: Ensure `index.html` is in the `templates` folder.
- **Port in Use**: Change `app.run(port=5001)` in `blockchain.py` and use `http://127.0.0.1:5001/`.
- **Blank Page**: Check browser console (F12) for errors; ensure internet for jQuery.

## 8. Optional Enhancements
- **Public Hosting**: Modify `app.run(host='0.0.0.0')` to access over a network.
- **Live Updates**: Integrate Flask-SocketIO for automatic chain refreshes.
- **Persistence**: Add file storage to save the blockchain between runs.

## 9. Acknowledgments
Built with Python, Flask, and jQuery. Inspired by basic blockchain concepts for educational purposes.

---
