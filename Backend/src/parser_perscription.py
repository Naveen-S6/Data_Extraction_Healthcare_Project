from parser_generic import MedicalDocumentParser
import re
class PerscriptionParsr(MedicalDocumentParser):
    def __init__(self, text):
        MedicalDocumentParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name':self.get_name(),
            'patient_address':self.get_address(),
            'medicine':self.get_medicine(),
            'directions':self.get_direction(),
            'refill':self.get_refill()
        }

    def get_name(self):
        pattern = "Name:(.*)Date"
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()

    def get_address(self):
        pattern = "Address:(.*)\n"
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()

    def get_medicine(self):
        pattern = "Address:[^\n]*(.*)Directions"
        matches = re.findall(pattern, self.text, flags = re.DOTALL)
        if len(matches)>0:
            return matches[0].strip()

    def get_direction(self):
        pattern = "Directions:(.*)Refill"
        matches = re.findall(pattern, self.text, flags = re.DOTALL)
        if len(matches)>0:
            return matches[0].strip()

    def get_refill(self):
        pattern = "Refill:.*(\d+).times"
        matches = re.findall(pattern, self.text)
        if len(matches)>0:
            return matches[0].strip()



if __name__ == "__main__":
    text = '''Dr John >mith, M.D

2 Non-Important street,
New York, Phone (900)-323- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times'''
    pp = PerscriptionParsr(text)
    print(pp.parse())
