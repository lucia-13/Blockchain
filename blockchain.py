from block import Block
#Code done by LUCIA FUENTES, inspired by codecademy


#class for the blockchain datastructure, built from individual transaction blocks, and  a genesis/initial block
class Blockchain:
    #constructor of the blockchain data structure including a chain list of blocks, unconfirmed transactions, and  agenesis block
    def __init__(self):
        self.chain = []
        self.unconfirmed_transactions = []
        self.genesis_block()
#conmstructor of a defualt genesis block, that pints to a 0 previous_hash
    def genesis_block(self):
        transactions = []
        genesis_block = Block(transactions, "0")
        genesis_block.generate_hash()
        self.chain.append(genesis_block)

#fucntion to add block to the tail fo the blockchain, implements generate_hash fucntion for generating hash for the new block,
    # uses proof of work to check for validity
    def add_block(self, transactions):
        previous_block_hash = self.chain[len(self.chain) - 1].hash
        new_block = Block(transactions, previous_block_hash)
        proof = self.proof_of_work(new_block)
        self.chain.append(new_block)
        return proof, new_block
#print whole blockchain using block print_contents() fucntion
    def print_blocks(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print("Block {} {}".format(i, current_block))
            current_block.print_contents()
#check if blockchin is valid, by comparing cached hash of current block with updated hash, then comapring
    # previous block's updated hash with the current's block previous hash
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("Current hash does not equal generated hash")
                return False
            if current.previous_hash != previous.generate_hash():
                print("Previous block's hash got changed")
                return False
        return True
#function implementating of work, iterates toll the nonce(0 till succesfull)
    # used for the hash generation creates a hash with 2(difficulty variable default) leading 0s

    def proof_of_work(self, block, difficulty=2):
        proof = block.generate_hash()
        while proof[:2] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
