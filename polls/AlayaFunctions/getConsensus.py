from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

# Connecting to a node using the HTTPProvider uri and chainId
w3 = Web3(HTTPProvider('http://47.241.91.2:6789'), chain_id=201030)
platon = PlatON(w3)
# Will be used To get Blocknumber that wil be used to track the miner
print(platon.consensusStatus)