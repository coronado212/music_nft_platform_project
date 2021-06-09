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

def app():
    @st.cache(allow_output_mutation=True)
    def load_contract():

        # Load the contract ABI
        with open(Path('apps/musicnftartist_abi.json')) as f:
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
    st.title("BeatBlocks - Music NFT Marketplace")

    st.title("Artist Portal")

    st.markdown("## Mint Your Audio NFT")
    accounts = w3.eth.accounts

    # Use a streamlit component to get the address of the audio owner from the user
    address = st.selectbox("Select Audio Owner", options=accounts)

    # Use a streamlit component to get the audio's URI
    audio_uri = st.text_input("Input Audio URI")

    if st.button("Mint Audio NFT"):

        # Use the contract to send a transaction to the registerAudio function
        tx_hash = contract.functions.registerAudio(
            address,
            audio_uri
        ).transact({'from': address, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write("Token minted.")
        st.balloons()

    st.markdown("---")

    ################################################################################
    # Display a Token
    ################################################################################
    st.markdown("## Display Your Audio NFT's")

    selected_address = st.selectbox("Select Account", options=accounts, key="3")

    tokens = contract.functions.balanceOf(selected_address).call()

    st.write(f"This address owns {tokens} tokens")

    token_id = st.selectbox("Audio Tokens", list(range(tokens)))

    if st.button("Display"):

        # Use the contract's `ownerOf` function to get the audio token owner
        owner = contract.functions.ownerOf(token_id).call()

        st.write(f"The token is registered to {owner}")

        # Use the contract's `tokenURI` function to get the audio token's URI
        token_uri = contract.functions.tokenURI(token_id).call()

        st.write(f"The tokenURI is {token_uri}")

        # Use the contract's 'contractURI' function to get the token metadata 
        token_metadata = contract.functions.contractURI().call()

        st.write(f"Congrats! This token includes the following access: {token_metadata}")
        