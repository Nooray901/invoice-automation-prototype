
import pytesseract
from PIL import Image
import re
import pandas as pd

# Simulated OCR output
simulated_text = """
Global Tech Ltd.
Unit 4, Innovation Park, Dublin
VAT No: IE123456T

Invoice No: INV-00834
Invoice Date: 2025-03-15
Due Date: 2025-04-15

Bill To:
Smart Systems Ireland
Accounts Payable Department

Description            Quantity     Unit Price     Total
----------------------------------------------------------
Consulting Services     10 hrs       EUR 100.00     EUR 1,000.00
Software License         1 unit      EUR 250.00     EUR 250.00
----------------------------------------------------------
Total Due: EUR 1,250.00
"""

invoice_no = re.search(r"Invoice No:\s+(\S+)", simulated_text).group(1)
supplier = re.search(r"(Global Tech Ltd\.)", simulated_text).group(1)
invoice_date = re.search(r"Invoice Date:\s+(\d{4}-\d{2}-\d{2})", simulated_text).group(1)
total_amount = re.search(r"Total Due:\s+EUR\s+([\d,]+\.\d{2})", simulated_text).group(1)
total_amount_clean = float(total_amount.replace(",", ""))

df = pd.DataFrame([{
    "Invoice No": invoice_no,
    "Supplier": supplier,
    "Date": invoice_date,
    "Total Amount (EUR)": total_amount_clean
}])

df.to_csv("extracted_invoices.csv", index=False)
print("Invoice data extracted and saved to extracted_invoices.csv")
