from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfFileReader, PdfFileWriter


def makeWatermark():
    text = input("Enter the watermark text here:")
    pdf = canvas.Canvas("watermark.pdf", pagesize=A4)
    pdf.translate(inch, inch)
    pdf.setFillColor(colors.grey, alpha=0.3)
    pdf.setFont("Helvetica", 50)
    pdf.rotate(45)
    pdf.drawCentredString(400, 100, 'ABC')
    pdf.drawCentredString(400, 50, 'CONFIDENTIAL')

    pdf.save()
    
    
def makepdf():
    pdf_file = input("PDF file: ")
    watermark = 'watermark.pdf'
    merged = "Watermarked.pdf"

    with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
        input_pdf = PdfFileReader(input_file)
        watermark_pdf = PdfFileReader(watermark_file)
        watermark_page = watermark_pdf.getPage(0)
        
        
        output = PdfFileWriter()

        for i in range(input_pdf.getNumPages()):
            pdf_page = input_pdf.getPage(i)
            pdf_page.mergePage(watermark_page)
            output.addPage(pdf_page)

        with open(merged, "wb") as merged_file:
            output.write(merged_file)
            
            

makeWatermark()
makepdf()
