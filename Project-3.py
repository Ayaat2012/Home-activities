# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing necessary dataset
df = pd.read_csv('Company Sales Data.csv')
print(df)

# Creating a line-plot for displaying the month-wise profit of the company
def monthlyProfit():
    plt.plot('total_profit', 'month_number', marker = 'o', mec = 'r', linestyle = 'dotted', color = 'black', linewidth = 3)
    plt.title("Monthly Profit")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

monthlyProfit()