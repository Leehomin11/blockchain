import hashlib

def hashGenerator(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()
class Block:
    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash

class MyBlockchain:
    def __init__(self):
        hashLast = hashGenerator('last_gen')
        hashFirst = hashGenerator('first_gen')

        genesis = Block('gen_data', hashFirst, hashLast)
        self.chain = [genesis]
    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        hash = hashGenerator(data+prev_hash)
        block = Block(data,hash,prev_hash)
        self.chain.append(block)

blch = MyBlockchain()
blch.add_block('A')
blch.add_block('B')
blch.add_block('C')
blch.add_block('D')
blch.add_block('E')
blch.add_block('F')
blch.add_block('G')
blch.add_block('H')
blch.add_block('I')
blch.add_block('J')
blch.add_block('K')
blch.add_block('L')
blch.add_block('M')
blch.add_block('N')
blch.add_block('O')
blch.add_block('P')
blch.add_block('Q')
blch.add_block('R')
blch.add_block('S')
blch.add_block('T')
blch.add_block('U')
blch.add_block('V')
blch.add_block('W')
blch.add_block('X')
blch.add_block('Y')
blch.add_block('Z')


for block in blch.chain:
    print(block.__dict__)
