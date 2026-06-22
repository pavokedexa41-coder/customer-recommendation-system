import streamlit as st
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# ==========================================
# LOAD DATASET
# ==========================================

df = pd.read_csv("customers.csv")

# ==========================================
# ENCODE TARGET
# ==========================================

encoder = LabelEncoder()
df["preferred_category"] = encoder.fit_transform(df["preferred_category"])

# ==========================================
# FEATURES
# ==========================================

feature_columns = [
    "age",
    "total_spend",
    "purchases_electronics",
    "purchases_clothing",
    "purchases_groceries",
    "purchases_books",
    "purchases_sports"
]

X = df[feature_columns]
y = df["preferred_category"]

# ==========================================
# SCALE DATA
# ==========================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# TRAIN MODEL
# ==========================================

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_scaled, y)

# ==========================================
# STREAMLIT UI
# ==========================================

st.title("🛒 Customer Purchase Recommendation System")
st.write("Enter customer details to get top 3 product recommendations")

# INPUTS
age = st.slider("Age", 18, 70, 30)
total_spend = st.slider("Total Spend (KSh)", 10000, 100000, 50000)

electronics = st.slider("Electronics Purchases", 0, 15, 5)
clothing = st.slider("Clothing Purchases", 0, 15, 5)
groceries = st.slider("Groceries Purchases", 0, 15, 5)
books = st.slider("Books Purchases", 0, 15, 5)
sports = st.slider("Sports Purchases", 0, 15, 5)

# PREDICTION BUTTON
if st.button("Get Recommendations"):

    input_data = pd.DataFrame([[age, total_spend, electronics, clothing, groceries, books, sports]],
                              columns=feature_columns)

    input_scaled = scaler.transform(input_data)

    distances, indices = model.kneighbors(input_scaled)

    scores = {
        "Electronics": 0,
        "Clothing": 0,
        "Groceries": 0,
        "Books": 0,
        "Sports": 0
    }

    for dist, idx in zip(distances[0], indices[0]):

        label = y.iloc[idx]
        category = encoder.inverse_transform([label])[0]

        weight = 1 / (dist + 0.001)
        scores[category] += weight

    total = sum(scores.values())

    results = []

    for cat, val in scores.items():
        percent = (val / total) * 100
        results.append((cat, percent))

    results.sort(key=lambda x: x[1], reverse=True)

    st.subheader("Top 3 Recommendations")

    for i, (cat, prob) in enumerate(results[:3], 1):
        st.write(f"{i}. {cat} ({prob:.2f}%)")