def get_items():
    print("Enter items (name,price,qty,hsn) (type END to finish)")

    items = []

    while True:
        line = input("> ")

        if line.upper() == "END":
            break

        try:
            name, price, qty, hsn = line.split(",")
            items.append({
                "name": name,
                "price": float(price),
                "qty": int(qty),
                "hsn": hsn
            })
        except:
            print("Format: name,price,qty,hsn")

    return items

def get_basic_info():
    company = input("Company Name: ")
    gstin = input("GSTIN: ")
    address = input("Address: ")
    email = input("Email: ")
    customer = input("Customer Name: ")

    return {
        "company": company,
        "gstin": gstin,
        "address": address,
        "email": email,
        "customer": customer
    }