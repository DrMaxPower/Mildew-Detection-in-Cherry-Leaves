import streamlit as st


def page_summary_body():

    st.write("\n")

    st.info(
        f" ### General Informatio \n"
        "**This website** has a built-in machine learning system that is capable of detecting mildew infection of a cherry leaf image. "
        f"It can instantly differ between healthy leaves or ones that have powdery mildew. " 
        f"Click the Mildew Detection (box 3) in the sidebar to upload your image. \n"
        f"But before you do, have a look at the Image Montage in the (box 2) *Leaves Visualizer* of how images **are optimized**." 
        )


                
    st.write("---")


    st.success(
        f" ### Requirements and Quality\n"
        f"**Our** goal was to be at over ±2 standard deviations from the mean "
        f"and we are proud to inform you that we are well above the *97%*  range and therefore exited our accuracy **goal**. "    
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