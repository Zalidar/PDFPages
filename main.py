from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    if row['Pages'] > 1:
        for x in range (row['Pages']-1):
            pdf.add_page()

pdf.output("output.pdf")