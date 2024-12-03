# MultiversX Account Generator

This script generates MultiversX accounts across different shards and automatically claims testnet tokens for each account using the r3d4.fr faucet.

## Features

- Generates accounts distributed across all shards (0, 1, and 2)
- Automatically claims testnet tokens for each generated account
- Saves account details (including mnemonic phrases) in individual JSON files
- Creates a summary file with all generated accounts

## Requirements

- Python 3.7+
- Virtual environment (recommended)

## Installation

1. Create a virtual environment: 
```bash
python3 -m venv venv
```

2. Activate the virtual environment:
On Windows:
```bash
venv\Scripts\activate
```
On Linux/Mac:
```bash
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Run the script:
```bash
python3 generate_accounts.py
```

The script will:
1. Generate 3 accounts per shard (9 accounts total)
2. Claim testnet tokens for each account
3. Save account details in the `wallets` directory
4. Create a summary in `accounts_summary.json`

## Generated Files

- `wallets/wallet_shardX_Y.json`: Individual wallet files containing:
  - Mnemonic phrase
  - Address
  - Shard number
  - Faucet transaction hash (if claim was successful)
- `accounts_summary.json`: Summary of all generated accounts

## Faucet Transaction Hashes

Below are the transaction hashes for the token claims. This section should be updated after running the script:

| Shard | Address | Transaction Hash |
|-------|---------|-----------------|
| 0 | erd1k8ha946d3zwjrvr849duhk5yl7wv7k3ljsddhv88jpr0yz5046uqknf9sm | https://testnet-explorer.multiversx.com/transactions/4418f128514daedb5e065bb725b7f5e5441c2590e6db955b6fafceb3f262f710 |
| 0 | erd12fq7w7wu9nct9ct8v6zt2jh0pn0cjdumxnpk6myzfrcmlf0s802qjzlqjs | https://testnet-explorer.multiversx.com/transactions/f277529a6383bd0acf6b7b069c5babb8b49566c9e6b8172fb47194db47b68913 |
| 0 | erd1qxgd6q769mv06upfgc8e3rn5t5ulzeszuep4h90dc3ypqn2fmxyqd2wsza | https://testnet-explorer.multiversx.com/transactions/d6733e0abff9c835fa2a5f925a88e1ac589fc022be5c6b0b24e728bd90e4985e |
| 1 | erd1q0nj70ncj9twljqvlcz507lj0uhjeds33n9cms0q0wkuevszuneslyqpnq | https://testnet-explorer.multiversx.com/transactions/405ef1d07db66cc855fbc6843acb041018fc6a31c1f53fd0bdabc8044455a30c |
| 1 | erd1k84xt0vk0hpwwsn9wr7htkmn4t8yeq3tk57hj4kg8a2w4630c5csm8367x | https://testnet-explorer.multiversx.com/transactions/0cd66cdf18fa5350c024059e65818e6c7d7afb817c12dcfae69186e91196ce14 |
| 1 | erd169ady67k7m6dldks2hjsu3jmxwc7l60p7r75zrwkp5kyydmvg7ps786yry | https://testnet-explorer.multiversx.com/transactions/b332fcd5dcd743213d0f64ada6cda32d46ca974c9dab38700b847270407cadb0 |
| 2 | erd1scvzv4e2r6hl0g5kjrm9k9zgvqccux299nydzvf3rgnlwhl38cmqzq0pk8 | https://testnet-explorer.multiversx.com/transactions/695ab26e664f768ac1ec71b97b2a18a260cbe65873b60e75adfcff6a7d01a2e3 |
| 2 | erd109mmtk7rypyyx8mzsxsa2f5clwg2hxz8a68v9lwaj2u3tk2edp8q074ykk | https://testnet-explorer.multiversx.com/transactions/7fc0bf4df28a481c9ecda9272823e9ea228936e4a141083e0c1aca37e7dcd2b8 |
| 2 | erd1d7fhvdc5dj8zgqvn0chqjkjc8h7x2gqtxduzx9n62utvjdzfvdmqy0sf6c | https://testnet-explorer.multiversx.com/transactions/0b73eb6bdc17ee32a2cf0c7fe2da8c496c9265765e3bb4c9e6df72038db3cf5f |

## Security Notice

⚠️ **Important**: The generated wallet files contain mnemonic phrases. Keep them secure and never share them with anyone.

## ⚠️ SECURITY WARNING

**NEVER USE THE GENERATED WALLETS FROM `/wallets` DIRECTORY ON MAINNET!**

These wallets are generated for testing purposes only and should be used exclusively on testnet or devnet. Using these wallets on mainnet would be extremely dangerous for several reasons:

1. The private keys and mnemonics are stored in plain text
2. The wallet files are potentially tracked in git history
3. The code is public and accessible to everyone

## Network

This script is configured to work with the MultiversX Testnet. The claimed tokens are test tokens (T-EGLD) and have no real value.

## License

This project is licensed under the MIT License - see the LICENSE file for details.