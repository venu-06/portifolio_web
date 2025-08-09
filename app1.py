import streamlit as st

# Read your portfolio HTML file
with open("portfolio.html", "r", encoding="utf-8") as f:
    portfolio_html = f.read()

# Display HTML inside Streamlit
st.components.v1.html(portfolio_html, height=3000, scrolling=True)
