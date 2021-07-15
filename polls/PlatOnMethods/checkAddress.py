from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

# Connecting to a node using the HTTPProvider uri and chainId
w3 = Web3(HTTPProvider("http://47.241.98.219:6789"),chain_id = 100)
platon = PlatON(w3)
#Checking if an address is valid
print(w3.isAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601'))
