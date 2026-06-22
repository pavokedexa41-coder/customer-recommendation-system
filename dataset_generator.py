import numpy as np
import pandas as pd

# ==========================================
# CUSTOMER DATASET GENERATOR (FIXED VERSION)
# ==========================================

np.random.seed(42)

customers = []
customer_id = 1

def add_noise(value):
    return max(0, value + np.random.randint(-3, 4))

# ==========================================
# 1. YOUNG TECH LOVERS (20)
# ==========================================

for i in range(20):

    age = np.random.randint(18, 31)
    gender = np.random.choice(["M", "F"])
    total_spend = np.random.randint(60000, 100001)

    electronics = add_noise(np.random.randint(8, 13))
    clothing = add_noise(np.random.randint(5, 10))
    groceries = add_noise(np.random.randint(3, 9))
    books = add_noise(np.random.randint(4, 10))
    sports = add_noise(np.random.randint(3, 8))

    customers.append([
        customer_id, age, gender, total_spend,
        electronics, clothing, groceries, books, sports,
        "Electronics",
        "Young Tech Lovers"
    ])

    customer_id += 1

# ==========================================
# 2. FAMILY SHOPPERS (20)
# ==========================================

for i in range(20):

    age = np.random.randint(30, 56)
    gender = np.random.choice(["M", "F"])
    total_spend = np.random.randint(30000, 80001)

    electronics = add_noise(np.random.randint(4, 9))
    clothing = add_noise(np.random.randint(6, 11))
    groceries = add_noise(np.random.randint(9, 15))
    books = add_noise(np.random.randint(4, 10))
    sports = add_noise(np.random.randint(3, 7))

    customers.append([
        customer_id, age, gender, total_spend,
        electronics, clothing, groceries, books, sports,
        "Groceries",
        "Family Shoppers"
    ])

    customer_id += 1

# ==========================================
# 3. FASHION LOVERS (20)
# ==========================================

for i in range(20):

    age = np.random.randint(18, 45)
    gender = np.random.choice(["M", "F"])
    total_spend = np.random.randint(40000, 90001)

    electronics = add_noise(np.random.randint(4, 9))
    clothing = add_noise(np.random.randint(9, 15))
    groceries = add_noise(np.random.randint(4, 9))
    books = add_noise(np.random.randint(3, 8))
    sports = add_noise(np.random.randint(4, 9))

    customers.append([
        customer_id, age, gender, total_spend,
        electronics, clothing, groceries, books, sports,
        "Clothing",
        "Fashion Lovers"
    ])

    customer_id += 1

# ==========================================
# 4. BOOK LOVERS (20)
# ==========================================

for i in range(20):

    age = np.random.randint(22, 60)
    gender = np.random.choice(["M", "F"])
    total_spend = np.random.randint(25000, 70001)

    electronics = add_noise(np.random.randint(3, 8))
    clothing = add_noise(np.random.randint(4, 9))
    groceries = add_noise(np.random.randint(4, 9))
    books = add_noise(np.random.randint(9, 15))
    sports = add_noise(np.random.randint(3, 7))

    customers.append([
        customer_id, age, gender, total_spend,
        electronics, clothing, groceries, books, sports,
        "Books",
        "Book Lovers"
    ])

    customer_id += 1

# ==========================================
# 5. SPORTS ENTHUSIASTS (20)
# ==========================================

for i in range(20):

    age = np.random.randint(18, 45)
    gender = np.random.choice(["M", "F"])
    total_spend = np.random.randint(35000, 90001)

    electronics = add_noise(np.random.randint(4, 9))
    clothing = add_noise(np.random.randint(5, 11))
    groceries = add_noise(np.random.randint(3, 8))
    books = add_noise(np.random.randint(3, 8))
    sports = add_noise(np.random.randint(9, 15))

    customers.append([
        customer_id, age, gender, total_spend,
        electronics, clothing, groceries, books, sports,
        "Sports",
        "Sports Enthusiasts"
    ])

    customer_id += 1

# ==========================================
# CREATE DATAFRAME
# ==========================================

df = pd.DataFrame(customers, columns=[
    "customer_id",
    "age",
    "gender",
    "total_spend",
    "purchases_electronics",
    "purchases_clothing",
    "purchases_groceries",
    "purchases_books",
    "purchases_sports",
    "preferred_category",
    "customer_segment"
])

# ==========================================
# SAVE DATASET
# ==========================================

df.to_csv("customers.csv", index=False)

print("\n==========================================")
print(" FIXED CUSTOMER DATASET CREATED ")
print("==========================================")

print("\nDistribution:")
print(df["preferred_category"].value_counts())