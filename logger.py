import csv
import os
from datetime import datetime

def log_trade(signal, amount, price, capital, colchon, beneficio_total, resultado="N/A"):
    filename = "historial_trading.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "fecha", "señal", "monto", "precio", "resultado",
                "capital", "colchon", "beneficio_total"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            signal, amount, price, resultado,
            round(capital, 2), round(colchon, 2), round(beneficio_total, 2)
        ])
