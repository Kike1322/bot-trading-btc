import ccxt
import os

def ejecutar_operacion(signal):
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    paper_mode = os.getenv("PAPER_MODE", "True").lower() == "true"

    exchange = ccxt.bybit({
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': True,
    })

    exchange.set_sandbox_mode(paper_mode)

    symbol = 'BTC/USDT'
    amount = 0.001
    order = None

    try:
        if signal == "buy":
            order = exchange.create_market_buy_order(symbol, amount)
        elif signal == "sell":
            order = exchange.create_market_sell_order(symbol, amount)
        else:
            print("No se ejecutó ninguna orden (hold).")
            return None

        print(f"Orden ejecutada: {order['side']} {order['amount']} {order['symbol']}")
        return order

    except Exception as e:
        print("Error al ejecutar la orden:", str(e))
        return None

