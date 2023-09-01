import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np

#importing models
mod1 = load_model('depression.h5')
mod2 = load_model('anxiety.h5')
li = [0]*9
#taking inputs
with st.expander("Age(ranges and values"):
  st.markdown("""
- 12-14 years → 2
- 15-17 years → 3
- 18-20 years → 4
- 21-24 years → 5""")
li[0]=st.number_input('Age',min_value=0)
with st.expander("Education(ranges and values"):
  st.markdown("""
- Special education → 1
- 6th grade to 8th grade → 2
- 9th grade to 11th grade → 3
- 12th grade (or pursuing GED) → 4""")
li[1] = st.number_input('Education',min_value=0)
li[2] = st.number_input('Ethnic',min_value=0)
li[3] = st.number_input('Race',min_value=0)
li[4] = st.number_input('Gender',min_value=0)
li[5] = st.number_input('Marital',min_value=0)
li[6] = st.number_input('SED',min_value=0)
li[7] = st.number_input('Employment',min_value=0)
li[8] = st.number_input('Residential',min_value=0)

def predict_mh(new_x_example):
  new_example_reshaped = np.asarray(li).reshape((1, 9))
  my_new_prediction = mod1.predict(new_example_reshaped)
  print(my_new_prediction)
  depression = -1
  if (my_new_prediction.flatten()[0] > 0.4):
    depression = 1
  else:
    depression = 0

  my_new_prediction_a = mod2.predict(new_example_reshaped)
  print(my_new_prediction_a.flatten()[0])
  anxiety = -1
  if (my_new_prediction_a.flatten()[0] > 0.4):
    anxiety = 1
  else:
    anxiety = 0

  prediction_dict = {'Depression':depression, "Anxiety":anxiety}
  return prediction_dict

bt = st.button('My Result')
if bt:
  st.write(predict_mh(li))
