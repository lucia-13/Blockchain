import datetime
from hashlib import sha256
#Code done by LUCIA FUENTES, inspired by codecademy
#class for the blockchains' cell, the blopck

class Block:
    #constructor of a block object, defined by a time stamp, traqnsaction dictionary,  and previous block hash, and the hash
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.generate_hash()

#generation of hash for each block,, based on its properties, using imported sha 256 hash funciton
    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()
#printing of a block content
    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash)