import os
import csv
from datetime import datetime

def log_trade(signal, amount, price, capital, colchon, beneficio_total,
              rsi=None, sma=None, ema=None, macd=None, macd_signal=None,
              adx=None, stoch_k=None, stoch_d=None, resultado="N/A"):

    filename = "historial_trading.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "fecha", "señal", "monto", "precio", "resultado",
                "capital", "colchon", "beneficio_total",
                "RSI", "SMA", "EMA", "MACD", "MACD_signal",
                "ADX", "Stoch_K", "Stoch_D"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            signal, amount, price, resultado,
            round(capital, 2), round(colchon, 2), round(beneficio_total, 2),
            rsi, sma, ema, macd, macd_signal,
            adx, stoch_k, stoch_d
        ])
