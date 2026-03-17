from formatter import format_bill
from pdf_generator import create_pdf
from utils import get_items, get_basic_info

def main():
    print("=== MAKEIT BILL GENERATOR ===\n")

    data = get_basic_info()
    data["items"] = get_items()

    formatted = format_bill(data)

    create_pdf(formatted, "bill.pdf")

    print("\n✅ Bill generated successfully: bill.pdf")

if __name__ == "__main__":
    main()