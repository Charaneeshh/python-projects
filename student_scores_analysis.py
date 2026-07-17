import pandas as pd
import matplotlib.pyplot as plt

# Sample student score data
scores = [
    {"name": "Aarav", "subject": "Math", "score": 85},
    {"name": "Aarav", "subject": "Science", "score": 78},
    {"name": "Deepa", "subject": "Math", "score": 92},
    {"name": "Deepa", "subject": "Science", "score": 88},
    {"name": "Mia", "subject": "Math", "score": 73},
    {"name": "Mia", "subject": "Science", "score": 80},
]

df = pd.DataFrame(scores)
print("Student scores data:\n")
print(df)

print("\nAverage score by student:")
print(df.groupby("name")["score"].mean())

print("\nAverage score by subject:")
print(df.groupby("subject")["score"].mean())

best_student = df.groupby("name")["score"].mean().idxmax()
print(f"\nBest average score: {best_student}")

# Create a bar chart and save it
summary = df.groupby("subject")["score"].mean().reset_index()
plt.figure(figsize=(6, 4))
plt.bar(summary["subject"], summary["score"], color=["#4CAF50", "#2196F3"])
plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.ylim(0, 100)
plt.savefig("score_chart.png")
print("\nSaved chart to score_chart.png")
print("Run this file with Python after installing pandas and matplotlib.")
