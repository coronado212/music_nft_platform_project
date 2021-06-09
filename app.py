import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats,app_artist,app_buyer # import app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Artist",app_artist.app)
app.add_app("Buyer",app_buyer.app)
# The main app
app.run()