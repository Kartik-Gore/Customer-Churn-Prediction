import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.title("📊 Customer Churn Prediction Dashboard")
st.write("Follow the steps below to upload your model and customer data from your local storage.")

# ---------------------------
# 1. Upload / Load trained model
# ---------------------------
st.subheader("Step 1: Upload Trained Model (.pkl)")
uploaded_model = st.file_uploader("Upload Model File", type="pkl", key="model_uploader")

if uploaded_model is not None:
    model = joblib.load(uploaded_model)
    st.success("✅ Model loaded successfully!")

    # ---------------------------
    # 2. Upload Customer CSV
    # ---------------------------
    st.subheader("Step 2: Upload Customer CSV")
    uploaded_file = st.file_uploader("Upload Customer CSV", type="csv", key="csv_uploader")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### 📂 Uploaded Data Preview", df.head())

        # ---------------------------
        # 3. Preprocess Dataset
        # ---------------------------
        df_processed = pd.get_dummies(df, drop_first=True).reindex(
            columns=model.feature_names_in_, fill_value=0
        )

        # ---------------------------
        # 4. Predict Churn & Probability
        # ---------------------------
        predictions = model.predict(df_processed)
        probabilities = model.predict_proba(df_processed)[:, 1]  # probability of churn
        df["Churn Prediction"] = predictions
        df["Churn Probability (%)"] = (probabilities * 100).round(2)

        st.write("### 🔮 Predictions Preview", df.head())

        # ---------------------------
        # 5. Interactive Charts
        # ---------------------------
        st.subheader("📈 Churn Insights")

        # Bar chart: Churn count
        churn_count = df["Churn Prediction"].value_counts().reset_index()
        churn_count.columns = ["Churn Status", "Count"]
        churn_count["Churn Status"] = churn_count["Churn Status"].map({0: "No Churn", 1: "Churn"})
        fig_bar = px.bar(churn_count, x="Churn Status", y="Count", color="Churn Status",
                         title="Churn Count", text="Count", color_discrete_map={"Churn": "red", "No Churn": "green"})
        st.plotly_chart(fig_bar)

        # Histogram: Churn Probability
        fig_hist = px.histogram(df, x="Churn Probability (%)", nbins=20, title="Churn Probability Distribution",
                                color="Churn Prediction", color_discrete_map={0: "green", 1: "red"})
        st.plotly_chart(fig_hist)

        # Pie chart: Churn vs Non-Churn
        fig_pie = px.pie(churn_count, names="Churn Status", values="Count", title="Churn vs Non-Churn")
        st.plotly_chart(fig_pie)

        # Optional: Download predictions
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download Predictions as CSV",
            data=csv,
            file_name="churn_predictions.csv",
            mime="text/csv",
        )

    else:
        st.info("📂 Please upload a CSV file for prediction.")
else:
    st.info("📂 Please upload your trained model (.pkl) first.")
