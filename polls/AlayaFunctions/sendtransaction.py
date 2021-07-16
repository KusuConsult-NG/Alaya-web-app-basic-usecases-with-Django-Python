from client_sdk_python import Web3, HTTPProvider
from client_sdk_python.eth import PlatON
from hexbytes import HexBytes

# Connecting to a node using the HTTPProvider uri and chainI
w3 = Web3(HTTPProvider('http://47.241.91.2:6789'), chain_id=201030)
platon = PlatON(w3)

address ='atp1zqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqr5jy24r'
# sendtransaction
to ='atp1pw4z6pypulwsvvr43xsuhax5vcchn20ma2mjce'
w3.personal.unlockAccount(address, "password", 999999)
data = {
    "from": address,
    "to": to,
    "value": 0x10909,
    "gas": 1000000,
    "gasPrice": 1000000000,
}
transaction_hex = HexBytes(platon.sendTransaction(data)).hex()
result = platon.waitForTransactionReceipt(transaction_hex)
print(result)