# This script converts a TIFF file to a PDF file using the Python Imaging Library (PIL). 
# The script reads the TIFF file and converts each page to a PIL image object. 
# It then saves the PIL images as a PDF file using the save method. 

from PIL import Image, ImageSequence
import logging

def convert_tiff_to_pdf(input_path, output_path):
    try:
        img = Image.open(input_path)
        pdf_path = output_path.with_suffix('.pdf')

        pages = []
        for page in ImageSequence.Iterator(img):
            img_page = page.convert('RGB')
            pages.append(img_page)

        if pages:
            pages[0].save(pdf_path, save_all=True, append_images=pages[1:], resolution=200.0)
        
        logging.info(f"Converted {input_path} to {pdf_path}")
        print(f"Converted {input_path} to {pdf_path}")
        return pdf_path
    except Exception as e:
        logging.error(f"An error occurred while converting {input_path} to PDF: {e}")
        print(f"An error occurred while converting {input_path} to PDF: {e}")
        return None
    

if __name__ == "__main__":
    input_path = ""
    output_path = ""

    convert_tiff_to_pdf(input_path, output_path)
