import pandas as pd

# Load dataset
df = pd.read_csv("data.csv")

# Display basic information
print("Dataset preview:")
print(df.head())

# Total balance
total_balance = df["amount"].sum()

# Expenses by category
expenses_by_category = (
    df[df["amount"] < 0]
    .groupby("category")["amount"]
    .sum()
)

print("\nTotal balance:", total_balance)
print("\nExpenses by category:")
print(expenses_by_category)
