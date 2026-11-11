import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 25.03,  # 緯度
    "longitude": 121.56,  # 經度
    "hourly": "temperature_2m",  # 離地 2 公尺高的氣溫
    "forecast_days": 2,  # 未來2天
    "timezone": "Asia/Taipei",
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()
df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])

print(df.head())
print("資料形狀：", df.shape)
print("平均溫度：", df["temperature_2m"].mean())
print("最高溫度：", df["temperature_2m"].max())
print("最低溫度：", df["temperature_2m"].min())

plt.figure(figsize=(10, 5))
plt.plot(df["time"], df["temperature_2m"], marker="o")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Hourly Temperature")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
