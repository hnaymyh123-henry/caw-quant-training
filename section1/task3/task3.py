import etherscan.accounts as accounts
import etherscan.proxies as proxies
import etherscan.stats as stats
import etherscan.tokens as tokens
from etherscan.contracts import Contract
#import etherscan.transactions as transactions
#from etherscan.blocks import Blocks
import json
import pandas as pd

address = '0x9dd134d14d1e65f84b706d6f205cd5b1cd03a46b'
key = '354XMWXFIA2JXKP7C64N455NX1ZNIKSH18'

#Accounts
api = accounts.Account(address=address, api_key=key)
balance = api.get_balance()
print('balance:', balance)

balance_multiple = api.get_balance_multiple()
print('balance_multiple:', balance_multiple)

#block_mined = api.get_all_blocks_mined(offset=10000, blocktype='blocks')
#print('block_mined:', block_mined)

transaction = api.get_transaction_page(page=1, offset=10)
df_transaction = pd.DataFrame(transaction)
print('transaction:', df_transaction.head())

#all_transaction = api.get_all_transactions(offset=10000, sort='asc')
#df_all_transaction = pd.DataFrame(all_transaction)
#print(all_transaction[0])


#Tokens
contract_address = '0x57d90b64a1a57749b0f932f1a3395792e12e7055'
api2 = tokens.Tokens(contract_address=contract_address, api_key=key)
token = api2.get_token_balance(address=address)
print('token:', token)
total_supply = api2.get_total_supply()
print('total supply:', total_supply)

#Proxies
api3 = proxies.Proxies(api_key=key)
#price = api3.gas_price()
#print('price:', price)

recent_block = api3.get_most_recent_block()
print('recent block:', recent_block)

block_by_number = api3.get_block_by_number(5747732)
print ('block_by_number:', block_by_number)

tx_count = api3.get_block_transaction_count_by_number(block_number='0x10FB78')
print('tx_count', int(tx_count, 16))

#code = api3.get_code('0xf75e354c5edc8efed9b59ee9f67a80845ade7d0c')
#print('code:', code)

#value = api3.get_storage_at('0x6e03d9cce9d60f3e9f2597e13cd4c54c55330cfd', 0x0)
#print('storage at', value)

transaction = api3.get_transaction_by_blocknumber_index(block_number='0x57b2cc',
                                                       index='0x2')
print('transaction by block number:', transaction['transactionIndex'])

TX_HASH = '0x1e2910a262b1008d0616a0beb24c1a491d78771baa54a33e66065e03b1f46bc1'
ransaction = api3.get_transaction_by_hash(
    tx_hash=TX_HASH)
print('transaction by hash:', transaction['hash'])

count = api3.get_transaction_count('0x6E2446aCfcec11CC4a60f36aFA061a9ba81aF7e0')
print('transaction count:', int(count, 16))

receipt = api3.get_transaction_receipt(
    '0xb03d4625fd433ad05f036abdc895a1837a7d838ed39f970db69e7d832e41205d')
print('transaction:', receipt)

uncles = api3.get_uncle_by_blocknumber_index(block_number='0x210A9B',
                                            index='0x0')
print(uncles['uncles'])


#Stats
api4 = stats.Stats(api_key=key)
total_supply = api4.get_total_ether_supply
print('total supply:', total_supply)

last_price = api4.get_ether_last_price()
print('last price:', last_price)


#Contracts
api5 = Contract(address=address, api_key=key)
#abi = api5.get_abi()
#print('abi:',abi)

sourcecode = api5.get_sourcecode()
print(sourcecode[0]['SourceCode'])


#Block
#api7 = Blocks(api_key=key)
#reward = api7.get_block_reward(2165403)
#print(reward)


#Transactions
#api6 = transactions.Transactions(api_key=key)
#TX_HASH = '0x15f8e5ea1079d9a0bb04a4c58ae5fe7654b5b2b4463375ff7ffb490aa0032f3a'
#status = api6.get_status(tx_hash=TX_HASH)
#print ('status:', status)

#TX_HASH = '0x513c1ba0bebf66436b5fed86ab668452b7805593c05073eb2d51d3a52f480a76'
#receipt_status = api6.get_tx_receipt_status(tx_hash=TX_HASH)
#print ('receipt status:', receipt_status)