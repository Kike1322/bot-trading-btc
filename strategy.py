import pandas as pd
import ta

def generate_signal(df):
    # Indicadores técnicos
    df['sma'] = df['close'].rolling(window=14).mean()
    df['ema'] = df['close'].ewm(span=14, adjust=False).mean()
    
    macd = ta.trend.MACD(df['close'])
    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()
    
    adx = ta.trend.ADXIndicator(df['high'], df['low'], df['close'], window=14)
    df['adx'] = adx.adx()
    
    stochastic = ta.momentum.StochasticOscillator(df['high'], df['low'], df['close'], window=14, smooth_window=3)
    df['stoch_k'] = stochastic.stoch()
    df['stoch_d'] = stochastic.stoch_signal()
    
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    latest = df.iloc[-1]

    # Condiciones para comprar
    buy_cond = (
        (latest['rsi'] < 30) and
        (latest['close'] > latest['ema']) and
        (latest['macd'] > latest['macd_signal']) and
        (latest['adx'] > 25) and  # tendencia fuerte
        (latest['stoch_k'] < 20) and
        (latest['stoch_k'] > latest['stoch_d'])  # cruce alcista stochastic
    )

    # Condiciones para vender
    sell_cond = (
        (latest['rsi'] > 70) and
        (latest['close'] < latest['ema']) and
        (latest['macd'] < latest['macd_signal']) and
        (latest['adx'] > 25) and  # tendencia fuerte
        (latest['stoch_k'] > 80) and
        (latest['stoch_k'] < latest['stoch_d'])  # cruce bajista stochastic
    )

    if buy_cond:
        return "buy"
    elif sell_cond:
        return "sell"
    else:
        return "hold"

