from Backend.src.parser_perscription import PerscriptionParser
import pytest

@pytest.fixture()
def document_1_Virat():
    text = '''Dr John >mith, M.D
    2 Non-Important street,
    New York, Phone (900)-323- ~2222
    
    Name:  Virat Kohli Date: 2/05/2022
    
    Address: 2 cricket blvd, New Delhi
    
    | Omeprazole 40 mg
    
    Directions: Use two tablets daily for three months
    
    Refill: 3 times'''
    return PerscriptionParser(text)

@pytest.fixture()
def document_2_Marta():
    text = '''Dr John Smith, M.D
    2 Non-Important Street,
    New York, Phone (000)-111-2222
    
    Name: Marta Sharapova Date: 5/11/2022
    
    Address: 9 tennis court, new Russia, DC
   
    Prednisone 20 mg
    Lialda 2.4 gram
    
    Directions:
    
    Prednisone, Taper 5 mg every 3 days, Finish in 2.5 weeks a Lialda - take 2 pill everyday for 1 month
    
    Refill: 2 times'''
    return PerscriptionParser(text)

@pytest.fixture()
def document_3_empty():
    return PerscriptionParser(" ")

def test_get_name(document_1_Virat, document_2_Marta, document_3_empty):
    assert document_1_Virat.get_filed("patient_name") == "Virat Kohli"
    assert document_2_Marta.get_filed("patient_name") == "Marta Sharapova"
    assert  document_3_empty.get_filed("patient_name") == None

def test_get_address(document_1_Virat, document_2_Marta, document_3_empty):
    assert document_1_Virat.get_filed("patient_address") == "2 cricket blvd, New Delhi"
    assert document_2_Marta.get_filed("patient_address") == "9 tennis court, new Russia, DC"
    assert document_3_empty.get_filed("patient_address") == None

def test_get_medicine(document_1_Virat, document_2_Marta, document_3_empty):
    assert document_1_Virat.get_filed("medicine") == "| Omeprazole 40 mg"
    assert document_2_Marta.get_filed("medicine") == "Prednisone 20 mg\n    Lialda 2.4 gram"
    assert document_3_empty.get_filed("medicine") == None

def test_get_direction(document_1_Virat, document_2_Marta, document_3_empty):
    assert document_1_Virat.get_filed("directions") == "Use two tablets daily for three months"
    assert document_2_Marta.get_filed("directions") == "Prednisone, Taper 5 mg every 3 days, Finish in 2.5 weeks a Lialda - take 2 pill everyday for 1 month"
    assert document_3_empty.get_filed("directions") == None

def test_get_refill(document_1_Virat, document_2_Marta, document_3_empty):
    assert document_1_Virat.get_filed("refill") == "3"
    assert document_2_Marta.get_filed("refill") == "2"
    assert document_3_empty.get_filed("refill") == None

def test_parser(document_1_Virat, document_2_Marta, document_3_empty):
    assert document_1_Virat.parse() == {
        'patient_name': 'Virat Kohli',
        'patient_address': '2 cricket blvd, New Delhi',
        'medicine': "| Omeprazole 40 mg",
        'directions':"Use two tablets daily for three months",
        'refill':'3'
    }

    assert document_2_Marta.parse() == {
        'patient_name': "Marta Sharapova",
        'patient_address': "9 tennis court, new Russia, DC",
        'medicine': "Prednisone 20 mg\n    Lialda 2.4 gram",
        'directions': "Prednisone, Taper 5 mg every 3 days, Finish in 2.5 weeks a Lialda - take 2 pill everyday for 1 month",
        'refill': '2'
    }

    assert document_3_empty.parse() == {
        'patient_name': None,
        'patient_address': None,
        'medicine': None,
        'directions': None,
        'refill': None
    }
