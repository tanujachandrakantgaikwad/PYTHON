import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Tanuja', 'Ravi', 'Sneha', 'Amit'],
    'Age': [22, 25, 23, 24],
    'City': ['Pune', 'Mumbai', 'Nashik', 'Nagpur']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Display basic information
print("\nBasic Information:")
print(df.info())

# Display statistics summary
print("\nStatistics Summary:")
print(df.describe())

# Access specific column
print("\nNames Column:")
print(df['Name'])
