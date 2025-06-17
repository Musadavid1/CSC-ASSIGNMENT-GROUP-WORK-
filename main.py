# main.py

import streamlit as st
from app.homepage import show_homepage

def main():
    st.set_page_config(page_title="Bank App", layout="centered")
    show_homepage()

if __name__ == "__main__":
    main()
