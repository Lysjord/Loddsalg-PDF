import json from reportlab.lib.pagesizes import A4 from reportlab.pdfgen import canvas from reportlab.platypus import Image

Filstier

json_path = "input_data.json" pdf_path = "Lådsalg.pdf"

PDF-dimensjoner

width, height = A4

Funksjon for å legge inn bilder

def draw_image(c, img_path, x, y, width, height): try: img = Image(img_path, width, height) img.drawOn(c, x, y) except Exception as e: print(f"Feil med bilde {img_path}: {e}")

Funksjon for å generere PDF

def generate_pdf(data): c = canvas.Canvas(pdf_path, pagesize=A4)

# Legg inn logo
draw_image(c, data.get("logo"), 50, height - 150, 100, 100)

# Overskrift
c.setFont("Helvetica-Bold", 24)
c.drawCentredString(width / 2, height - 50, "Lådsalg - KSK G13")

# VIPPS-nummer og pris per lodd
c.setFont("Helvetica", 14)
c.drawString(50, height - 180, f"VIPPS: {data.get('vipps_number')}")
c.drawString(50, height - 200, f"Pris per lodd: {data.get('price_per_ticket')} kr")

# Midtfelt for sponsorbilder
sponsors = data.get("sponsors", [])
x_offset = 60
y_offset = height - 300
for sponsor in sponsors:
    draw_image(c, sponsor, x_offset, y_offset, 100, 100)
    x_offset += 120
    if x_offset + 100 > width - 60:
        x_offset = 60
        y_offset -= 120

# Nedrefelt for premier
prizes = data.get("prizes", [])
y_offset = 100
c.setFont("Helvetica", 12)
for prize in prizes:
    c.drawString(60, y_offset, prize)
    y_offset -= 15
    if y_offset < 60:
        c.showPage()
        y_offset = height - 60

# Lagre PDF
c.save()

Les JSON og generer PDF

def main(): try: with open(json_path, "r", encoding="utf-8") as file: data = json.load(file) generate_pdf(data) print("PDF generert som Lådsalg.pdf") except Exception as e: print(f"Feil ved generering av PDF: {e}")

if name == "main": main()


