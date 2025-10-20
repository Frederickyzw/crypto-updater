from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(title="Crypto Price API")

@app.get("/")
def root():
    return {"message": "Welcome to Crypto Price API (Hugging Face)"}

@app.get("/latest")
def get_latest():
    df = pd.read_csv("data/crypto_data.csv")
    last_row = df.iloc[-1].to_dict()
    return {"latest": last_row}

@app.get("/ohlc")
def get_all():
    df = pd.read_csv("data/crypto_data.csv")
    return df.to_dict(orient="records")