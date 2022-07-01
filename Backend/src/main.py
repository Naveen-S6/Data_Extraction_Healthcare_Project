from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from Extractor import extract
import uuid
import os
app = FastAPI()

@app.post('/extract_text')
async def extract_text(
        file_type: str = Form(...),
        file: UploadFile = File(...)
):

    content = file.file.read()
    file_path = "../Uploads"+str(uuid.uuid4())+".pdf"
    with open(file_path, "wb") as f:
        f.write(content)

    try:
        data = extract(file_path, file_type)
    except Exception as e:
        data = {
            'error': str(e)
        }

    if os.path.exists(file_path):
        os.remove(file_path)

    return data

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)