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

log_trade(
    signal=signal,
    amount=0.001,
    price=df.iloc[-1]["close"],
    capital=capital.capital,
    colchon=capital.colchon,
    beneficio_total=capital.beneficio_total,
    resultado=beneficio
)

