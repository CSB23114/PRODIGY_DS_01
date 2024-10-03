import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Example dataset
data = {'Gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
        'Count': [50, 45, 55, 65, 60, 50, 40, 55]}

df = pd.DataFrame(data)

# Bar chart
sns.barplot(x='Gender', y='Count', data=df)
plt.title('Gender Distribution')
plt.show()


# Example dataset
ages = np.random.randint(18, 60, size=100)  # Random age data

# Histogram
sns.histplot(ages, kde=False, bins=10)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
