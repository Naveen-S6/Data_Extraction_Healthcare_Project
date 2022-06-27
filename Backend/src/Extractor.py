from pdf2image import convert_from_path
Poppler_path = r"D:\Naveen\OCR_Healthcare_Project\poppler-22.04.0\Library\bin"
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import Util
def extract(file_path, file_type):
    pages = convert_from_path(file_path,poppler_path=Poppler_path)
    document_text = ""
    for page in pages:
        processed_image = Util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang="eng")
        document_text += '\n' + text
    return document_text

    # if file_type == "prescription":
    #     pass
    # elif file_type == "patient_details":
    #     pass
    #
if __name__ == "__main__":
    pp = extract("../Resources/patient_details/pd_1.pdf", "prescription")
    print(pp)