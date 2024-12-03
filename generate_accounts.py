from pathlib import Path
from multiversx_sdk import Address, AddressComputer
from multiversx_sdk import Mnemonic, UserWallet
from multiversx_sdk import ProxyNetworkProvider
import json
import requests
import time

class AccountGenerator:
    def __init__(self, network="testnet"):
        self.network = network
        self.proxy = ProxyNetworkProvider(f"https://{network}-api.multiversx.com")
        self.address_computer = AddressComputer(number_of_shards=3)
        self.output_dir = Path("./wallets")
        self.output_dir.mkdir(exist_ok=True)
        self.faucet_url = "https://api.r3d4.fr/faucet/list"  # Faucet URL
        
    def generate_account(self):
        """Generate a new wallet and return its details"""
        mnemonic = Mnemonic.generate()
        secret_key = mnemonic.derive_key(0)
        wallet = UserWallet.from_secret_key(secret_key, "password")
        
        # Get public key and address
        public_key = secret_key.generate_public_key()
        address = Address(public_key.buffer, "erd")
        
        return {
            "mnemonic": mnemonic.get_text(),
            "address": address.to_bech32(),
            "shard": self.address_computer.get_shard_of_address(address)
        }

    def generate_accounts_by_shard(self, accounts_per_shard=3):
        """Generate specified number of accounts per shard and claim tokens"""
        accounts = {0: [], 1: [], 2: []}
        
        while any(len(shard_accounts) < accounts_per_shard for shard_accounts in accounts.values()):
            account = self.generate_account()
            shard = account["shard"]
            
            if len(accounts[shard]) < accounts_per_shard:
                # Claim tokens from faucet
                faucet_result = self.claim_faucet(account["address"])
                if faucet_result:
                    account["faucet_tx_hash"] = faucet_result.get("tx_result")
                
                accounts[shard].append(account)
                
                # Save wallet to file
                wallet_path = self.output_dir / f"wallet_shard{shard}_{len(accounts[shard])}.json"
                with open(wallet_path, 'w') as f:
                    json.dump(account, f, indent=4)
                
                print(f"Generated account in shard {shard}: {account['address']}")
                print(f"Saved to: {wallet_path}")
                print("-" * 80)
                
                # Wait between requests
                time.sleep(2)
        
        return accounts

    def claim_faucet(self, address):
        """Claim tokens from faucet for a given address"""
        try:
            payload = {
                "formdata": {
                    "network": "T",  # T testnet
                    "token": "1",    # Token ID pour xEGLD
                    "address": address,
                    "amount": "1"    # 1 xEGLD
                }
            }
            headers = {
                "Content-Type": "application/json"
            }
            
            response = requests.post(self.faucet_url, json=payload, headers=headers)
            
            if response.status_code == 200:
                print(f"Successfully claimed tokens for {address}")
            else:
                print(f"Failed to claim tokens for {address}: {response.text}")
                return None
                
        except Exception as e:
            print(f"Error claiming tokens for {address}: {str(e)}")
            return None

def main():
    # Initialize generator
    generator = AccountGenerator(network="testnet")
    
    # Generate 3 accounts per shard
    accounts = generator.generate_accounts_by_shard(3)
    
    # Save all accounts to a summary file
    with open("accounts_summary.json", 'w') as f:
        json.dump(accounts, f, indent=4)
    
    print("\nGeneration complete!")
    print(f"Total accounts generated: {sum(len(shard) for shard in accounts.values())}")
    print("Summary saved to: accounts_summary.json")

if __name__ == "__main__":
    main() 