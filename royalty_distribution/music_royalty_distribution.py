
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

# A list of the nusci album:
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
st.markdown("# Music Royalty Income")
st.text(" \n")

################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## BeatBlocks Address")

##########################################
# Step 1 - Part 4:
# Create a variable named `account`. Set this variable equal to a call on the
# `generate_account` function. This function will create the Fintech Finder
# customer’s (in this case, your) HD wallet and Ethereum account.

# @TODO:
#  Call the `generate_account` function and save it as the variable `account`
# YOUR CODE HERE
account = generate_account()

##########################################

# Write the client's Ethereum account address to the sidebar
st.sidebar.write(account.address)

##########################################
# Step 1 - Part 5:
# Define a new `st.sidebar.write` function that will display the balance of the
# customer’s account. Inside this function, call the `get_balance` function and
#  pass it your Ethereum `account.address`.

# @TODO
# Call `get_balance` function and pass it your account address
# Write the returned ether balance to the sidebar
# YOUR CODE HERE
st.sidebar.write("Balance:", get_balance(account.address), " eth")
st.sidebar.text("______________________________________________")
st.sidebar.text(" \n")

##########################################

# Create a select box to chose a FinTech Hire candidate
person = st.sidebar.selectbox('Select an Album', albums)

# Create a input field to record the number of hours the candidate worked
total_streams = st.sidebar.number_input("Total Streams in Current Month")
st.sidebar.text("______________________________________________")
st.sidebar.text(" \n")

# Identify the FinTech Hire candidate
candidate = investors_database[person][0]

# Write the Fintech Finder candidate's name to the sidebar
st.sidebar.write("Album: ", candidate)

# Identify the FinTech Finder candidate's Ethereum Address
candidate_address = investors_database[person][1]

# Write the inTech Finder candidate's Ethereum Address to the sidebar
st.sidebar.write("Owner Address: ", candidate_address)

# Identify the FinTech Finder candidate's hourly rate
rate_per_thousand= investors_database[person][3]

# Write the inTech Finder candidate's hourly rate to the sidebar
st.sidebar.write("Rate per 1,000 streams: ", rate_per_thousand)


latest_royalty_distribution = investors_database[person][3] * total_streams / 1000
st.sidebar.write("Latest Royalty Distribution:", latest_royalty_distribution, " eth")

st.sidebar.text("______________________________________________")
st.sidebar.text(" \n")

##########################################
# Step 2 - Part 2:
# * Call the `send_transaction` function and pass it three parameters:
    # - Your Ethereum `account` information. (Remember that this `account`
    # instance was created when the `generate_account` function was called.)
    #  From the `account` instance, the application will be able to access the
    #  `account.address` information that is needed to populate the `from` data
    # attribute in the raw transaction.
    #- The `candidate_address` (which will be created and identified in the
    # sidebar when a customer selects a candidate). This will populate the `to`
    # data attribute in the raw transaction.
    # - The `wage` value. This will be passed to the `toWei` function to
    # determine the wei value of the payment in the raw transaction.

# * Save the transaction hash that the `send_transaction` function returns as a
# variable named `transaction_hash`, and have it display on the application’s
# web interface.


if st.sidebar.button("Send Transaction"):

    # @TODO
    # Call the `send_transaction` function and pass it 3 parameters:
    # Your `account`, the `candidate_address`, and the `wage` as parameters
    # Save the returned transaction hash as a variable named `transaction_hash`
    # YOUR CODE HERE
    transaction_hash = send_transaction(account, candidate_address, latest_royalty_distribution)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

# The function that starts the Streamlit application
# Writes FinTech Finder candidates to the Streamlit page
get_albums()
