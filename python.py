from ib_insync import *

def main():
    # Connexion à TWS ou IB Gateway
    ib = IB()
    ib.connect('92.154.106.15', 7497, clientId=2)  # Assurez-vous que le port et clientId correspondent à votre configuration

    ticker = input("Entrez le ticker de l'action à acheter : ")
    amount_in_eur = float(input("Entrez le montant en euros : "))

    # Conversion EUR en USD (à adapter selon le taux de change actuel)
    exchange_rate = 1.1
    amount_in_usd = amount_in_eur * exchange_rate

    # Création de l'objet pour le stock
    stock = Stock(ticker, 'SMART', 'USD')

    # Récupération des informations de marché
    ib.qualifyContracts(stock)
    market_data = ib.reqMktData(stock, '', False, False)
    ib.sleep(2)  # Attendre que les données soient reçues

    if market_data.last is not None:
        market_price = market_data.last
        quantity = int(amount_in_usd // market_price)
        order = MarketOrder('BUY', quantity)
        trade = ib.placeOrder(stock, order)
        ib.sleep(1)  # Attendre que l'ordre soit transmis
        print(f"Ordre d'achat placé pour {quantity} actions de {ticker} à {market_price} USD chacune.")
    else:
        print("Prix du marché non disponible.")

    ib.disconnect()

if __name__ == "__main__":
    main()