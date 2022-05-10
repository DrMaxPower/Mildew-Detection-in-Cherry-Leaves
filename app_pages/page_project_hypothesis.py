import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    # Fix accuracy
    st.success(
        f"* This program can be used to with a high accuracy separate heathy leaves from leaves with mildew infect. \n"
        f"* The genneral accuracy rate is 0.9988"
    )

    