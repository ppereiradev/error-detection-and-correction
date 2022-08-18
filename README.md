# Error Detection and Correction Algorithms in Python

In this repository, we have the implementation from scratch of some error detection and correction algorithms used in computer networks.

## Installation

This implementation has no dependecies, but it is better if you create a virtual environment to execute it.

Create a virtual environment.
```bash
python3 -m venv venv --prompt="error-detection"
```

After that, we will have a venv folder in the directory. Activate the virtual environment.
```bash
source venv/bin/activate
```

Now you have the virtual environment activated.

## Usage

Execute first the server, so the client will have who connect with. You have to pass the name of the algorithm as argument when running the server.py.
```bash
python server.py -a crc
```
or
```bash
python server.py --algorithm hamming
```

Now you can run the client. Remember you have to pass the same algorithm that you passed for the server.
```bash
python client.py -a crc
```
or
```bash
python client.py --algorithm hamming
```

The algorithm options are: parity, crc, hamming, reed-solomon. Suppose you want to run the Reed-Solomon algorithm, so you have to run the server and the client, respectively, as follows:

```bash
python server.py --algorithm reed-solomon
python client.py --algorithm reed-solomon
```

## File Description

```bash
├── README.md
├── algorithms # folder that contains the algorithm implementations
│   ├── crc.py # Cyclic Redundancy Check implementation
│   ├── hamming.py # Hamming Code implementation
│   ├── parity.py # Odd Parity Error Detection implementation
│   └── reed_solomon.py # Reed-Solomon Code implementation
├── client.py # Simulating the client side, where it sends a message to the server
└── server.py # Simulating the server side, where the message is processed and it verifies if the message contains any error
```