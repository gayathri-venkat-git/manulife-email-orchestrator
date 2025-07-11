from api.app import app
import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

# api/app.py
from fastapi import FastAPI, UploadFile, File
from modules.control_flow_agent import orchestrate_email

app = FastAPI()

@app.post("/process_email/")
async def process_email(file: UploadFile = File(...)):
    content = await file.read()
    result = orchestrate_email(content)
    return result
