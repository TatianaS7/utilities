# This script extracts the text from each page of a PDF file and filters the pages based on the presence of target text.
# If a page contains any of the target texts, it is included in the output PDF. 
# Otherwise, it is skipped.

import pytesseract
import re
import io
from PIL import Image
import fitz


# Extract Text from Page
def extract_text(page):
    text = page.get_text()
    if not text.strip():
        pix = page.get_pixmap()
        image_data = pix.tobytes("png")
        img = Image.open(io.BytesIO(image_data))
        text = pytesseract.image_to_string(img)
    return text


# Check if page contains target text
def contains_target_text(text):
    target_texts = [
        "Target Text 1",
        "Target Text 2",
        "Target Text 3"
    ]

    for target in target_texts:
        if re.search(target, text, re.IGNORECASE):
            return True
    
    return False


# Filter Pages by Text
def filter_pages(input_pdf, output_pdf):
    try:
        doc = fitz.open(input_pdf)
        output = fitz.open()

        for page_num in range(len(doc)):
            page = doc[page_num]

            text = extract_text(page)

            if contains_target_text(text):
                output.insert_pdf(doc, from_page=page_num, to_page=page_num)
                print(f"Page {page_num + 1} contains target text and was included")
            else:
                print(f"Page {page_num + 1} does not contain target text and was skipped")

        # Save Output PDF
        output.save(output_pdf)
        print(f"Output PDF saved to {output_pdf}")
    
    except Exception as e:
        print(f"Error: {e}")