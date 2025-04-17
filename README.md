# 🧾 Conversion Analysis Project — AppsForBharat

This project performs a **conversion rate analysis** at both the **store** and **SKU** level to provide actionable insights and recommendations to improve sales performance.

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
> ```
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

You can install them via:

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
