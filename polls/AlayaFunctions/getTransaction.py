from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON

w3 = Web3(HTTPProvider('http://47.241.91.2:6789'), chain_id=201030)
platon = PlatON(w3)
print(w3.isConnected())
print(platon.getTransaction('0x7468ed943204cd2304b2dac5399dd4afa30331136fb41e4aa634c33285ea16c4'))
