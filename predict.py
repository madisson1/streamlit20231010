import streamlit as st
import pickle
import pandas as pd



st.header('Melbourne Housing price prediction calculator')
st.write('Predict housing price based on "Rooms", "Distance", "Bedroom2", "Bathroom", "Car", "Landsize"')


# room number slider
x1 = st.slider('Rooms', min_value=1, max_value=100, value=3)

# distance number slider

x2 = st.slider('Distance', min_value=1.0, max_value=100.0,  value=3.0)

# bedroom number slider

x3 = st.slider('Bedroom2', min_value=1, max_value=100, value=3)

# bathroom number slider

x4 = st.slider('Bathroom', min_value=1, max_value=100, value=3)

# car numbere slider

x5 = st.slider('Car', min_value=1, max_value=100, value=3)

# landsize number slider

x6 = st.slider('Landsize', min_value=1, max_value=100, value=3)

with open("modelfolder/model.pkl", "rb") as model_file:
          loaded_model = pickle.load(model_file)
        
        
data_dict = {
    "Rooms" : x1,
    "Distance" : x2,
    "Bedroom2" : x3,
    "Bathroom" : x4,
    "Car" : x5,
    "Landsize" : x6    
}
          
X_test = pd.DataFrame([data_dict])          
y_pred = loaded_model.predict(X_test)


if st.button( "Price prediction"):
    #if the button is clicked then write "THE PRICE IS"
    st.write("THE PRICE IS", y_pred)
    
    
    