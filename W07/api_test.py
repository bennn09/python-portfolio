import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
"latitude": 25.03361,
"longitude": 121.56444,
"current": "temperature_2m",
"timezone": "Asia/Taipei"
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()
data = response.json()
print(data)

# 1. 先取得第一層 current 字典
current = data["current"]
# 2. 取得 temperature_2m 的目標值
temperature = current["temperature_2m"]
# 3. 印出結果
print(f"現在經度 {params['longitude']} 緯度 {params['latitude']} 的溫度為 {temperature}°C")
