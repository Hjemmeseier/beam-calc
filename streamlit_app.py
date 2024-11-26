import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# App Title
st.title("Simple Supported Beam Analysis")

# Inputs
length = st.number_input("Length of Beam (m):", min_value=0.01, value=5.00, step=0.01, format="%.2f")
uniform_load = st.number_input("Uniform Load (kN/m):", min_value=0.01, value=10.00, step=0.01, format="%.2f")

if st.button("Calculate"):
    # Reactions
    reaction = (uniform_load * length) / 2
    st.subheader("Reactions")
    st.write(f"Reaction at Support A: {reaction:.2f} kN")
    st.write(f"Reaction at Support B: {reaction:.2f} kN")
    
    # Shear Force Diagram
    x = np.linspace(0, length, 1000)
    shear_force = reaction - uniform_load * x

    # Moment Diagram
    bending_moment = reaction * x - (uniform_load * x**2) / 2

    # Plot Shear Force Diagram
    st.subheader("Shear Force Diagram")
    fig1, ax1 = plt.subplots()
    ax1.plot(x, shear_force, label="Shear Force (kN)", color="blue")
    ax1.axhline(0, color="black", linewidth=0.8)
    ax1.set_xlabel("Position along Beam (m)")
    ax1.set_ylabel("Shear Force (kN)")
    ax1.set_title("Shear Force Diagram")
    ax1.legend()
    ax1.grid()
    st.pyplot(fig1)