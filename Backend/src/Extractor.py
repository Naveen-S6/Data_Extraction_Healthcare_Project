from pdf2image import convert_from_path
import Util
import pytesseract
from parser_patient_details import PatientDetailsParser
from parser_perscription import PerscriptionParser
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
Poppler_path = r"D:\Naveen\OCR_Healthcare_Project\poppler-22.04.0\Library\bin"

def extract(file_path, file_type):
    pages = convert_from_path(file_path, poppler_path=Poppler_path)
    document_text = ""
    for page in pages:
        processed_image = Util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang="eng")
        document_text += '\n' + text

    if file_type == "prescription":
        extracted_data = PerscriptionParser(document_text).parse()
    elif file_type == "patient_details":
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid file type: {file_type}")
    return extracted_data

if __name__ == "__main__":
    pp = extract("../Resources/patient_details/pd_2.pdf", "patient_details")
    print(pp)