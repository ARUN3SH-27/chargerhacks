from solana.account import Account
from solana.rpc.api import Client

# Initialize a Solana account
user_account = Account()

# Connect to a Solana RPC server
rpc_url = "https://api.mainnet-beta.solana.com"
client = Client(rpc_url)

# Simulate a charity's wallet (in practice, charities would create their own wallets)
charity_account = Account()

# Prompt the user to input a donation amount
donation_amount = float(input("Enter the donation amount in SOL: "))

# Send the donation to the charity
transaction = client.transfer(user_account, charity_account.public_key(), int(donation_amount * 10**9))

# Sign and send the transaction
transaction.sign(user_account)
tx_hash = client.send_transaction(transaction)

# Check the transaction status
confirmation_status = client.get_confirmation_status(tx_hash)
if confirmation_status == "confirmed":
    print(f"Donation of {donation_amount} SOL sent to the charity.")
else:
    print("Transaction failed or is still pending.")
