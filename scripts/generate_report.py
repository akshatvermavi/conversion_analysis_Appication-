# from fpdf import FPDF
from fpdf import FPDF  # Same name but better Unicode support in fpdf2
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
key_findings = """
- Store_39 has the highest conversion rate (~67%) among all stores.
- SKU_11 leads the SKU performance with a conversion rate around 59%.
- Some stores (Store_15, Store_31) and SKUs (SKU_15, SKU_13) show lower than 35% conversion.
- High-converting stores tend to have fewer visits but higher purchase intent.
"""
pdf.chapter_body(key_findings)

# Recommendations
pdf.chapter_title("Recommendations")
recommendations = """
- Investigate marketing strategies or store layout used by top stores like Store_39 and Store_49.
- Promote high-converting SKUs like SKU_11 and SKU_7 more prominently across underperforming stores.
- Consider A/B testing store flows or checkout processes in low-performing stores.
- Use top stores as a benchmark and apply similar inventory positioning in others.
"""
pdf.chapter_body(recommendations)

# Charts
pdf.chapter_title("Top Performing Stores by Conversion Rate")
pdf.add_image("outputs/charts/top_stores.png")

pdf.chapter_title("Top Performing SKUs by Conversion Rate")
pdf.add_image("outputs/charts/top_skus.png")

# Save PDF
pdf.output("outputs/summary_report.pdf")
print("PDF generated: outputs/summary_report.pdf")
