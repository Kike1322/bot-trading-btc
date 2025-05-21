from data import get_btc_data
from strategy import generate_signal
from capital_manager import CapitalManager
import os
print("Directorio actual:", os.getcwd())
from trader import ejecutar_operacion
from logger import log_trade

import os
print("Contenido de la carpeta actual:", os.listdir())
#from alertas_email2 import enviar_alerta_email


capital = CapitalManager(20)

df = get_btc_data()
signal = generate_signal(df)

print(f"Señal generada: {signal}")

orden = ejecutar_operacion(signal)

if signal == "buy":
    beneficio = 50
elif signal == "sell":
    beneficio = -30
else:
    beneficio = 0

g, r, reinv = capital.repartir_beneficio(beneficio)

print(f"""
Capital actual: {capital.capital:.2f} USDT
Colchón: {capital.colchon:.2f} USDT
Ganancia retirada: {capital.beneficio_total:.2f} USDT
""")

latest = df.iloc[-1]

log_trade(
    signal=signal,
    amount=0.001,
    price=latest["close"],
    capital=capital.capital,
    colchon=capital.colchon,
    beneficio_total=capital.beneficio_total,
    resultado=beneficio,
    rsi=round(latest['rsi'], 2),
    sma=round(latest['sma'], 2),
    ema=round(latest['ema'], 2),
    macd=round(latest['macd'], 6),
    macd_signal=round(latest['macd_signal'], 6),
    adx=round(latest['adx'], 2),
    stoch_k=round(latest['stoch_k'], 2),
    stoch_d=round(latest['stoch_d'], 2),
)


