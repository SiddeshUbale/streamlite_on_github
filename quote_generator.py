import streamlit as st
import random

# Sample quotes (you can add more)
quotes = [
    "The only way to do great work is to love what you do.",
    "In the middle of difficulty lies opportunity.",
    "It is better to be alone than in bad company.",
    "The future belongs to those who believe in the beauty of their dreams."
]

def generate_quote():
  return random.choice(quotes)

st.title("Random Quote Generator")
st.write("Need some inspiration? Click the button below!")

if st.button("Generate Quote"):
  quote = generate_quote()
  st.success(quote)
