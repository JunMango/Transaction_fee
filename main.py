import requests

print("hi this is bitcoin fee calculator from junMango")

# hash = input() # 해쉬 값 받기
hash = "61247a248efdf6181d806dc2a3634ebde0d5a51c4cb9dbdc666f797ed4f2b79f"
# test hash value
# 61247a248efdf6181d806dc2a3634ebde0d5a51c4cb9dbdc666f797ed4f2b79f

# test url
url = "https://bitcoin-mainnet.public.blastapi.io"
# header
headers = {
    'content-type': 'text/plain',
}
#데이터 형식 => method 마다 이름 바꿔야 함.
data = {
    "jsonrpc": "1.0",
    "id": "test",
    "method": "getrawtransaction",
    "params": [hash, True]
}
response = requests.post(url, headers=headers, json=data)
data = response.json()
# 응답 결과 출력
vin_txid = data['result']['vin'][0]['txid']
# vout에서 첫 번째 value와 n 가져오기
vout_value_1 = data['result']['vout'][0]['value']
vout_value_2 = data['result']['vout'][1]['value']
# vout_n = data['result']['vout'][0]['n']

print(vin_txid)
print(vout_value_1)
print(vout_value_2)
print(data)

data_tx = {
    "jsonrpc": "1.0",
    "id": "test",
    "method": "getrawtransaction",
    "params": [vin_txid, True]
}
response_tx = requests.post(url, headers=headers, json=data_tx)

data_vintx = response_tx.json()
vout_value_3 = data_vintx['result']['vout'][1]['value']
print(vout_value_3)

fee_result = vout_value_3 - (vout_value_1+vout_value_2)

print("Transaction 수수료는 다음과 같습니다 => "+str(fee_result) + " BTC")