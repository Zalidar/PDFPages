from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="letter")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=0)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    for y in range(30, 265, 10):
        pdf.line(x1=10, x2=200, y1=y, y2=y)
    pdf.ln(245)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R", ln=1, border=0)
    if row['Pages'] > 1:
        for x in range (row['Pages']-1):
            pdf.add_page()
            for y in range(20, 265, 10):
                pdf.line(x1=10, x2=200, y1=y, y2=y)
            pdf.ln(255)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row['Topic'], align="R", ln=1, border=0)

pdf.output("output.pdf")
