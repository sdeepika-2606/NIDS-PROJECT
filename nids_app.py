import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("nids_model.pkl")

st.title("🛡️ Network Intrusion Detection System (NIDS)")
st.write("Upload a network traffic CSV file to detect intrusions.")

uploaded_file = st.file_uploader("📤 Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("🔍 Uploaded Data")
    st.dataframe(df.head())

    # Match model features
    required_cols = model.feature_names_in_
    for col in required_cols:
        if col not in df.columns:
            df[col] = 0  # fill missing with 0

    df = df[required_cols]

    # Predict
    predictions = model.predict(df)
    df["Prediction"] = predictions

    st.subheader("✅ Prediction Results")
    st.dataframe(df)

    # Downloadable output
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Results as CSV", csv, "nids_results.csv", "text/csv")
