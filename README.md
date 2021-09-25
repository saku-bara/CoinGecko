# CoinGecko
 CoinGecko top currencies 
 
### Installation 

```
pip install pycoingecko
```

### Usage 

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Example

```python
cg.get_coins_markets('usd')  # n = 10
['Bitcoin', 'Ethereum', 'Cardano', 'Tether', 'Binance Coin', 'XRP', 'Solana', 'Polkadot', 'USD Coin', 'Dogecoin']
```
