import mlflow
import pandas as pd
import streamlit as st


@st.cache_resource
def load_model():

    mlflow.set_tracking_uri("http://127.0.0.1:5000")

    return mlflow.pyfunc.load_model("models:/diamond_price_model/latest")


model = load_model()

st.title("Diamond Price Predictor")

carat = st.number_input("Carat", min_value=0.1, value=1.0)

cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])

color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])

clarity = st.selectbox(
    "Clarity", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

depth = st.number_input("Depth", value=61.0)

table = st.number_input("Table", value=55.0)

x = st.number_input("Length (x)", value=5.0)

y = st.number_input("Width (y)", value=5.0)

z = st.number_input("Depth (z)", value=3.0)

if st.button("Predict"):

    sample = pd.DataFrame(
        {
            "carat": [carat],
            "cut": [cut],
            "color": [color],
            "clarity": [clarity],
            "depth": [depth],
            "table": [table],
            "x": [x],
            "y": [y],
            "z": [z],
        }
    )

    prediction = model.predict(sample)

    st.success(f"Predicted Price: ${prediction[0]:,.2f}")
