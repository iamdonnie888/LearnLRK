import requests

# 设置自定义 User-Agent
headers = {
    "User-Agent": "MyCustomUserAgent/1.0"
}

# 发送请求
response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.json())
