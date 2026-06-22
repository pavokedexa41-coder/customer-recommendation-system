import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier

# ==========================================
# LOAD DATASET
# ==========================================

customers = pd.read_csv("customers.csv")

# ==========================================
# ENCODE TARGET COLUMN
# Convert preferred category into numbers
# ==========================================

encoder = LabelEncoder()
customers["preferred_category"] = encoder.fit_transform(
    customers["preferred_category"]
)

# ==========================================
# SELECT FEATURES
# These are the customer details used for prediction
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

X = customers[feature_columns]
y = customers["preferred_category"]

# ==========================================
# SCALE THE FEATURES
# KNN performs better when data is scaled
# ==========================================

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==========================================
# SPLIT DATA INTO TRAINING AND TESTING
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.20,
    random_state=42
)

# ==========================================
# CREATE AND TRAIN THE KNN MODEL
# ==========================================

model = KNeighborsClassifier(
    n_neighbors=7
)

model.fit(X_train, y_train)

# ==========================================
# RECOMMENDATION FUNCTION
# Returns the Top 3 recommendations
# ==========================================

def recommend_top3(age,
                   total_spend,
                   electronics,
                   clothing,
                   groceries,
                   books,
                   sports):

    # Create customer profile
    input_data = pd.DataFrame([[
        age,
        total_spend,
        electronics,
        clothing,
        groceries,
        books,
        sports
    ]], columns=feature_columns)

    # Scale customer profile
    input_scaled = scaler.transform(input_data)

    # Find the 7 nearest neighbours
    distances, indices = model.kneighbors(input_scaled)

    # Create score dictionary
    scores = {
        "Electronics": 0,
        "Clothing": 0,
        "Groceries": 0,
        "Books": 0,
        "Sports": 0
    }

    # Distance-weighted voting
    for distance, index in zip(distances[0], indices[0]):

        label = y_train.iloc[index]

        category = encoder.inverse_transform([label])[0]

        # Weight based on distance
        weight = 1 / (distance + 0.001)

        scores[category] += weight

    # Convert scores to percentages
    total_score = sum(scores.values())

    results = []

    for category, score in scores.items():

        percentage = (score / total_score) * 100

        results.append((
            category,
            round(percentage, 2)
        ))

    # Sort from highest to lowest
    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Return Top 3
    return results[:3]

# ==========================================
# TEST THE RECOMMENDATION SYSTEM
# ==========================================

print("\n===================================")
print(" TOP 3 PRODUCT RECOMMENDATIONS")
print("===================================\n")

results = recommend_top3(
    age=40,
    total_spend=75000,
    electronics=1,
    clothing=5,
    groceries=2,
    books=6,
    sports=4
)

for i, (category, probability) in enumerate(results, start=1):
    print(f"{i}. {category} ({probability:.2f}%)")