from pydantic import BaseModel, Field, validator
from typing import List, Optional

class TranslationRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000, description="Text to translate (up to 1000 characters)")
    target_language: str = Field(..., min_length=2, max_length=5, description="Target language ISO code (e.g., ta, hi, kn, bn)")
    
    @validator('target_language')
    def validate_language_code(cls, v):
        # Simple validation for language code format
        if not v.isalpha():
            raise ValueError("Language code must contain only alphabetic characters")
        return v.lower()

class TranslationResponse(BaseModel):
    original_text: str
    translated_text: str
    target_language: str

class BulkTranslationRequest(BaseModel):
    texts: List[str] = Field(..., description="List of texts to translate")
    target_language: str = Field(..., min_length=2, max_length=5, description="Target language ISO code")
    
    @validator('texts')
    def validate_texts(cls, v):
        if not v:
            raise ValueError("At least one text must be provided")
        for text in v:
            if len(text) > 1000:
                raise ValueError(f"Each text must be at most 1000 characters (found {len(text)})")
        return v
    
    @validator('target_language')
    def validate_language_code(cls, v):
        if not v.isalpha():
            raise ValueError("Language code must contain only alphabetic characters")
        return v.lower()

class BulkTranslationResponse(BaseModel):
    translations: List[TranslationResponse]

class HealthResponse(BaseModel):
    status: str
    version: str
    timestamp: str