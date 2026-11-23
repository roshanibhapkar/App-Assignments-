
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Assig12inputfile - Assig12inputfile.csv")

print("First 5 Records:")
print(data.head())

print("\nDataset Information:")
data.info()

print("\nDataset Shape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

data["TotalCharges"] = pd.to_numeric(
    data["TotalCharges"], errors="coerce"
)

num_cols = data.select_dtypes(include=np.number).columns

for col in num_cols:
    data[col] = data[col].fillna(data[col].median())

cat_cols = data.select_dtypes(include="object").columns

for col in cat_cols:
    if data[col].isnull().sum() > 0:
        data[col] = data[col].fillna(data[col].mode()[0])

print("\nDuplicate Records:")
print(data.duplicated().sum())

data = data.drop_duplicates()

print("\nSummary Statistics:")
print(data.describe())

print("\nCustomer Churn Count:")
print(data["Churn"].value_counts())

print("\nCustomer Churn Percentage:")
print(data["Churn"].value_counts(normalize=True) * 100)

fees = data["MonthlyCharges"].to_numpy()

print("\nMonthly Charges Analysis:")
print("Mean:", np.mean(fees))
print("Median:", np.median(fees))
print("Minimum:", np.min(fees))
print("Maximum:", np.max(fees))
print("Standard Deviation:", np.std(fees))

data["Churn"].value_counts().plot(
    kind="bar",
    title="Customer Churn Distribution"
)

plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

plt.hist(data["MonthlyCharges"], bins=5)

plt.title("Distribution of Monthly Charges")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

data.groupby("Churn")["Tenure"].mean().plot(
    kind="bar",
    title="Average Tenure by Churn Status"
)

plt.xlabel("Churn Status")
plt.ylabel("Average Tenure")
plt.tight_layout()
plt.show()

data.groupby("Churn")["MonthlyCharges"].mean().plot(
    kind="bar",
    title="Average Monthly Charges by Churn Status"
)

plt.xlabel("Churn Status")
plt.ylabel("Average Monthly Charges")
plt.tight_layout()
plt.show()

num_data = data.select_dtypes(include=np.number)

print("\nCorrelation Matrix:")
print(num_data.corr())

print("\nEDA Completed Successfully!")
