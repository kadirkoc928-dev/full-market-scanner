import yfinance as yf
import ta

def get_data(symbol):
    return yf.Ticker(symbol).history(period="6mo", interval="1d")

def add_indicators(df):
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)
    df["EMA20"] = ta.trend.ema_indicator(df["Close"], 20)
    df["EMA50"] = ta.trend.ema_indicator(df["Close"], 50)

    df["MACD"] = ta.trend.macd(df["Close"])
    df["MACD_SIG"] = ta.trend.macd_signal(df["Close"])

    df["VOL_AVG"] = df["Volume"].rolling(20).mean()
    df["VOL_RATIO"] = df["Volume"] / df["VOL_AVG"]

    return df
