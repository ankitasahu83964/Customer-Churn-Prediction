import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("Models/churn_model.pkl")
scaler = joblib.load("Models/scaler.pkl")
feature_columns = joblib.load("Models/feature_columns.pkl")
totalcharges_median = joblib.load("Models/totalcharges_median.pkl")

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction System")
st.write("Predict customer churn risk using Machine Learning.")

st.subheader("Enter Customer Information")

with st.form("customer_form"):

    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        partner = st.selectbox("Partner", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["Yes", "No"])
        tenure = st.number_input("Tenure (Months)", 0, 72, 12)
        phone = st.selectbox("Phone Service", ["Yes", "No"])
        multiple_lines = st.selectbox(
            "Multiple Lines", ["No", "Yes", "No phone service"]
        )
        internet = st.selectbox(
            "Internet Service", ["DSL", "Fiber optic", "No"]
        )
        online_security = st.selectbox(
            "Online Security", ["Yes", "No", "No internet service"]
        )
        online_backup = st.selectbox(
            "Online Backup", ["Yes", "No", "No internet service"]
        )

    with col2:
        device_protection = st.selectbox(
            "Device Protection", ["Yes", "No", "No internet service"]
        )
        tech_support = st.selectbox(
            "Tech Support", ["Yes", "No", "No internet service"]
        )
        streaming_tv = st.selectbox(
            "Streaming TV", ["Yes", "No", "No internet service"]
        )
        streaming_movies = st.selectbox(
            "Streaming Movies", ["Yes", "No", "No internet service"]
        )
        contract = st.selectbox(
            "Contract", ["Month-to-month", "One year", "Two year"]
        )
        paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
        payment = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )
        monthly = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
        total = st.number_input("Total Charges", 0.0, 10000.0, 840.0)

    submitted = st.form_submit_button("Predict Customer Churn")

if submitted:

    customer = pd.DataFrame([{
        "gender": gender,
        "SeniorCitizen": senior,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone,
        "MultipleLines": multiple_lines,
        "InternetService": internet,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless,
        "PaymentMethod": payment,
        "MonthlyCharges": monthly,
        "TotalCharges": total
    }])

    customer["TotalCharges"] = pd.to_numeric(
        customer["TotalCharges"], errors="coerce"
    ).fillna(totalcharges_median)

    encoded = pd.get_dummies(customer, drop_first=True, dtype=int)
    encoded = encoded.reindex(columns=feature_columns, fill_value=0)

    scaled = scaler.transform(encoded)

    probability = model.predict_proba(scaled)[0][1]
    prediction = model.predict(scaled)[0]

    st.subheader("Prediction Result")
    st.metric("Churn Probability", f"{probability * 100:.2f}%")

    if probability >= 0.70:
        st.error("High Risk: Customer is likely to churn.")
        st.write("Recommendation: Contact the customer and offer a suitable retention plan.")

    elif probability >= 0.40:
        st.warning("Medium Risk: Customer needs attention.")
        st.write("Recommendation: Improve customer engagement and monitor satisfaction.")

    else:
        st.success("Low Risk: Customer is less likely to churn.")
        st.write("Recommendation: Maintain service quality and customer relationship.")

    st.write(
        "Model Prediction:",
        "Churn" if prediction == 1 else "No Churn"
    )
