from fastapi import FastAPI
from app.schemas import ExtractRequest, ExtractResponse
from app.services import extract_information

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Structured Output Extractor API is running"}


@app.post("/extract", response_model=ExtractResponse)
def extract_data(request: ExtractRequest):
    return extract_information(request.text)