from fastapi import APIRouter, HTTPException, Depends
from app.models.schemas import TranslationRequest, TranslationResponse, BulkTranslationRequest, BulkTranslationResponse
from app.services.translator import translation_service
from app.utils.logger import log_request
from app.db.database import log_translation

router = APIRouter(prefix="/api/v1", tags=["translation"])

@router.post("/translate", response_model=TranslationResponse)
async def translate_text(request: TranslationRequest):
    """Translate a single text to the specified target language"""
    try:
        translated_text = await translation_service.translate_text(
            text=request.text,
            target_language=request.target_language
        )
        
        response = TranslationResponse(
            original_text=request.text,
            translated_text=translated_text,
            target_language=request.target_language
        )
        
        # Log the translation
        log_request(request.dict(), response.dict())
        await log_translation(
            source_text=request.text,
            target_language=request.target_language,
            translated_text=translated_text
        )
        
        return response
    
    except Exception as e:
        log_request(request.dict(), error=e)
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")

@router.post("/translate/bulk", response_model=BulkTranslationResponse)
async def translate_bulk(request: BulkTranslationRequest):
    """Translate multiple texts to the specified target language"""
    try:
        translated_texts = await translation_service.translate_bulk(
            texts=request.texts,
            target_language=request.target_language
        )
        
        translations = []
        for i, (original, translated) in enumerate(zip(request.texts, translated_texts)):
            translations.append(TranslationResponse(
                original_text=original,
                translated_text=translated,
                target_language=request.target_language
            ))
            
            # Log each translation
            await log_translation(
                source_text=original,
                target_language=request.target_language,
                translated_text=translated
            )
        
        response = BulkTranslationResponse(translations=translations)
        log_request(request.dict(), response.dict())
        
        return response
    
    except Exception as e:
        log_request(request.dict(), error=e)
        raise HTTPException(status_code=500, detail=f"Bulk translation failed: {str(e)}")