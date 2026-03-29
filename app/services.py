from app.llm_clients import extract_with_llm
from app.schemas import ExtractResponse


def extract_information(text: str) -> ExtractResponse:
    result = extract_with_llm(text)

    return ExtractResponse(
        name=result.get("name"),
        company=result.get("company"),
        email=result.get("email"),
        role=result.get("role")
    )