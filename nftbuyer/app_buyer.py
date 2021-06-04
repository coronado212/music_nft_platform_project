import os
import json
from web3 import Web3
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

################################################################################
# Contract Helper function:
################################################################################


@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./contracts_copy/compiled/musicnft_abi.json')) as f:
        musicnft_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=musicnft_abi
    )

    return contract
    
contract = load_contract()

################################################################################
# Register New Audio
################################################################################
st.title("Buy New Audio")
# accounts = w3.eth.accounts
audio_hashes=['fdsafd', 'fdsafds,a', 'fdsafdsa']
# get the full list of tokens and filter by where owner is artist.

# Get a list of tokens available for sale
# token_uri = contract.functions.tokenURI(token_id).call()


# Use a streamlit component to get the list of tokens available 
address = st.selectbox("Select Audio", options=audio_hashes)

st.markdown(f'Here is information about seledted token')
         #   {token.functions.get_perks()}')

# Use button to initiate purchase
if st.button("Purchase"):

    # Use the contract to send a transaction to the registerAudio function
    tx_hash = contract.functions.purchase(
        address,
        audio_uri
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt Mined:")
    st.write(dict(receipt))
    
    st.write(f'Congrats! You just bought  a {token.functions.getType()}') 

st.markdown("---")

################################################################################
# Purchase a Token
################################################################################
if st.button("Purchase NFT"):

    # Use the contract to purchase an NFT 
    tx_hash = contract.functions.transfer(
        address,
        audio_uri,
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt Mined:")
    st.write(dict(receipt))
    
    st.write(f'Congrats! You just bought the BeatBlocks Ultimate VIP Experience!') 
    # {token.functions.getType()}') 

st.markdown("---")