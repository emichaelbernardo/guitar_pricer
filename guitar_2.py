import math
import pickle
import sklearn
import streamlit as st
import boto3
import boto3.session
from PIL import Image
import configparser
 
# loading the trained model from local drive
#with open('models/guitar_test.pkl', 'rb') as f:
#    model = pickle.load(f)
    

## loading the trained model from AWS S3 

config = configparser.ConfigParser()
config.read('aws.ini')
    
AWS_key_id     = config['aws']['aws_access_key_id']
AWS_secret_key = config['aws']['aws_secret_access_key']   
    

# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id = AWS_key_id,
    aws_secret_access_key =  AWS_secret_key,
    region_name = 'us-east-1'
)
response = client.get_object(Bucket='dataforguitarapp', Key='guitar_test.pkl')
body = response['Body'].read()
model = pickle.loads(body)    

@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(cond_score, type_code, price_range):   
 
    # Making predictions 
    prediction = model.predict( 
        [[cond_score, type_code, price_range]])
     
    return prediction

def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-image: url("bg.png");
    background-size: cover;"> 
    
    <h1 style ="color:black;text-align:center;">Guitar Price Prediction ML App</h1> 
    </div> 
    """
    # def img_to_bytes(img_path):
    #img_bytes = Path(bg.png).read_bytes()
    #encoded = base64.b64encode(img_bytes).decode()
    #return encoded
    img = Image.open("bg.png")
    st.image(img)

    
    
    
    # display the front end aspect
    #st.markdown(html_temp, unsafe_allow_html = True) 
    
    #header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(encoded)
     
    
    #header_html = "<img src='bg.png'>"
    
    #st.markdown(
    #    header_html, unsafe_allow_html=True,
    #)    
    
    #def format_func(box,choice_dict):
    #        return choice_dict[box]

   

    
    
    conditions = { 
        6: "Mint",
        5: "Excellent",
        4: "Very Good",
        3: "Good",
        2: "Fair",
        1: "Poor"
        }   

    cond_score = st.selectbox(
        label="the Condition of guitar:",
        options= (6,5, 4, 3, 2, 1), 
        format_func=lambda x: conditions.get(x),
        )   
    
    types = { 
        1: "Solid Body",
        2: "Semi-Hollow",
        3: "Hollow Body",
        4: "Other"
        
        }   

    type_code = st.selectbox(
        label="Body type of guitar:",
        options= (1,2,3,4), 
        format_func=lambda x: types.get(x),
        )  
   


    price_dict = {#2: "Not Sure.",
                  2: "less than 500",
                  3: "less than 1000",
                  4: "less than 1500",
                  5: "less than 2500" }
    
    price_range = st.selectbox(
        label="How much was it originally:",
        options= (5, 4, 3, 2), 
        format_func=lambda x: price_dict.get(x),
        )       
    
    #price_range = st.selectbox(
    #'How much did you pay for it?',(1, 2, 3, 4, 5, 6))
    #,  
    #options=list(price_dict.keys(), format_func=format_func(price_range,price_dict))
    
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(cond_score, type_code, price_range)
        price = "{:.2f}".format(result[0])
        
        #st.write('Guitar value is $',price)
        st.success('Guitar value is ${}'.format(price))
        
        
if __name__=='__main__': 
    main()        