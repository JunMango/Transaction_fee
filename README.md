# Transaction_fee

수업 시간에 매번 curl 명령어를 사용하여

```
curl https://bitcoin-mainnet.public.blastapi.io \
--request POST \
--header 'content-type: text/plain;' \
--data '{"jsonrpc": "1.0", "id": "test", "method": "getrawtransaction", "params": ["61247a248efdf6181d806dc2a3634ebde0d5a51c4cb9dbdc666f797ed4f2b79f", true]}'
{"result":{"txid":"61247a248efdf6181d806dc2a3634ebde0d5a51c4cb9dbdc666f797ed4f2b79f",
"hash":"61247a248efdf6181d806dc2a3634ebde0d5a51c4cb9dbdc666f797ed4f2b79f","version":2,"size":223,"vsize":223,"weight":892,"locktime":816010,
"vin":[{"txid":"18b8202617cf56a2665f68ea71424ed302f581bd44e6c16f16b0a4597caa9a1c","vout":1,
"scriptSig":{"asm":"3045022100cb80bd593df0a6037e2211fffaca7bb60b73f8bd4af72b40ddb9913aad751315022001917cdf5c64d546bd3be8c954e8120c949fcd955628afc962e91a5ad52428c2[ALL] 02cc3b7a4add08664cbedaa9a29d47895545e33855aa74f3e49afb7462b380a509",
"hex":"483045022100cb80bd593df0a6037e2211fffaca7bb60b73f8bd4af72b40ddb9913aad751315022001917cdf5c64d546bd3be8c954e8120c949fcd955628afc962e91a5ad52428c2012102cc3b7a4add08664cbedaa9a29d47895545e33855aa74f3e49afb7462b380a509"},
"sequence":4294967293}],"vout":[{"value":0.00300000,"n":0,"scriptPubKey":{"asm":"0 d53499cc05b1d32aed54c40ca62413ee650ebafb",
"desc":"addr(bc1q656fnnq9k8fj4m25csx2vfqnaejsawhmjxsmj6)#hmp0hrj4",
"hex":"0014d53499cc05b1d32aed54c40ca62413ee650ebafb","address":"bc1q656fnnq9k8fj4m25csx2vfqnaejsawhmjxsmj6","type":"witness_v0_keyhash"}},
{"value":0.03239546,"n":1,"scriptPubKey":{"asm":"OP_DUP OP_HASH160 9676c0c6f0718ccb6dc18e0cf04d066de9ce016f OP_EQUALVERIFY OP_CHECKSIG",
"desc":"addr(1Eiact3kAA2obB1n4u5Z1oY1s3Nsh73BY8)#re2wp40v","hex":"76a9149676c0c6f0718ccb6dc18e0cf04d066de9ce016f88ac",
"address":"1Eiact3kAA2obB1n4u5Z1oY1s3Nsh73BY8","type":"pubkeyhash"}}],
"hex":"02000000011c9aaa7c59a4b0166fc1e644bd81f502d34e4271ea685f66a256cf172620b818010000006b483045022100cb80bd593df0a6037e2211fffaca7bb60
b73f8bd4af72b40ddb9913aad751315022001917cdf5c64d546bd3be8c954e8120c949fcd955628afc962e91a5ad52428c2012102cc3b7a4add08664cbedaa9a29d47895545e33855aa74f3e49a
fb7462b380a509fdffffff02e093040000000000160014d53499cc05b1d32aed54c40ca62413ee650ebafb7a6e3100000000001976a9149676c0c6f0718ccb6dc18e0cf04d066de9ce016f88ac8a730c00",
"blockhash":"000000000000000000000509455c894e1410baf15230036827dc2e9e0fb49f95",
"confirmations":46039,
"time":1699570862,
"blocktime":1699570862},
"error":null,"id":"test"}
```

다음과 같은 것들을 터미널 안에서 해결하고 값을 찾는게 굉장히 불편하여 복습할겸 코드로 옮겨 보았습니다 

효율적으로 적지 않았기 때문에 코드 자체는 리펙토링이 필요해 보입니다.
