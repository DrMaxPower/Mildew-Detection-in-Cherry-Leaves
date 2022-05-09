import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**General Information**\n"
        f"This is an ML system that is capable of detecting mildew infection of a tree leaf image.\n"
        f"It can instantly differ between healthy leaf or that has powdery mildew." 
        f"A similar manual process is in place for other crops for detecting pests at Marianne McGuineys "
        f"The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops." 
        )
    if st.button("More Info About Farm & Foods"):
        st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/DrMaxPower/Mildew-Detection-in-Cherry-Leaves/blob/main/README.md).")
        
        
        



    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* The client is interested in predicting if a cherry tree is healthy or contains powdery mildew."
        )
    if st.button("Some about success"):
        st.write("More Info About Farm & Foods")