import os
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("charts", exist_ok=True)
os.makedirs("reports", exist_ok=True)

print("=" * 65)
print("     STUDENT PERFORMANCE ANALYSIS - DAY 14")
print("=" * 65)

df = pd.read_csv("students.csv")

print("\nDataset Loaded Successfully!\n")
print(df)

print("\nDataset Shape:", df.shape)

print("\nAverage Marks:", round(df["Marks"].mean(), 2))
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())

branch_avg = df.groupby("Branch")["Marks"].mean()

print("\nBranch-wise Average Marks")
print(branch_avg)

# Chart 1
plt.figure(figsize=(6,4))
branch_avg.plot(kind="bar")
plt.title("Average Marks by Branch")
plt.tight_layout()
plt.savefig("charts/average_marks.png")
plt.close()

# Chart 2
plt.figure(figsize=(6,4))
plt.hist(df["Marks"], bins=5)
plt.title("Marks Distribution")
plt.tight_layout()
plt.savefig("charts/marks_distribution.png")
plt.close()

# Chart 3
plt.figure(figsize=(6,4))
plt.plot(df["Name"], df["Marks"], marker="o")
plt.title("Student Performance")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/branch_performance.png")
plt.close()

with open("reports/analysis_report.txt", "w") as file:
    file.write("Student Performance Analysis Report\n")
    file.write("="*40 + "\n")
    file.write(f"Total Students: {len(df)}\n")
    file.write(f"Average Marks: {df['Marks'].mean():.2f}\n")
    file.write(f"Highest Marks: {df['Marks'].max()}\n")
    file.write(f"Lowest Marks: {df['Marks'].min()}\n\n")
    file.write("Branch-wise Average Marks\n")
    file.write(str(branch_avg))

print("\nCharts generated successfully.")
print("Analysis report saved successfully.")

print("\nProject Completed Successfully ✅")
print("=" * 65)
