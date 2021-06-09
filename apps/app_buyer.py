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
        with open(Path('apps/musicnftbuyer_abi.json')) as f:
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

    st.title("Purchase Portal")

    accounts = w3.eth.accounts

    buyer_address = st.selectbox("Buyer", options=accounts)

    # Use a streamlit component to get the address of the audio owner from the user
    seller_address = st.selectbox("Seller/Artist ", options=accounts)

    tokens = contract.functions.balanceOf(seller_address).call()

    # get the full list of tokens and filter by where owner is artist.
    token_id = st.selectbox("Available Tokens", list(range(tokens)))

    st.write("Token Price: 0.01 eth")

    ################################################################################
    # Purchase a Token
    ################################################################################
    if st.button("Purchase NFT"):

        token_uri = contract.functions.tokenURI(token_id).call()

        tx_hash = contract.functions.registerAudio(
            buyer_address,
            token_uri
        ).transact({'from': seller_address, 'gas': 1000000})
        receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        st.write("Congratulations! Your purchase is complete!")
        st.balloons()

    st.markdown("---")

    ################################################################################
    # Display a Token
    ################################################################################
    st.markdown("## Display Your Audio NFT's")

    selected_buyer_address = st.selectbox("Select Account", options=accounts)

    buyer_tokens = contract.functions.balanceOf(selected_buyer_address).call()

    st.write(f"This address owns {buyer_tokens} tokens")

    buyer_token_id = st.selectbox("Show Tokens", list(range(buyer_tokens)))

    if st.button("Display", key="4"):
        token_uri = contract.functions.tokenURI(buyer_token_id).call()
        st.write(f"Access your recently purchased NFT below: {token_uri}")
        token_metadata = contract.functions.contractURI().call()
        st.write("## The BeatBlocks VIP Experience includes the following access:")
        st.write("* Lifetime Backstage Passes")
        st.write("* Lifetime Front Row Concert Tickets")
        st.write("* Lifetime Virtual Concert Tickets")
        st.write("* Lifetime Artist Membership - Allows you to hear samples of the songs before they’re released")
        st.write("* Remix & Royalties - When a song reaches our set popularity count, a remix version of the song is released, and NFT owners receive lifetime royalties for that song")
        st.write("* Artist-to-Artist Access - Your favorite artist will send his team to work with you for a day on one of your songs/projects")
        st.write("* Digital Album")
        st.write("* Physical Album")
        st.write("* New artist merchandise every 6 months")