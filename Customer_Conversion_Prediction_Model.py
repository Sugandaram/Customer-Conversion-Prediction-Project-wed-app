import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

customer_conversion_prediction_model = pickle.load(open('F:/IDM\Video/Guvi_DTM_Videos/Kousik Krishna/Final_Projects_Kousik Krishnan/customer_conversion_prediction_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Customer Conversion Prediction System',
                          
                          ['Customer Conversion Prediction'],
                           
                          icons=['person'],
                           
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Customer Conversion Prediction'):
    
    # page title
    st.title('Customer Conversion Prediction')
    
    
    # getting the input data from the user
    #col1, col2, col3 = st.columns(3)
    age = st.text_input('Age of the Customer')
    job = st.text_input('Job of the customer - management = 0, technician = 1, entrepreneur = 2, blue-collar= 3,retired = 4, admin = 5, services = 6, self-employed = 7,unemployed = 8,housemaid = 9, student = 10')
    marital = st.text_input('Marital of the customer - married = 0, single = 1, divorced = 2')
    education_qual = st.text_input('Education and quality of the customer - tertiary = 0, secondary = 1, primary = 3')
    call_type = st.text_input('Call types of the customer - cellular = 1, telephone = 0')
    day = st.text_input('Menson the day - 1 to 31')
    mon = st.text_input('Menson the month - may = 5, jun =  6, jul = 7, aug = 8, oct = 10, nov = 11, dec = 12, jan = 1, feb = 2,mar = 3, apr = 4, sep = 9')
    dur = st.text_input('Call duration')
    num_calls = st.text_input('Number of calls')
    prev_outcome = st.text_input('The previous outcome of the customer - unknown = 1, failure = 2, other = 3, success = 4')                      
    
    
    # code for Prediction
    Customer_Conversion_Prediction = ''
    
    # creating a button for Prediction
    
    if st.button('Customer Conversion Prediction Result'):
        customer_conversion_prediction = customer_conversion_prediction_model.predict([[age,job,marital,education_qual, call_type,day,mon,dur,num_calls,prev_outcome]])
        
        if (customer_conversion_prediction[0] == 1):
          Customer_Conversion_Prediction = 'The person subscribes to the insurance.'
        else:
          Customer_Conversion_Prediction = 'The person does not subscribe to the insurance.'
        
    st.success(Customer_Conversion_Prediction)
