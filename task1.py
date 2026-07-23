import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Count male and female passengers
gender_count = df["Sex"].value_counts()

# Create bar chart
plt.figure(figsize=(6,4))
gender_count.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Passengers")

plt.show()