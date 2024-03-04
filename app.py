import streamlit
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

model= ['Maruti Suzuki Swift', 'Tata Indigo eCS', 'Mahindra KUV100 K8',
       'Ford EcoSport Trend', 'Hyundai Verna Fluidic', 'Renault Kwid RXT',
       'Volkswagen Polo Highline1.2L', 'Honda City ZX',
       'Maruti Suzuki Maruti', 'Mahindra Jeep MM', 'Tata Zest XM',
       'Mahindra Scorpio Vlx', 'Hyundai Creta 1.6', 'Hyundai Santro Xing',
       'Ford EcoSport Titanium', 'Chevrolet Enjoy 1.4',
       'Maruti Suzuki Alto', 'Toyota Corolla Altis', 'Mahindra Quanto C8',
       'Renault Duster 110', 'Mahindra Logan Diesel',
       'Volkswagen Vento Konekt', 'Tata Zest XE', 'Renault Duster RxL',
       'Hyundai Elite i20', 'Mercedes Benz A', 'Ford EcoSport Ambiente',
       'Honda City', 'Hyundai Fluidic Verna', 'Maruti Suzuki Omni',
       'Audi Q5 2.0', 'Honda Brio VX', 'Volkswagen Jetta Comfortline',
       'Maruti Suzuki Ciaz', 'Mini Cooper S', 'Maruti Suzuki Ritz',
       'Volkswagen Polo', 'Chevrolet Beat LT', 'Maruti Suzuki Wagon',
       'Tata Sumo Grande', 'Hyundai Accent GLE', 'Mahindra Scorpio VLX',
       'Maruti Suzuki Esteem', 'Hyundai i10 Magna', 'Mahindra Scorpio',
       'Mitsubishi Pajero Sport', 'Hyundai i20 Magna', 'Tata Indigo LS',
       'Maruti Suzuki Stingray', 'Skoda Fabia 1.2L', 'Mahindra XUV500',
       'Honda Amaze', 'Chevrolet Beat', 'Honda City 1.5',
       'Maruti Suzuki Ertiga', 'Skoda Fabia Classic',
       'Hindustan Motors Ambassador', 'Tata Indigo LX',
       'Chevrolet Sail 1.2', 'Maruti Suzuki Zen', 'Renault Duster',
       'Mahindra Scorpio S4', 'Mahindra Xylo E8', 'Hyundai Santro',
       'Mahindra TUV300 T4', 'Honda Jazz VX', 'Chevrolet Beat LS',
       'Tata Indigo CS', 'Hyundai Grand i10', 'Hyundai i20 Sportz',
       'Hyundai i10', 'Toyota Corolla H2', 'Renault Duster 85PS',
       'Hyundai Verna 1.6', 'Honda City SV', 'Hyundai i20 Asta',
       'Hyundai Getz GLE', 'Mahindra Bolero Power', 'Toyota Etios Liva',
       'Renault Duster 85', 'Skoda Superb 1.8', 'Chevrolet Spark',
       'Hyundai i10 Sportz', 'Renault Lodgy 85', 'Chevrolet Tavera Neo',
       'Audi Q3 2.0', 'Renault Kwid', 'Force Motors Force',
       'Tata Aria Pleasure', 'Mahindra Scorpio S10', 'Datsun GO T',
       'Toyota Fortuner', 'Ford EcoSport', 'BMW 5 Series',
       'Mahindra Bolero SLE', 'Nissan Micra XV', 'Maruti Suzuki Dzire',
       'Mahindra Scorpio SLE']

company = ['Maruti', 'Tata', 'Mahindra', 'Ford', 'Hyundai', 'Renault',
       'Volkswagen', 'Honda', 'Chevrolet', 'Toyota', 'Mercedes', 'Audi',
       'Mini', 'Mitsubishi', 'Skoda', 'Hindustan', 'Force', 'Datsun',
       'BMW', 'Nissan']

fuel_type = ['Petrol', 'Diesel']




regressor = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
st.title('Car Price Prediction')


col1, col2= st.columns(2)

with col1:
    company = st.selectbox('Select the Company', company)
with col2:
    name = st.selectbox('Select the model', model)


col3, col4, col5 = st.columns(3)

with col3:
    year = st.number_input('Manufacturing Year')
with col4:
    kms_driven = st.number_input('Enter the Distance Driven')
with col5:
    fuel_type = st.selectbox('Fuel Type', fuel_type)


if st.button('predict probability'):
    input_df = pd.DataFrame({'name': [name],
                             'company': [company],
                             'year': [year],
                             'kms_driven': [kms_driven],
                             'fuel_type': [fuel_type]})

    result = regressor.predict(input_df)
    st.header("Predicted Price: " + str(result))