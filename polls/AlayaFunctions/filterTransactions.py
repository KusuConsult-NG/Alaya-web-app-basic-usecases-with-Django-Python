
from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

# w3 = Web3(HTTPProvider('http://47.241.98.219:6789 '), chain_id=210309)

w3 = Web3(HTTPProvider('http://47.241.91.2:6789'), chain_id=201030)
platon = PlatON(w3)
print(platon.filter('latest'))
print(platon.filter('pending'))
print(platon.filter({'fromBlock': 1000000,'toBlock': 1000100,'address':'atp1uug5ar8kx5trs6fp9zrev3xrxrlptrxdaq6jdf'}))

