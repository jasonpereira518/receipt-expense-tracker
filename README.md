# Expense Tracker

Receipt Expense Tracker is a Python-based tool that automatically extracts text and purchase totals from receipt images using OCR (Optical Character Recognition).
It simplifies expense tracking by identifying store names, detecting totals, and saving data directly into a CSV file for easy analysis.

## Features

• OCR Extraction: Uses pytesseract and Pillow to convert receipt images into readable text.

• Store Detection: Identifies store names (e.g., Walmart, Target, Costco) even when OCR text is slightly distorted, using a 66% in-order fuzzy match.

• Automatic Total Detection: Finds and extracts the final purchase total while ignoring subtotals or taxes.

• Expense Logging: Saves store name, date, total, and timestamp into expenses.csv.

• Modular Design: The OCR functionality is isolated in ocr_reader.py and can be reused in other projects.


## Tech Stack

**Python 3**
• pytesseract (OCR engine)
• Pillow (PIL) for image handling
• Regex & CSV for text parsing and data storage

