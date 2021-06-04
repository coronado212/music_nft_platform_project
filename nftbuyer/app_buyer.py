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
    with open(Path('./contracts_buyer/compiled/musicnftbuyer_abi.json')) as f:
        musicnftbuyer_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=musicnftbuyer_abi
    )

    return contract
    
contract = load_contract()

################################################################################
# Display Available NFTs
################################################################################
st.title("BeatBlocks - Music NFT Marketplace")

st.title("Fan Portal")

st.markdown("Available Audio NFTs")
accounts = w3.eth.accounts

# Use a streamlit component to get the address of the audio owner from the user
address = st.selectbox("Select Audio Owner", options=accounts)

audio_hashes=['https://gateway.pinata.cloud/ipfs/QmbbaGdg8sPTyE7XVQ93kiNpHJx4ZqEbFP3gLdebyAQ7ip']
# get the full list of tokens and filter by where owner is artist.

token_id = st.selectbox("Audio Tokens", (audio_hashes))

if st.button("Display"):

    nft_address = contract.functions.ownerOf(token_id).call()

    # Get a list of tokens available for sale
    token_uri = contract.functions.tokenURI(token_id).call()

    # Use a streamlit component to get the list of tokens available 
    address = st.selectbox("Select Audio", options=audio_hashes)

    token_metadata = contract.functions.contractURI().call()
    st.markdown(f'This token includes:{token_metadata}')

################################################################################
# Purchase a Token
################################################################################
if st.button("Purchase NFT"):

    # Use the contract to purchase an NFT 
    tx_hash = contract.functions.transfer(
        address,
        token_uri,
    ).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt Mined:")
    st.write(dict(receipt))
    
    st.write(f'Congrats! You just bought the BeatBlocks Ultimate VIP Experience!') 
    # {token.functions.getType()}') 

st.markdown("---")