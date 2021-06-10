
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from crypto_wallet import generate_account, get_balance, send_transaction

investors_database = {
    "Ryman": ["Ryman", "0xaC8eB8B2ed5C4a0fC41a84Ee4950F417f67029F0", 5.654, .002, "Images/album1.jpg"],
    "Sound Wave": ["Sound Wave", "0x2422858F9C4480c2724A309D58Ffd7Ac8bF65396", 3.254, .001, "Images/album2.jpg"],
    "Shameless": ["Shameless", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", 9.345, .002, "Images/album3.jpg"],
    "Back to Paradise": ["Back to Paradise", "0x8fD00f170FDf3772C5ebdCD90bF257316c69BA45", 6.458, .002, "Images/album4.jpg"]
}

# A list of the music album:
albums = ["Ryman", "Sound Wave", "Shameless", "Back to Paradise"]


def get_albums():
    """Display the database of Fintech Finders candidate information."""
    db_list = list(investors_database.values())

    for number in range(len(albums)):
        st.image(db_list[number][4], width=200)
        st.write("Album: ", db_list[number][0])
        st.write("Owner Address: ", db_list[number][1])
        st.write("Last 12 Months' Royalties: ", db_list[number][2], " eth")
        st.write("Rate per 1,000 streams : ", db_list[number][3], " eth")
        st.text(" \n")

################################################################################
# Streamlit Code

# Streamlit application headings
st.markdown("# Music Royalty Distribution")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## BeatBlocks Address")

##########################################
# Create a variable named `account`. Set this variable equal to a call on the

account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

#########################################


# Call `get_balance` function and pass it your account address
st.sidebar.write("Balance:", get_balance(account.address), " eth")
st.sidebar.text("______________________________________________")
st.sidebar.text(" \n")

##########################################

# Create a select box to chose a album
person = st.sidebar.selectbox('Select an Album', albums)

# Create a input field to record the total streams in current month
total_streams = st.sidebar.number_input("Total Streams in Current Month")
st.sidebar.text("______________________________________________")
st.sidebar.text(" \n")

# Identify the investor
candidate = investors_database[person][0]

# Write the album name
st.sidebar.write("Album: ", candidate)

# Identify the investor's Ethereum Address
candidate_address = investors_database[person][1]

# Write the iinvestor's Ethereum Address to the sidebar
st.sidebar.write("Owner Address: ", candidate_address)

# Identify the investor's streaming rate
rate_per_thousand= investors_database[person][3]

# Write the investors's streaming rate to the sidebar
st.sidebar.write("Rate per 1,000 streams: ", rate_per_thousand)


latest_royalty_distribution = investors_database[person][3] * total_streams / 1000
st.sidebar.write("Latest Royalty Distribution:", latest_royalty_distribution, " eth")

st.sidebar.text("______________________________________________")
st.sidebar.text(" \n")

##########################################
# Step 2 - Part 2:

if st.sidebar.button("Send Transaction"):


    # Call the `send_transaction` function and pass it 3 parameters:
    transaction_hash = send_transaction(account, candidate_address, latest_royalty_distribution)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
get_albums()
