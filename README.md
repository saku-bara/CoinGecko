# CoinGecko
 CoinGecko top currencies 
 
### Installation 

```
pip install pycoingecko
```

## edit path in the script

Provide proper path to the file where data will be saved. You need to edit `test.py` file. In my case it is:

```python
sys.path.append('D:\\assignment1')
```

### Usage 

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

```python
# after installing the project and changing path
cd Coingecko\test
python test.py
```

### Example

```
enter the number: 10
['Bitcoin', 'Ethereum', 'Cardano', 'Tether', 'Binance Coin', 'XRP', 'Solana', 'Polkadot', 'USD Coin', 'Dogecoin']
```
