import requests
 
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude":52.07403900458741,
    "longitude":-1.0189248964611797,
    "current": (
        "temperature_2m,"
        "relative_humidity_2m,"
        "apparent_temperature,"
        "wind_speed_10m,"
        "is_day"
    ),
    "timezone": "Europe/London"
}

# Part 2: 發送 GET 請求
response = requests.get(
    url,
    params=params,
    timeout=10
)
# 檢查 HTTP 回應狀態
response.raise_for_status()

# Part 3: 解析 JSON 回應(剝洋蔥)
data = response.json()
current = data["current"]

time = current["time"]
temperature = current["temperature_2m"]
humidity = current["relative_humidity_2m"]
apparent_temperature = current["apparent_temperature"]
wind_speed = current["wind_speed_10m"]
# 讀取 is_day 欄位
is_day = current["is_day"]


# Part 4: 印出結果
print("=" * 40)
print("API Weather Explorer")
print("=" * 40)
print(f"資料時間：{time}")
print(f"目前溫度：{temperature} °C")
print(f"相對濕度：{humidity} %")
print(f"體感溫度：{apparent_temperature} °C")
print(f"風速：{wind_speed} km/h")

print(f"白天/夜晚: {is_day}")
print("=" * 40)
print("白天" if is_day else "夜晚")