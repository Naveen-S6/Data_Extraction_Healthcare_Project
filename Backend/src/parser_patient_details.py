from Backend.src.parser_generic import MedicalDocumentParser
import re

class PatientDetailsParser(MedicalDocumentParser):
    def __init__(self, text):
        MedicalDocumentParser.__init__(self, text)

    def parse(self):
        return {
            "patient_name" : self.get_patient_name(),
            "phone_number" : self.get_phone_number(),
            "Hepatitis status": self.get_hepatitis_status(),
            "medical problems":self.get_medical_problems()
        }

    def get_patient_name(self):
        name_pattern = "Birth Date(.*?)\(\d{3}\)"
        name_match = re.findall(name_pattern, self.text, flags=re.DOTALL)
        if name_match:
            name = self.remove_noise_from_name(name_match[0])
            return name

    def remove_noise_from_name(self, name):
        name = name.strip()
        date_pattern = '((Jan|April|Feb|March|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[ \d+]*)'
        date_match = re.findall(date_pattern, name)
        if date_match:
            name = name.replace(date_match[0][0], "").strip()

        return name

    def get_phone_number(self):
        phone_num_pattern = "Patient Information.*?(\(\d{3}\) \d{3}-\d{4})"
        phone_num_match = re.findall(phone_num_pattern, self.text, flags=re.DOTALL)
        if phone_num_match:
            return phone_num_match[0].strip()

    def get_hepatitis_status(self):
        hepatitis_pattern = "Have you had the Hepatitis B vaccination\?.*?(Yes|No)"
        hepatitis_status_match = re.findall(hepatitis_pattern, self.text, flags=re.DOTALL)
        if hepatitis_status_match:
            return hepatitis_status_match[0].strip()

    def get_medical_problems(self):
        medi_prob_pattern = "List any Medical Problems (\(|\{)asthma, seizures, headaches(\)|\}):(.*?)(‘Name|Name)"
        medi_prob_match = re.findall(medi_prob_pattern, self.text, flags=re.DOTALL)
        if medi_prob_match:
            return medi_prob_match[0][2].strip()

if __name__ == "__main__":
    text = '''17/12/2020

        Patient Medical Record

        Patient Information Birth Date

        Kathy Crawford May 6 1972

        (737) 988-0851 Weight’

        9264 Ash Dr 95

        New York City, 10005 '

        United States Height:
        190

        In Case of Emergency
        ee J
        Simeone Crawford 9266 Ash Dr
        New York City, New York, 10005
        Home phone United States
        (990) 375-4621
        Work phone
        Genera! Medical History
        nn ee
        Chicken Pox (Varicella): Measies:
        IMMUNE

        IMMUNE
        Have you had the Hepatitis B vaccination?

        No

        List any Medical Problems (asthma, seizures, headaches}:

        Migraine.

        ‘Name of Insurance Company:

        Random Insuarance Company - 4789 Bollinger Rd
        Jersey City, New Jersey, 07030

        a Policy Number:
        71 1520731 3 Expiry Date:

        . 30 December 2020
        Do you have medical insurance?

        Yes:

        Medical Insurance Details

        List any allergies:

        Peanuts

        List any medication taken regularly:
        Triptans'''
    pd = PatientDetailsParser(text)
    print(pd.parse())
