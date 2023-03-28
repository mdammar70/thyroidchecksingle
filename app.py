import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
def thyroid_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
        return 'You are free from thyroid disease'
    else:
      return 'you have thyroid disease'
def main():
    # giving a title
    st.title('Thyroid Prediction Web App')

    TSH = st.text_input('TSH VALUE : Thyroid-Stimulating Hormone')
    TT4 = st.text_input('TT4 VALUE : Total thyroxine')
    T4U = st.text_input('T4U  VALUE: Thyroxine ')
    FTI= st.text_input('FTI : Free thyroxine index')
    diab_diagnosis = ''  
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Thyroid Test Result'):
        diagnosis = thyroid_prediction([TSH,TT4,T4U,FTI])
        
        
    st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()