import pytest
from Backend.src.parser_patient_details import PatientDetailsParser

@pytest.fixture
def document_1_kathy():
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
    return PatientDetailsParser(text)

@pytest.fixture()
def document_2_jerry():
    text ='''Patient Medical Record
    
    Patient Information Birth Date
    
    Jerry Lucas May 2 1998
    
    (279) 920-8204 Weight:
    
    4218 Wheeler Ridge Dr 57
    
    Buffalo, New York, 14201 Height:
    
    United States gnt
    170
    
    In Case of Emergency
    
    - eee
    
    Joe Lucas . 4218 Wheeler Ridge Dr
    Buffalo, New York, 14201
    Home phone United States
    Work phone
    
    General Medical History
    
    Chicken Pox (Varicelia): Measles: ..
    
    IMMUNE NOT IMMUNE
    
    Have you had the Hepatitis B vaccination?
    
    ‘Yes
    
    | List any Medical Problems (asthma, seizures, headaches):
    N/A
    
    
    Name of Insurance Company:
    Random Insuarance Company
    
    Policy Number:
    5638746258
    
    Do you have medical insurance?
    
    _ Yes
    
    Medical Insurance Details
    
    List any allergies:
    N/A
    
    List any medication taken regularly:
    
    N/A
    
    4218 Smeeler Ridge Dr
    Buffalo, New York, 14206
    United States
    
    Expiry Date:
    31 December 2020
    '''
    return PatientDetailsParser(text)
@pytest.fixture()
def document_3_emptyp():
    text = " "
    return PatientDetailsParser(text)

def test_get_patient_name(document_1_kathy,document_2_jerry, document_3_emptyp):
    assert document_1_kathy.get_patient_name() == 'Kathy Crawford'
    assert document_2_jerry.get_patient_name() == 'Jerry Lucas'
    assert document_3_emptyp.get_patient_name() == None

def test_get_phone_number(document_1_kathy,document_2_jerry, document_3_emptyp):
    assert document_1_kathy.get_phone_number() == '(737) 988-0851'
    assert document_2_jerry.get_phone_number() == '(279) 920-8204'
    assert document_3_emptyp.get_phone_number() == None

def test_get_hepatitis_status(document_1_kathy,document_2_jerry, document_3_emptyp):
    assert document_1_kathy.get_hepatitis_status() == "No"
    assert document_2_jerry.get_hepatitis_status() == "Yes"
    assert document_3_emptyp.get_hepatitis_status() == None

def test_get_medical_problems(document_1_kathy,document_2_jerry, document_3_emptyp):
    assert document_1_kathy.get_medical_problems() == "Migraine."
    assert document_2_jerry.get_medical_problems() == "N/A"
    assert document_3_emptyp.get_medical_problems() == None

def test_parse(document_1_kathy,document_2_jerry, document_3_emptyp):
    doc = document_1_kathy.parse()

    assert doc["patient_name"] == "Kathy Crawford"
    assert doc["phone_number"] == '(737) 988-0851'
    assert doc["Hepatitis status"] == "No"
    assert doc["medical problems"] == "Migraine."

    do2 = document_2_jerry.parse()
    assert do2["patient_name"] == 'Jerry Lucas'
    assert do2["phone_number"] == '(279) 920-8204'
    assert do2["Hepatitis status"] == "Yes"
    assert do2["medical problems"] == "N/A"

    do3 = document_3_emptyp.parse()
    assert do3["patient_name"] == None
    assert do3["phone_number"] == None
    assert do3["Hepatitis status"] == None
    assert do3["medical problems"] == None