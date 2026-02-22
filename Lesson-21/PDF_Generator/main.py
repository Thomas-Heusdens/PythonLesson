from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

data_frame = pd.read_csv("topics.csv")

for index, row in data_frame.iterrows():
    for i in range(row["Pages"]):
        pdf.add_page()
        # First page has the title
        if i == 0:
            # Title
            pdf.set_font(family="Helvetica", style="B", size=24)
            pdf.set_text_color(100, 100, 255)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", border=0, ln=1)
            # Lines
            pdf.set_draw_color(100, 100, 255)
            for line in range(21, 288, 10):
                pdf.line(10, line, 200, line)
            # Footer
            pdf.ln(260)
            pdf.set_font(family="Times", style="I", size=12)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R", border=0, ln=1)
        # All the other pages have no title
        else:
            # Lines
            pdf.set_draw_color(100, 100, 255)
            for line in range(10, 288, 10):
                pdf.line(10, line, 200, line)
            # Footer
            pdf.ln(272)
            pdf.set_font(family="Times", style="I", size=12)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R", border=0, ln=1)

# Create PDF
pdf.output("output.pdf")