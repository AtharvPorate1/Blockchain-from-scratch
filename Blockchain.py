# Creating a Blockchain from Scratch

import datetime as dt 
import hashlib as hs

class Block:
    def __init__(self, index, timestamp, data, prevhash):
        self.index = index
        self.timestamp = dt.datetime.now()
        self.data = data
        self.prevhash = prevhash
        self.hash = self.hashblock()
    
    def hashblock(self):
        encryption = hs.sha256()
        block_data = {
        "index": self.index,
        "timestamp": self.timestamp,
        "data": self.data,
        "prevhash": self.prevhash,
    }
        block_string = str(block_data)
        encryption.update(block_string.encode("utf-8"))
        return encryption.hexdigest()
    
    @staticmethod
    def genesisblock():
        return Block(0, dt.datetime.now(), "Genesis Transactions", "")
    
    @staticmethod
    def newblock(prevblock):
        index = prevblock.index + 1
        timestamp = dt.datetime.now()
        data = f"Transaction #{index}"
        prevhash = prevblock.hash
        return Block(index, timestamp, data, prevhash)
    
# Initializing the blockchain with the genesis block
Blockchain = [Block.genesisblock()]

# Making this block a prevblock
prevblock = Blockchain[0]

# Adding few more blocks
for i in range(1, 5):
    addblock = Block.newblock(prevblock)
    Blockchain.append(addblock)
    
    # Setting this new block as prevblock
    prevblock = addblock

    print(f"Block ID : #{addblock.index}\n")
    print(f"Timestamp : {addblock.timestamp}\n")
    print(f"Hash of the block : {addblock.hash}\n")
    print(f"Hash of the previous block : {addblock.prevhash}\n")
    print(f"Data of Block : {addblock.data}")



    
        
