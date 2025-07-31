import streamlit as st
import pandas as pd
import joblib

# Load the model
model = joblib.load('nids_model.pkl')

st.title("🛡️ Network Intrusion Detection System (NIDS)")
st.write("Upload a CSV file to detect network intrusions using a trained ML model.")

# File upload
uploaded_file = st.file_uploader("Upload CSV", type=["csv", "txt"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📊 Uploaded Data Preview")
    st.dataframe(df.head())

    # Predict
    predictions = model.predict(df)
    df['Prediction'] = predictions

    st.subheader("✅ Prediction Results")
    st.write(df[['Prediction']].value_counts())
    st.dataframe(df)

    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Predictions", csv, "nids_predictions.csv", "text/csv")
