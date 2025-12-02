from ocr_reader import extract_text
import re, csv
import datetime

def parse_total(text) -> float:
    """
    Extracts the total amount from the OCR text.
    """
    
    pattern = r'\bTotal\s*\$?(\d+\.\d{2})'

    match = re.search(pattern, text, re.IGNORECASE)
    return float(match.group(1)) if match else 0.0

KNOWN_STORES = [
    "walmart", "target", "costco", "aldi", "kroger", "cvs",
    "best buy", "lowe's", "home depot", "starbucks", "walgreens",
    "sam's Club", "whole Foods", "trader Joe's"
]

def _ratio_in_order(line: str, store: str) -> float:
    """
    Returns the ratio of characters in 'store' that appear in 'line' in order.
    """
    a = line.lower()
    b = store.lower()
    i,j = 0,0
    matched = 0

    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            matched += 1
            j += 1
        i += 1

    return matched / len(b)

def parse_store_name(text) -> str:
    """
    Extracts the store name from the OCR text.
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    for line in lines:
        for store in KNOWN_STORES:
            if _ratio_in_order(line, store) > 0.6:
                return store.title()
        if any(keyword in line.lower() for keyword in KNOWN_STORES):
            return line
        if re.search(r'\b(store|mart|shop|supermarket|grocery|market)\b', line, re.IGNORECASE):
            return line
                    
    return "Unknown Store"


def save_to_csv(store, date, total, added_date=None):
    """
    Saves the extracted data to a CSV file.
    """
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([store, date, total, added_date if added_date else ""])

if __name__ == "__main__":
    text = extract_text('sample_receipt.webp')
    
    total_amount = parse_total(text)
    store_name = parse_store_name(text)

    if total_amount:
        x = datetime.datetime.now()
        if store_name:
            print(f"Store Name: {store_name}")
        else:
            print("Store Name: Unknown Store")
        print(f"Total Amount: ${total_amount:.2f}")
        save_to_csv(store_name, x.strftime("%Y-%m-%d"), total_amount, x.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        print("Total amount not found in the receipt.")