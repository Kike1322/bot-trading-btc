import pandas as pd
import ta

def generate_signal(df):
    df['sma'] = df['close'].rolling(14).mean()
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    latest = df.iloc[-1]

    if latest['rsi'] < 30 and latest['close'] > latest['sma']:
        return "buy"
    elif latest['rsi'] > 70 and latest['close'] < latest['sma']:
        return "sell"
    else:
        return "hold"
