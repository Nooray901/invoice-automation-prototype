
README - Invoice Processing Automation Prototype
------------------------------------------------

Student Name: [Raazia Liaqat]
Student ID: [x23405970]
Course Name: Intelligent Agents and Process Automation

------------------------------------------------
Project Overview:
------------------------------------------------
This prototype demonstrates the automation of invoice intake and data extraction, which forms the first critical step in an invoice processing workflow. The system captures an invoice, applies Optical Character Recognition (OCR) to extract key fields (invoice number, supplier, date, total), and saves the structured data into a CSV file.

------------------------------------------------
Folder Contents:
------------------------------------------------
1. invoice_automation.py              - Python script to extract invoice data from simulated text (OCR output).
2. Sample_Invoice_INV-00834.pdf       - Sample input invoice used for testing.
3. extracted_invoices.csv             - Output file containing extracted invoice data in structured format.
4. invoice_extraction_screenshot.png  - Screenshot showing the extracted data table.

------------------------------------------------
Prerequisites:
------------------------------------------------
To run the Python script, ensure you have the following installed:

1. Python 3.x
2. Required Python Libraries:
   - pandas
   - re (Regular Expressions - built-in)
   - pytesseract
   - Pillow (PIL)

Install libraries via pip:
pip install pandas pytesseract pillow

You must also install the Tesseract OCR engine on your machine:

- For macOS:
brew install tesseract

- For Windows, download from:
https://github.com/tesseract-ocr/tesseract/wiki

------------------------------------------------
How to Run the Prototype:
------------------------------------------------
1. Ensure Tesseract OCR is installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the folder containing `invoice_automation.py`.
4. Run the script:
python invoice_automation.py
5. The extracted data will be saved to `extracted_invoices.csv` in the same folder.

------------------------------------------------
Contact:
------------------------------------------------
For any questions regarding this prototype, please contact:
[x23405970@student.ncirl.ie]

