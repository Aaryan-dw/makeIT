from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(data, filename):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []

    # HEADER
    story.append(Paragraph(f"<b>{data['company']}</b>", styles["Title"]))
    story.append(Paragraph(f"GSTIN: {data['gstin']}", styles["Normal"]))
    story.append(Paragraph(data["address"], styles["Normal"]))
    story.append(Paragraph(data["email"], styles["Normal"]))
    story.append(Spacer(1, 10))

    story.append(Paragraph("<b>Tax Invoice</b>", styles["Heading2"]))
    story.append(Spacer(1, 10))

    # CLIENT + INVOICE INFO TABLE
    info_table = Table([
        ["Client Name:", data["customer"], "Invoice No:", data["invoice_no"]],
        ["Date:", data["date"], "", ""]
    ])
    info_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))
    story.append(info_table)
    story.append(Spacer(1, 15))

    # MAIN TABLE
    table_data = [["Sr No", "Description", "HSN", "Qty", "Rate", "Amount"]]
    table_data += data["items"]
    table_data.append(["", "", "", "", "Total", data["total"]])
    table_data.append(["", "", "", "", "CGST (9%)", data["cgst"]])
    table_data.append(["", "", "", "", "SGST (9%)", data["sgst"]])
    table_data.append(["", "", "", "", "Grand Total", data["grand_total"]])

    table = Table(table_data)
    table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("BACKGROUND", (0,0), (-1,0), colors.grey)
    ]))
    story.append(table)
    story.append(Spacer(1, 20))

    # BANK DETAILS
    bank_table = Table([
        ["Bank Name", "Your Bank"],
        ["Account No", "XXXXXXXXXX"],
        ["IFSC Code", "XXXX0000"]
    ])
    bank_table.setStyle(TableStyle([
        ("GRID", (0,0), (-1,-1), 1, colors.black)
    ]))
    story.append(Paragraph("<b>Bank Details</b>", styles["Heading3"]))
    story.append(bank_table)

    story.append(Spacer(1, 30))
    story.append(Paragraph("Authorized Signatory", styles["Normal"]))

    doc.build(story)