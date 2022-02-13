%%writefile app.py
 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('models/guitar.pkl', 'rb') 
model = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(cond_score, type_code, price_range):   
 
    # Pre-processing user input    
    #if Gender == "Male":
    #    Gender = 0
    #else:
    #    Gender = 1
 
    #if Married == "Unmarried":
    #    Married = 0
    #else:
    #    Married = 1
 
    #if Credit_History == "Unclear Debts":
    #    Credit_History = 0
    #else:
    #    Credit_History = 1  
 
    #LoanAmount = LoanAmount / 1000
 
    # Making predictions 
    prediction = model.predict( 
        [[cond_score, type_code, price_range]])
     
    return prediction

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
    
    cond_score = st.selectbox(
     'condition?',(1, 2, 3, 4, 5, 6))

    type_code = st.selectbox(
     'type?',(1, 2, 3, 4, 5, 6))

    price_range = st.selectbox(
     'How much did you pay for it?',(1, 2, 3, 4, 5, 6))
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(cond_score, type_code, price_range) 
        st.success('value is  {}'.format(result))
        