from app.llm import extract_with_llm
from app.schema import ExtractResponse

def extract_information(text: str) -> ExtractResponse:
    result = extract_with_llm(text)

    return ExtractResponse(name = reult.get("name")
    company=result.get("company"),
    email=result.get("email"),
    role=result.get("role"))
    
            