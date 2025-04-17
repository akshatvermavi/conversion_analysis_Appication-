# 🧾 Conversion Analysis Project — AppsForBharat

This project performs a **conversion rate analysis** at both the **store** and **SKU** level to provide actionable insights and recommendations to improve sales performance.

---

### Github Repository Link of Complete Project 

[https://github.com/akshatvermavi/conversion_analysis_project_AppsForBharat](https://github.com/akshatvermavi/conversion_analysis_project_AppsForBharat)

### Project Drive Link

[https://drive.google.com/drive/folders/1KMSgIuIb8kPFZRP8djsOhBKJN8MQWo9M?usp=sharing](https://drive.google.com/drive/folders/1KMSgIuIb8kPFZRP8djsOhBKJN8MQWo9M?usp=sharing)

---

## 📁 Project Structure

```
conversion_analysis_project_AppsForBharat/
│
├── data/
│   └── store_sku_ba_dataset.csv       # Provided dataset
│
├── outputs/
│   ├── charts/
│   │   ├── top_stores.png             # Bar chart: Top performing stores by conversion rate
│   │   └── top_skus.png               # Bar chart: Top performing SKUs by conversion rate
│   └── summary_report.pdf             # Final PDF report with insights & recommendations
│
├── scripts/
│   ├── conversion_analysis.py         # Script for analyzing store and SKU conversion rates
│   └── generate_report.py             # Script to generate a PDF report
│
├── requirements.txt                   # Required Python packages
└── README.md                          # Project documentation
```

---

## 🧪 Objective

To analyze transaction-level data, calculate conversion rates, and visualize:

- Top performing **Stores**
- Top performing **SKUs**

Then, generate a **summary report** highlighting key trends and recommendations for business improvement.

---

## 🛠️ Setup Instructions

1. **Clone the repository or download the files**
2. **Install dependencies**

Make sure you're using Python ≥ 3.8. Use a virtual environment if needed:

```bash
pip install -r requirements.txt
```

> ⚠️ If you are behind a proxy (like a campus/office network), use:
>
> ```bash
> pip install -r requirements.txt --proxy http://username:password@proxy_address:port
> ```

3. **Place the dataset**

Download the provided dataset and place it at:

```
data/store_sku_ba_dataset.csv
```

4. **Run analysis and generate charts**

```bash
python scripts/conversion_analysis.py
```

This will generate two charts in the `outputs/charts/` directory.

5. **Generate the final PDF report**

```bash
python scripts/generate_report.py
```

This will create the `summary_report.pdf` in the `outputs/` folder.

---

## 📊 Output Charts

- `top_stores.png`: Bar chart of top stores by conversion rate
- `top_skus.png`: Bar chart of top SKUs by conversion rate

---

## 📄 PDF Report

- The PDF (`summary_report.pdf`) includes:
  - A summary of top-performing stores and SKUs
  - Embedded charts
  - Recommendations for improving underperforming segments

---

## 📦 Requirements

```txt
pandas
matplotlib
seaborn
fpdf2         # (or fpdf if you're using the original version)
Pillow
```

Install them via:

```bash
pip install pandas matplotlib seaborn fpdf2 Pillow
```

---

## 💡 Recommendations Provided

- Focus marketing efforts on top-converting stores.
- Investigate low-performing SKUs and consider promotional pricing.
- Optimize inventory and distribution for high-converting SKUs.
- Conduct A/B testing for layout or user journey improvements.

---

## 🙋‍♂️ Author

**Akshat Verma**
Conversion Analysis Project for Business Analyst Intern Task
📅 17th April 2025

## Code - `conversion_analysis.py`

```python
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
```

## Code - `generate_report.py`

```python
from fpdf import FPDF  # fpdf2 for better Unicode support
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Conversion Analysis Summary Report', ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln()

    def add_image(self, img_path, w=160):
        self.image(img_path, w=w)
        self.ln(10)

# Create PDF
pdf = PDF()
pdf.add_page()

# Key Findings
pdf.chapter_title("Key Findings")
key_findings = '''
- Store_39 has the highest conversion rate (~67%) among all stores.
- SKU_11 leads the SKU performance with a conversion rate around 59%.
- Some stores (Store_15, Store_31) and SKUs (SKU_15, SKU_13) show lower than 35% conversion.
- High-converting stores tend to have fewer visits but higher purchase intent.
'''
pdf.chapter_body(key_findings)

# Recommendations
pdf.chapter_title("Recommendations")
recommendations = '''
- Investigate marketing strategies or store layout used by top stores like Store_39 and Store_49.
- Promote high-converting SKUs like SKU_11 and SKU_7 more prominently across underperforming stores.
- Consider A/B testing store flows or checkout processes in low-performing stores.
- Use top stores as a benchmark and apply similar inventory positioning in others.
'''
pdf.chapter_body(recommendations)

# Charts
pdf.chapter_title("Top Performing Stores by Conversion Rate")
pdf.add_image("outputs/charts/top_stores.png")

pdf.chapter_title("Top Performing SKUs by Conversion Rate")
pdf.add_image("outputs/charts/top_skus.png")

# Save PDF
pdf.output("outputs/summary_report.pdf")
print("PDF generated: outputs/summary_report.pdf")
```
