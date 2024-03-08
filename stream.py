import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('classifier1.pkl', 'rb'))

st.title(' FERTILIZER RECOMMENDATION ')

st.write('Enter the values below to predict the crop:')

Nitrogen = st.number_input('Nitrogen')
Potassium = st.number_input('Potassium')
Phosphorous = st.number_input('Phosphorous')

if st.button('Predict'):
    # prediction
    result = model.predict(np.array([[Nitrogen, Potassium, Phosphorous]]))
    if result[0] == 0:
        result = 'TEN-TWENTY SIX-TWENTY SIX'
    elif result[0] == 1:
        result = 'Fourteen-Thirty Five-Fourteen'
    elif result[0] == 2:
        result = 'Seventeen-Seventeen-Seventeen'
    elif result[0] == 3:
        result = 'TWENTY-TWENTY'
    elif result[0] == 4:
        result = 'TWENTY EIGHT-TWENTY EIGHT'
    elif result[0] == 5:
        result = 'DAP'
    else:
        result = 'UREA'

    st.write('Recommmended Fertilizer :', result)
