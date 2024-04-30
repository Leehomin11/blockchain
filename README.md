# Simple Blockchain Implementation in Python

This is a basic implementation of a blockchain in Python. It includes classes for creating blocks and a blockchain, as well as functions for generating hashes using SHA-256.

## Features

- **Block Generation**: Blocks are created with data, a hash, and a reference to the previous block's hash.
- **Blockchain Creation**: The blockchain is initialized with a genesis block.
- **Adding Blocks**: New blocks can be added to the blockchain, each referencing the hash of the previous block.
- **Hashing**: SHA-256 hashing is used to generate hashes for blocks.

## Usage

To use this implementation, simply include the `blockchain.py` file in your project and follow these steps:

1. **Initialize Blockchain**: Create an instance of `MyBlockchain` to initialize the blockchain with a genesis block.
2. **Add Blocks**: Use the `add_block` method to add new blocks to the blockchain.

```python
blch = MyBlockchain()
blch.add_block('Data for Block 1')
blch.add_block('Data for Block 2')
# Add more blocks as needed
```
## Access Blockchain

To access individual blocks and their properties, you can iterate over the `chain` attribute of the blockchain.

```python
for block in blch.chain:
    print(block.__dict__)
```

## Example

Here's an example of how blocks are structured:

```python
{
    'data': 'Data for Block 1',
    'hash': 'Hash of Block 1',
    'prev_hash': 'Hash of Previous Block'
}
```

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

-------------------
You can paste this content directly into your README.md file on GitHub. Let me know if you need any further assistance!
