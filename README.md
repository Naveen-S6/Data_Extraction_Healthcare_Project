# OCR based Medical Data Extraction Project

I made this project by following codebasics python course, the link for the course is below. If you are interested checkout the link.

[Codebasics Python course](https://codebasics.io/courses/python-for-beginner-and-intermediate-learners)

## Problem statement

There are a lot of procedures needs to followed by the health insurance companies as per the government regulation to issue the claims, for that the insurance company has to process the images of patient details and prescription sent by hospitals or induvial doctors and extract useful data from them. For these process, the most insurance companies outsource workforce from companies like “Mr. X data Analytics” to extract the information from images manually. 

Mr. X data Analytics uses a software, which will show the scanned images of patient details or prescription, the person needs to type the information by seeing the image manually in the the right side column and select the type of information . As it is a manual process, error will be common and dealing with the huge set of images like in the pandemic time, will not be possible with the same amount of workforce. As well the Insurance companies has requested to send the data within 24hrs when it is send for extraction. All of these constraints forced, Mr. X data Analytics to consider for a software upgrade from their old software. 

## Solution approach

To solve all these problems, we are building a program which can do the extraction of data from images automatically. As always, machines can not replace humans. A person will recheck the extracted data and submit. So, that it will save a tremendous amount which was taken to type the data manually. 

Here, we are using the Python programming language and pytesseract google library for extracting the data and Regex module to process the data and get distilled desired output.


## Technologies used

- Python
- oops
- Pdf2image module
- Opencv
- pytesseract
- Regular expression
- pytest
- Postman
- FastApi

## Workflow

<img src="https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/blob/main/Backend/Notebooks/workflow.jpg" class = "center">

### PDF to Image

For converting PDF to image, we have used pdf2image library.

### Without preprocessing extracting data

Tried extracting data from source files without any processing, as they are not in proper format to be extracted, the extracted data was not as expected.

<img src="https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/blob/main/Backend/Notebooks/dark_image.jpg" width="350" class="center">

### Extracted data from the above image
```commandline
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Maria Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

—momennannenncmneneunnmnnnnninsissiyoinnitnahaadaanih issn earnttneenrenen:

Prednisone 20 mg
Lialda 2.4 gram

3 days,

or 1 month
```
---
### Image processing

we decided to preprocess the image using opencv module, before extracting data from them. For that we have first used normal thresholding and checked, which resulted in below image

<img src="https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/blob/main/Backend/Notebooks/filter_dark.jpg" width="350" class="center">


So, if there is any shadow or some noise, the normal thresholding fade out the area. which will result in loss of data. 

In the search of better approach of this problem, we have decided to use adaptive thresholding technique. In this technique, the image will be divided into sub image and the thresholding value will be different for all sub regions.
And the end result of adaptive thresholding is much better compared to normal thresholding.

<img src="https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/blob/main/Backend/Notebooks/adaptive_filter_dark.jpg" width="350" class='center'>

### After preprocessing the image data extraction

```commandline
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month
```
---
### Notebook

For all these above trials, used jupyter books and developed the small bits of the functionalities., which can be used later while designing the class.

[Notebooks](https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/tree/main/Backend/Notebooks)

---
### OOPS design

The code was written in using OOPs concepts for extracting the medical data from prescription and patient details documents.

[Code](https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/tree/main/Backend/src)

---
### Regular expression

using regular expression module we can match the patterns and extract the data we want from the files. For this project, 
analyst the medical files and as fact all the medical documents will follow same pattern, we wrote patterns that match only the required data.
Before writing the python code, It is advisable to practise and match the patterns in regex 101 website.

[regex101](https://regex101.com/)

---
### Test driven Development

In this project test driven development methodology was used to develop the code. For testing pytest module was used. 
For all the methods and final result the test cases was designed and checked simultaneously while developing the code.

[Test cases](https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/tree/main/Backend/Test)

---
### FastApi

Used FastAPI for hosting the server of the project. FastApi, as name suggest is help us to develop fast and some other advantages are,

- In build Data validation
- In build Documentation
- Fast running and performance

---
### Postman

As it is a backend project, not developed frontend part. For checking how the server responds for http requests, used postman to trigger http requests and tested the outcome.

<img src="https://github.com/Naveen-S6/Data_Extraction_Healthcare_Project/blob/main/Backend/Notebooks/postman.png" width="600" class="center">

---
## Result

This backend functionality can be integrated into the Mr.X Analytics existing software and data can be extracted automatically. 
The extracted data may have some errors, the person who is performing the work has to correct it and submit the response.

### Benefits

- Mr.X Analytics can save at least of 30 secs for each document. It is small amount of time when looking for one document, but cumulatively it can save a tremendous amount of time which can help the company to complete more documents within the given time and make more profit
- The company doesn't have to hire extra people in the season time.
- As it is a combination of automation and manual the error will be very much low.
