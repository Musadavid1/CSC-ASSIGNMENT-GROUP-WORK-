# app/homepage.py

import streamlit as st
from core.bank import Bank

bank = Bank("Streamlit Bank")

def show_homepage():
    st.title("🏦 Streamlit Bank App")
    st.subheader("Welcome to Your Personal Banking Dashboard")

    user = st.text_input("Enter your name")
    account_type = st.selectbox("Select Account Type", ["Savings", "Current"])

    st.write("---")

    if st.button("Create Account"):
        balance = st.number_input("Initial Deposit", min_value=0)
        st.success(bank.create_account(user, account_type, balance))

    st.write("---")

    deposit_amt = st.number_input("Deposit Amount", min_value=0, key="dep")
    if st.button("Deposit"):
        st.success(bank.deposit(user, account_type, deposit_amt))

    withdraw_amt = st.number_input("Withdraw Amount", min_value=0, key="wd")
    if st.button("Withdraw"):
        st.success(bank.withdraw(user, account_type, withdraw_amt))

    if st.button("Check Balance"):
        st.info(f"Balance: ${bank.get_balance(user, account_type)}")
