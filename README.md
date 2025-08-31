# 📊 Customer Churn Prediction

A machine learning project to predict **customer churn** (whether a customer will leave a service).  
Includes **EDA, feature engineering, model training**, and an interactive **Streamlit dashboard**.

---

## 🚀 Features
- 📈 Exploratory Data Analysis (EDA)  
- ⚙️ Feature Engineering (missing values, encoding, scaling)  
- 🤖 ML Model Training & Evaluation  
- 🖥️ Streamlit Dashboard for predictions  

---

## 📂 Project Structure
```
customer-churn-prediction/
│── data/
│   ├── raw/                # Original dataset
│   ├── processed/          # Cleaned & feature engineered dataset
│
│── notebooks/
│   ├── 01_EDA.ipynb        # Exploratory Data Analysis
│   ├── 02_Feature_Eng.ipynb# Feature engineering
│   ├── 03_Modeling.ipynb   # ML training + evaluation
│
│── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate_model.py
│
│── models/
│   ├── churn_model.pkl     # Trained ML model
│
│── dashboard/
│   ├── app.py              # Streamlit app
│
│── reports/
│   ├── insights.md         # Documented insights
│   ├── presentation.pptx   # Optional slides
│
│── requirements.txt        # Dependencies
│── README.md               # Project overview
```

---

## 🛠️ Installation
Clone this repository and install dependencies:
```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
```

---

## ▶️ Usage

### 1. Run Notebooks
Navigate to `notebooks/` and open Jupyter Notebooks to explore:
- `01_EDA.ipynb` – Data exploration & visualization  
- `02_Feature_Eng.ipynb` – Feature engineering & preprocessing  
- `03_Modeling.ipynb` – Model training & evaluation  

### 2. Train Model
```bash
python src/train_model.py
```

### 3. Evaluate Model
```bash
python src/evaluate_model.py
```

### 4. Launch Dashboard
```bash
streamlit run dashboard/app.py
```

Upload your **trained model (`churn_model.pkl`)** and a **CSV file** of customer data to generate churn predictions.

---

## 📌 Tech Stack
- **Python**  
- **Pandas, NumPy** – Data manipulation  
- **Scikit-learn** – ML models & preprocessing  
- **Matplotlib, Seaborn** – Visualization  
- **Streamlit** – Interactive dashboard  

---

## 📈 Example Workflow
1. Load and explore the dataset with EDA notebook  
2. Perform preprocessing & feature engineering  
3. Train and save ML model (`churn_model.pkl`)  
4. Use Streamlit dashboard for churn prediction  

---

## 👨‍💻 Author
**Kartik Gore** – [GitHub](https://github.com/Kartik-Gore)
