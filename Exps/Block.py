import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
        print(f"Block created: {self.__dict__}")

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True)
        computed_hash = hashlib.sha256(block_string.encode()).hexdigest()
        print(f"Calculating hash for block {self.index}: {computed_hash}")
        return computed_hash

class Blockchain:
    def __init__(self):
        print("Initializing blockchain...")
        self.chain = [self.create_genesis_block()]
        print("Genesis block created.")

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        print(f"Adding new block with data: {data}")
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)
        print(f"New block added: {new_block.__dict__}")

    def is_chain_valid(self):
        print("Validating blockchain...")
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {i} has been tampered!")
                return False
            if current_block.previous_hash != previous_block.hash:
                print(f"Block {i} has an invalid previous hash!")
                return False
        print("Blockchain is valid.")
        return True

# Usage
blockchain = Blockchain()
blockchain.add_block("First transaction data")
blockchain.add_block("Second transaction data")

for block in blockchain.chain:
    print(vars(block))

print("Blockchain valid:", blockchain.is_chain_valid())
