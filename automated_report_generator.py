import pandas as pd
from fpdf import FPDF
from datetime import datetime

# Step 1: Read data from CSV
data = pd.read_csv('sample_data.csv')  # Replace with your actual file

# Step 2: Perform analysis (basic stats)
summary = data.describe()

# Step 3: Convert summary to string
summary_str = summary.to_string()

# Step 4: Create a PDF using FPDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'AUTOMATED REPORT', ln=1, align='C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=1, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=1)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, body)
        self.ln()

# Step 5: Generate the PDF
pdf = PDF()
pdf.add_page()
pdf.chapter_title("Data Summary")
pdf.chapter_body(summary_str)

pdf.output("sample_report.pdf")
print("PDF report generated as 'sample_report.pdf'")
