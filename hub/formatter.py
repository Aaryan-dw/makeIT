import datetime
import random

def format_bill(data):
    items = []
    total = 0

    for i, item in enumerate(data["items"], start=1):
        amount = item["price"] * item["qty"]
        total += amount

        items.append([
            i,
            item["name"],
            item.get("hsn", "0000"),
            item["qty"],
            item["price"],
            amount
        ])

    cgst = total * 0.09
    sgst = total * 0.09
    grand_total = total + cgst + sgst

    return {
        "company": data["company"],
        "gstin": data["gstin"],
        "address": data["address"],
        "email": data["email"],
        "customer": data["customer"],
        "invoice_no": f"INV-{random.randint(1000,9999)}",
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "items": items,
        "total": total,
        "cgst": cgst,
        "sgst": sgst,
        "grand_total": grand_total
    }