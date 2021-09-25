from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

n = int(input("enter the number: "))
my_list = cg.get_coins_markets('usd')
output = []
for i in range(0,n):
    output.append(my_list[i]['name'])

print(output)
