from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

# Connecting to a node using the HTTPProvider uri and chainId
w3 = Web3(HTTPProvider("http://47.241.98.219:6789"),chain_id = 100)
platon = PlatON(w3)

# get Balance
address ='lat1uqhqjnfrzm3qytm95ym6j8fkl0w6xtncjwzhxu'
balance = platon.getBalance(address)
print("Account Balance: "+str(balance))