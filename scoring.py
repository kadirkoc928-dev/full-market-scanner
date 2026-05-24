def score_stock(df):

    last = df.iloc[-1]

    score = 0

    # Trend
    if last["EMA20"] > last["EMA50"]:
        score += 25

    # Momentum
    if 45 <= last["RSI"] <= 65:
        score += 15

    # MACD
    if last["MACD"] > last["MACD_SIG"]:
        score += 15

    # Volume Accumulation
    if last["VOL_RATIO"] > 1.5:
        score += 20

    # Breakout behavior
    if last["Close"] > df["Close"].max() * 0.98:
        score += 25

    return min(score, 100)
