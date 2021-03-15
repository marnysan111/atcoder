import requests
import json

# エンドポイント
url = 'http://192.168.1.10:8080/json'
# リクエスト
res = requests.get(url)
# 取得したjsonをlists変数に格納
lists = json.loads(res.text)

print(lists[0])

"""
for list in lists:
    print(list['name'] + ': ' + list['alpha2Code'])
"""