import etherscan.accounts as accounts
import etherscan.proxies as proxies
import etherscan.stats as stats
import etherscan.tokens as tokens
import json
import pandas as pd

address = '0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b'
key = '354XMWXFIA2JXKP7C64N455NX1ZNIKSH18'

api = accounts.Account(address=address, api_key=key)
transaction = api.get_transaction_page(page=1, offset=10)
df_transaction = pd.DataFrame(transaction)
print('transaction:', df_transaction.head())

api2 = tokens.Tokens(contract_address=address, api_key=key)
token = api2.get_token_balance(address=address)
print('token:', token)

api3 = proxies.Proxies(api_key=key)
block = api3.get_most_recent_block()
print('block:', block)

api4 = stats.Stats(api_key=key)
total_supply = api4.get_total_ether_supply
print('total supply:', total_supply)
