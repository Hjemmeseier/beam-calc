import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("Simple Supported Beam Analysis")

# Inputs
length = st.number_input("Length of Beam (m):", min_value=0.01, value=5.00, step=0.01, format="%.2f")
uniform_load = st.number_input("Uniform Load (kN/m):", min_value=0.01, value=10.00, step=0.01, format="%.2f")

