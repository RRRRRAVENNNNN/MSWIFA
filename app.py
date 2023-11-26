import streamlit as st
from joblib import load
import numpy as np

model = load('model/ML_model.joblib')
scaler = load('model/StandardScaler.joblib')

st.title('GB model for predicting heavy metal immobilization rate in MSWIFA by geopolymers')

col1, col2 = st.columns(2)

with col1:
    feature1 = st.number_input(u'$\mathrm{n(SiO_2)/n(Al_2O_3)}$', step=0.0001, format='%.4f')
    feature2 = st.number_input(u'$\mathrm{n(SiO_2)/n(CaO)}$', step=0.0001, format='%.4f')
    feature3 = st.number_input(u'$\mathrm{Fe_2O_3\;(\%)}$', step=0.0001, format='%.4f')
    feature4 = st.number_input(u'$\mathrm{Na_2O\;(\%)}$', step=0.0001, format='%.4f')
    feature5 = st.number_input(u'$\mathrm{temperature\;(℃)}$', step=0.0001, format='%.4f')
    feature6 = st.number_input(u'$\mathrm{curing\;time\;(d)}$', step=0.0001, format='%.4f')
with col2:
    feature7 = st.number_input(u'$\mathrm{liquid/solid}$', step=0.0001, format='%.4f')
    feature8 = st.number_input(u'$\mathrm{alkali\;equivalent\;(\%)}$', step=0.0001, format='%.4f')
    feature9 = st.number_input(u'$\mathrm{activator\;modulus}$', step=0.0001, format='%.4f')
    feature10 = st.number_input(u'$\mathrm{heavy\;metal\;valence}$', step=0.0001, format='%.4f')
    feature11 = st.number_input(u'$\mathrm{initial\;concentratio\;(mg/L)}$', step=0.0001, format='%.4f')
    feature12 = st.number_input(u'$\mathrm{heavy\;metal\;electronegativity}$', step=0.0001, format='%.4f')
feature13 = st.number_input(u'$\mathrm{radius\;of\;hydrated\;heavy\;metal\;ions\;(Å)}$', step=0.0001, format='%.4f')
feature = st.number_input(u'$\mathrm{Experimental\;heavy\;metal\;immobilization\;rate\;(\%)}$', step=0.0001, format='%.4f')

feature_values = [feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13]


if st.button('Predict'):
    input_data = np.array([feature_values])
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    error = abs(float(prediction) - feature)
    st.success(f'Predicted heavy metal immobilization rate: {prediction[0]:.2f}%')
    if feature != 0:
        st.success(f'Error: {Residual:.2f}%')
    
