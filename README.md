# NIDS-PROJECT

# 🛡️ Network Intrusion Detection System (NIDS)

This project is a **Network Intrusion Detection System** built using **machine learning**. It detects whether incoming network traffic is **normal** or a type of **cyber-attack** such as:

- DoS (Denial of Service)
- Probe
- R2L (Remote to Local)
- U2R (User to Root)

The detection is done by uploading a **CSV file** containing network traffic features.

## 🔍 How It Works

1. Upload a `.csv` file containing network traffic data.
2. The Streamlit web interface reads the file.
3. The trained ML model predicts whether each row (packet) is **normal** or an **attack**.
4. The result is displayed in the table with prediction labels.

## ✅ Requirements

- Python
- streamlit
- pandas
- scikit-learn
- joblib

To run locally:
```bash
streamlit run nids_app.py
