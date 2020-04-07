from blockchain import Blockchain
#Code done by LUCIA FUENTES, inspired by codecademy
#testing
block_one_transactions = {"sender":"Lucia", "receiver": "Julia", "amount":"999"}
block_two_transactions = {"sender": "Diego", "receiver":"Laika", "amount":"666"}
block_three_transactions = {"sender":"Frida", "receiver":"Rex", "amount":"420"}
fake_transactions = {"sender": "Renata", "receiver":"Jaime, Juan Pablo", "amount":"1398"}


local_blockchain = Blockchain() #instattiation of a blockchain object
local_blockchain.print_blocks() #print, to check that a default genesis block is created

#create 3 blocks
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks() #print local_clockchain, now should have 3 blocks + genesis block

local_blockchain.chain[2].transactions = fake_transactions #try to chnage one block data
local_blockchain.validate_chain() #will notice the invalidity