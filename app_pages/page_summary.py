import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("\n")

    st.info(
        f" ### General Informatio \n"
        "**This webstie** has an built in machine learning system that is capable of detecting mildew infection of a cherry leaf image. "
        f"It can instantly differ between healthy leaf or ones that has powdery mildew. " 
        f"Click the *Mildew Detection* (box 3) in the sidebar to uppload you image.\n"
        f"But before you do, have a look at the Image Montage in the (box 2) *Leaves Visualizer* of how images **is optimized**." 
        )


    if st.button("More Info"):

        st.write(
            "**At** Farm & Foods we are proved to deliver high quality products and even if our lives and the enviroment change we "
            "strongly belive poeple like our products just the way they are both in taste and in price. Therefor have I "
            "asked Marianne McGuineys and here team to get in the frontline of future technology. \n"
            "All and all we whant our workes to minimize tedious and repetitive work and maximize planes of world domination. "
            "Best regars Dr Max Power \n"
            "*head and CEO* of **Farm & Foods**"       
        )

                
    st.write("---")


    st.success(
        f" ### Requirements and Quality\n"
        f"**Our** goal was to be at over ±2 standard deviations from the mean "
        f"and we are proude to informe you that we are well above *97%* range and therfore exided our accuracy **goal**. "    
        )


    if st.button("Info"):

        st.write(
            f"* You can find extra information about business requiraments and stastical information in *Project Hypothesis* \n"
            f"* You can find extra information about Machine Learning and Convolutional Neurak Network in *Project Performance*"
            )

        st.warning(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/DrMaxPower/Mildew-Detection-in-Cherry-Leaves/blob/main/README.md)."
        )