# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing necessary dataset
df = pd.read_csv('Company Sales Data.csv')
print(df)

# Creating a line-plot for displaying the month-wise profit of the company
def line_plot():
  plt.plot(df['month_number'], df['total_profit'], linestyle='dotted', marker='o', mec='r', color='black', linewidth=3)
  plt.title('Month-wise Profit')
  plt.xlabel('Month')
  plt.ylabel('Profit')
  plt.grid(True)
  plt.tight_layout()
  plt.show()

# Creating a multi-line plot for displaying the sales-data for all the products month-wise
def multi_line_plot():
  products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']

  for product in products:
    plt.plot(df['month_number'], df[product], marker='o', linewidth=3, label=product)

  plt.title('Sales Data for All Products')
  plt.xlabel('Month')
  plt.ylabel('Sales')
  plt.grid(True)
  plt.legend() 
  plt.tight_layout()
  plt.show()

# Creating a bar plot to compare the sales of facecream and facewash per month
def bar_plot():
  plt.bar(df['month_number'], df['facecream'], color='red', label='Facecream')
  plt.bar(df['month_number'], df['facewash'], color='blue', label='Facewash')
  plt.title('Sales Comparison of Facecream and Facewash')
  plt.xlabel('Month')
  plt.ylabel('Sales')
  plt.grid(True)
  plt.legend()
  plt.tight_layout()
  plt.show()

# Running the charts
line_plot()
multi_line_plot()
bar_plot()