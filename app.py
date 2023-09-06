import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
st.title("Smhyal")
st.subheader('Supporting Mental Health via. AI Learning')
st.markdown("""Supporting Mental Health in Youth via. AI Learning, or Smhyal, is an all-in-one tool for simple self-diagnosis for two of the most common, yet critical, psychological disorders among youth: anxiety and depression.
The Smhyal algorithm is based on a modified version of an artificial neural network (ANN), with an accuracy of more than 94% anxiety and depression diagnosis. The model was trained on the data for young adults from the publicly-available Substance Abuse and Mental Health Service Administration (SAMHSA) MH-CLD survey dataset. The algorithm was created by Avi Verma, under the guidance of Dr. Kaustubh Supekar at Stanford University. We hope that Smyhal will positively impact young adults by counteracting the underdiagnosis of anxiety and depression.
""")
st.write('None of the data entered in the form or the diagnosis outputs are ever stored or traced.')
st.sidebar.success('Select the pages')
