import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
df = pd.read_csv('data/store_sku_ba_dataset.csv')

# Conversion Rate Calculation
df['Conversion Rate'] = df['Transactions'] / df['Total Visits']

# Store-Level Conversion
store_conv = df.groupby('Store ID').agg({
    'Total Visits': 'sum',
    'Transactions': 'sum',
    'Revenue': 'sum'
})
store_conv['Conversion Rate'] = store_conv['Transactions'] / store_conv['Total Visits']
store_conv = store_conv.sort_values('Conversion Rate', ascending=False)

# SKU-Level Conversion
sku_conv = df.groupby('SKU ID').agg({
    'Total Visits': 'sum',
    'Transactions': 'sum',
    'Revenue': 'sum'
})
sku_conv['Conversion Rate'] = sku_conv['Transactions'] / sku_conv['Total Visits']
sku_conv = sku_conv.sort_values('Conversion Rate', ascending=False)

# Visualizations
sns.barplot(x=store_conv.head(10).index, y=store_conv['Conversion Rate'].head(10))
plt.title("Top 10 Performing Stores by Conversion Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/charts/top_stores.png')

sns.barplot(x=sku_conv.head(10).index, y=sku_conv['Conversion Rate'].head(10))
plt.title("Top 10 Performing SKUs by Conversion Rate")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/charts/top_skus.png')
