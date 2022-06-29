from Backend.src.parser_generic import MedicalDocumentParser
import re
class PerscriptionParser(MedicalDocumentParser):
    def __init__(self, text):
        MedicalDocumentParser.__init__(self, text)

    def parse(self):
        return {
            'patient_name':self.get_filed('patient_name'),
            'patient_address':self.get_filed('patient_address'),
            'medicine':self.get_filed('medicine'),
            'directions':self.get_filed('directions'),
            'refill':self.get_filed('refill')
        }
    def get_filed(self, filed_name):
        pattern_dic ={
            "patient_name":{'pattern': 'Name:(.*)Date', 'flags':0},
            "patient_address": {'pattern': 'Address:(.*)\n', 'flags': 0},
            "medicine": {'pattern': 'Address:[^\n]*(.*)Directions', 'flags': re.DOTALL},
            "directions": {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            "refill": {'pattern': 'Refill:.*(\d+).times', 'flags': 0},
        }
        pattern_object = pattern_dic[filed_name]
        if pattern_object:
            matches = re.findall(pattern_object['pattern'], self.text, flags=pattern_object["flags"])
            if matches:
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
    pp = PerscriptionParser(text)
    print(pp.parse())
