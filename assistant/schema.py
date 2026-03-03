from pydantic import BaseModel, Field


class AssistantResponse(BaseModel):
    answer: str = Field(..., description="Main response text")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score between 0 and 1")