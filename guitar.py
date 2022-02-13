import streamlit as st
import numpy as np
import pandas as pd
import pickle

# load model
model = pickle.load(open('models/guitar.pkl','rb'))

def predict_age(condition,guitar_brand,guitar_model,guitar_origin,price_range):
    input=np.array([[condition,guitar_brand,guitar_model,guitar_origin,price_range]])
    prediction = model.predict(input)
    
    return int(prediction)

#st.title("Guitar Appraiser")
html_temp = """
<div style="background:#025246 ;padding:10px">
<h2 style="color:white;text-align:center;"> Guitar Price Predictor ML App </h2>
</div>
"""
st.markdown(html_temp, unsafe_allow_html = True)

condition = st.selectbox(
     'What is the condition of the guitar?',
     ('Mint', 'Excellent','Very Good','Good','Fair','Poor'))

brand = st.selectbox(
     'What is the brand of the guitar?',
('Ampeg',
 'Aria',
 'B.C. Rich',
 'B3',
 'BC Rich',
 'Burns',
 'Charvel',
 'Collings',
 'Cort',
 'Danelectro',
 'DeArmond',
 'Dean',
 'DiPinto',
 'Duesenberg',
 'ESP',
 'EVH',
 'Eastman',
 'Eastwood',
 'Electra',
 'Epiphone',
 'Ernie Ball Music Man',
 'Fano',
 'Fender',
 'Framus',
 'G&L',
 'Gibson',
 'Giffin',
 'Godin',
 'Gretsch',
 'Grosh',
 'Guild',
 'Hagstrom',
 'Hamer',
 'Harden Engineering',
 'Harley Benton',
 'Harmony',
 'Heritage',
 'Ibanez',
 'Jackson',
 'James Trussart',
 'Jerry Jones',
 'Kay',
 'Kramer',
 'Larrivee',
 'Line 6',
 'Martin',
 'Memphis',
 'Michael Kelly',
 'Mosrite',
 'Music Man',
 'Nash',
 'National',
 'Norma',
 'Other',
 'Ovation',
 'PRS',
 'Parker',
 'Peavey',
 'Reverend',
 'Rickenbacker',
 'Schecter',
 'Silvertone',
 'Squier',
 'Strandberg',
 'Suhr',
 'Supro',
 'Taylor',
 'The Loar',
 'Tokai',
 'Tom Anderson',
 'Vox',
 'Warmoth',
 'Washburn',
 'Woodrow',
 'Yamaha'))
guitar_model = st.selectbox(
     'What is the model of the guitar?',
('330',
 'AG Series',
 'AT Series',
 'AT100CL-SB',
 'AX Series',
 'AZ',
 'Boden',
 'Brad Paisley Esquire',
 'C-1',
 'C-7',
 'CST',
 'Casino',
 'Contender',
 'Coronado',
 'Cutlas',
 'Cyclone',
 'Diablo',
 'EC-1000',
 'ES-335',
 'ES-339',
 'Electromatic',
 'Falcon',
 'Fly',
 'G6129T',
 'GRX70QA',
 'H-1001',
 'HT7',
 'Horizon',
 'Jaguar',
 'Jazzmaster',
 'Joe Satriani',
 'Kirk Hammett Signature',
 'LG',
 'Les Paul',
 'Les Paul Classic',
 'Les Paul Custom',
 'Les Paul Junior',
 'Les Paul Special',
 'Les Paul Standard',
 'Les Paul Studio',
 'Les Paul Traditional',
 'Les Paul Tribute',
 'M-200',
 'M-I',
 'Mockingbird',
 'Mod Shop',
 'Mod Shop 50',
 'Monarkh',
 'Northender',
 'Omen',
 'Other',
 'PRS Custom 24',
 'Player Jaguar',
 'Player Jazzmaster',
 'Player Stratocaster',
 'Player Telecaster',
 'RG',
 'RG Series',
 'RX Series',
 'Reverse Explorer',
 'S-63',
 'S2',
 'SE',
 'SG',
 'SG Classic',
 'SG Junior',
 'SG Standard',
 'San Dimas Style 1',
 'Sheraton',
 'Sheraton II',
 'Silver Sky',
 'Snakebyte',
 'Soloist',
 'Special 22',
 'Stingray',
 'Stratocaster',
 'Streamliner',
 'Suhr Standard',
 'Sun Valley',
 'T486B',
 'TQM',
 'Telecaster',
 'V',
 'Valentine',
 'Wildkat',
 'Wolfgang Special',
 'Wood Library Custom 24',
 'X Series'))
guitar_origin = st.selectbox(
     'Country of Origin?',
('Asia', 'EU', 'United States', 'other'))

price_range = st.selectbox(
     'How much did you pay for it?',
(1, 2, 3, 4, 5, 6))


CHOICES = {1: "less than 300",
           2: "less than 500",
           3: "less than 1000",
           4: "less than 1500",
           5: "less than 2500" }
           


def format_func(price_range):
    return CHOICES[price_range]


price_range = st.selectbox("How much did you pay for it?", options=list(CHOICES.keys()), format_func=format_func)
#st.write(f"You selected option {option} called {format_func(option)}")





safe_html ="""  
<div style="background-color:#80ff80; padding:10px >
<h2 style="color:white;text-align:center;"> The Abalone is young</h2>
</div>
"""

def predict_class():
    data = list(map(float,[sepal_length,sepal_width,petal_length, petal_width]))
    result, probs = predict(data)
    st.write("The predicted class is ",result)  
