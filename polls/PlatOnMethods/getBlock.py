from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

# Connecting to a node using the HTTPProvider uri and chainId
w3 = Web3(HTTPProvider("http://47.241.98.219:6789/"))
platon = PlatON(w3)
block_number = platon.blockNumber
print("Block Number: "+str(block_number))