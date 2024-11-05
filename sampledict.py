Dict = {"CRV": "CASH RECEIPT", "CPV": "CASH PAYMENT","BRV":"BANK RECEIPT","BPV":"BANK PAYMENT","CON":"CONTRA","JOU":"JOURNAL" }
print(Dict)
print(Dict['CRV'])
print(Dict['CPV'])
print(Dict['BRV'])
print(Dict['BPV'])
print(Dict['CON'])
print(Dict['JOU'])
if Dict['CRV'] == "CASH RECEIPT":
    mdcr = "CRV"
    print(mdcr)
    