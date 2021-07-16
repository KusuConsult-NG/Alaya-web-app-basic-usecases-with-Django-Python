from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

# Connecting to a node using the HTTPProvider uri and chainId
w3 = Web3(HTTPProvider('http://47.241.91.2:6789'), chain_id=201030)
platon = PlatON(w3)

# get Balance
address ='atp1pw4z6pypulwsvvr43xsuhax5vcchn20ma2mjce'
balance = platon.getBalance(address)
print("Account Balance: "+str(balance))