import ccxt
import json

def ejecutar_operacion(signal):
    with open("settings.json") as f:
        config = json.load(f)

    exchange = ccxt.binance({
        'apiKey': config["apiKey"],
        'secret': config["secret"],
        'enableRateLimit': True
    })

    exchange.set_sandbox_mode(config.get("paper_mode", True))

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
