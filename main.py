import joblib
import pandas as pd
import streamlit as st

iris=['setosa', 'versicolor', 'virginica']

st.write("""
# Iris prediction app
""")

st.sidebar.header('User Input')

def user_input_features():
    sepal_length=st.sidebar.slider('Sepal Length cm',min_value=4.3,max_value=7.9,value=5.8)
    sepal_width=st.sidebar.slider('Sepal Width cm',min_value=2.0,max_value=4.4,value=3.05)
    petal_length=st.sidebar.slider('Petal Length',min_value=1.0,max_value=6.9,value=3.75)
    petal_width=st.sidebar.slider('Petal Width cm',min_value=0.1,max_value=2.5,value=1.19)
    
    data={'sepal length (cm)':sepal_length,
         'sepal width (cm)':sepal_width,
         'petal length (cm)':petal_length,
         'petal width (cm)':petal_width}
    
    df=pd.DataFrame(data,index=[0])
    
    return df

df=user_input_features()
st.subheader('User Input (Dataframe)')
st.write('Alter the parameters in the sidebar and based on your input app will return predictions')
st.write(df)

st.subheader('Class labels and their corresponding index')
st.write(pd.DataFrame(iris,columns=['flowers']))

model=joblib.load('random_forest_classifier.joblib')

st.subheader('Prediction')
st.write(iris[model.predict(df)[0]])