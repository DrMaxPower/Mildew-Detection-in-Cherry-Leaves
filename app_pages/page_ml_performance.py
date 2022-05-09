import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation

from tensorflow import keras

def page_ml_performance_metrics():
    version = 'v1'

    st.write("### Train, Validation and Test Set: Labels Frequencies")

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")


    st.write("### Model History")
    col1, col2 = st.beta_columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Traninig Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Traninig Losses')
    st.write("---")
    if st.checkbox('Model: "sequential"'): 
      st.write(
        f"_________________________________________________________________\n"
        f"Layer (type)                 Output Shape              Param #   \n"
        f"=================================================================\n"
        f"conv2d (Conv2D)              (None, 254, 254, 24)      672       \n"
        f"_________________________________________________________________\n"
        f"max_pooling2d (MaxPooling2D) (None, 127, 127, 24)      0         \n"
        f"_________________________________________________________________\n"
        f"conv2d_1 (Conv2D)            (None, 125, 125, 12)      2604      \n"
        f"_________________________________________________________________\n"
        f"max_pooling2d_1 (MaxPooling2 (None, 62, 62, 12)        0         \n"
        f"_________________________________________________________________\n"
        f"conv2d_2 (Conv2D)            (None, 60, 60, 8)         872       \n"
        f"_________________________________________________________________\n"
        f"max_pooling2d_2 (MaxPooling2 (None, 30, 30, 8)         0         \n"
        f"_________________________________________________________________\n"
        f"conv2d_3 (Conv2D)            (None, 28, 28, 6)         438       \n"
        f"_________________________________________________________________\n"
        f"max_pooling2d_3 (MaxPooling2 (None, 14, 14, 6)         0         \n"
        f"_________________________________________________________________\n"
        f"flatten (Flatten)            (None, 1176)              0         \n"
        f"_________________________________________________________________\n"
        f"dense (Dense)                (None, 128)               150656    \n"
        f"_________________________________________________________________\n"
        f"dropout (Dropout)            (None, 128)               0         \n"
        f"_________________________________________________________________\n"
        f"dense_1 (Dense)              (None, 1)                 129       \n"
        f"=================================================================\n"
        f"Total params: 155,371\n"
        f"Trainable params: 155,371\n"
        f"Non-trainable params: 0\n"
        f"_________________________________________________________________\n"
        )


    st.write("### Generalised Performance on Test Set")
    st.dataframe(pd.DataFrame(load_test_evaluation(version), index=['Loss', 'Accuracy']))