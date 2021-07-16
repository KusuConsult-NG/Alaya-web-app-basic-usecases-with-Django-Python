from django.http import HttpResponse
from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON
from hexbytes import HexBytes

# Connecting to a node using the HTTPProvider uri and chainId
w3 = Web3(HTTPProvider('http://47.241.91.2:6789'), chain_id=201030)
platon = PlatON(w3)

#Checking if the connection is valid
true = True
if(w3.isConnected() == true):
    status = "You are connected!"

# Used to get a block number on Alaya/PlatOn
block_number = platon.blockNumber

# Get balance of Lat account address
address ='atp1uug5ar8kx5trs6fp9zrev3xrxrlptrxdaq6jdf'
balance = "Account Balance: "+str(platon.getBalance(address))

# Details about the block below
block_details = platon.getBlock(5821991)

def index(request):
    return HttpResponse(status)