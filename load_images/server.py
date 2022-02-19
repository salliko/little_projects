from pathlib import Path
from fastapi import FastAPI, File, UploadFile
from typing import List


app = FastAPI()


def save_file(filename, data):
    path = Path(__file__).parent
    with open(path.joinpath("files", filename), 'wb') as f:
        f.write(data)


@app.post("/upload-file/")
async def create_upload_file(files: List[UploadFile] = File(...)):
    for file in files:
        contents = await file.read()
        save_file(file.filename, contents)

    return {"Uploaded Filenames": [file.filename for file in files]}
