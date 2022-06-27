import streamlit as st


rawText = st.text_area("Enter Stock Symbols")
result = ""
if rawText:
    for symbol in rawText.split("\n"):
        result += symbol + " "

    st.write(result)