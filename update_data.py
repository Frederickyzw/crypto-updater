import requests
import pandas as pd
from datetime import datetime
import os

def fetch_crypto(symbol="BTC", currency="USDT", limit=1440):
    url = f"https://min-api.cryptocompare.com/data/v2/histominute?fsym={symbol}&tsym={currency}&limit={limit}"
    r = requests.get(url)
    data = r.json()
    if data["Response"] != "Success":
        raise Exception("Failed to fetch data:", data)

    df = pd.DataFrame(data["Data"]["Data"])
    # ubah kolom time ke datetime
    df["time"] = pd.to_datetime(df["time"], unit="s")
    # urutkan kolom sesuai format yang diinginkan
    df = df[["time", "high", "low", "open", "volumefrom", "volumeto", "close"]]
    # format time ke MM/DD/YYYY HH:MM
    df["time"] = df["time"].dt.strftime("%m/%d/%Y %H:%M")
    return df

def save_csv():
    # buat folder data jika belum ada
    os.makedirs("data", exist_ok=True)
    df = fetch_crypto(symbol="BTC", currency="USDT", limit=1440)
    df.to_csv("data/crypto_data.csv", index=False)
    print(f"[{datetime.now()}] Data updated and saved to data/crypto_data.csv")

if __name__ == "__main__":
    save_csv()
