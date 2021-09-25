from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
print(cg.get_price('bitcoin', 'usd'))
