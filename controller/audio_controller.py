from fastapi import APIRouter, UploadFile, File

from service.audio_service import check_health, apply_speech_to_text

html_form_router = APIRouter()


@html_form_router.get("/audio/health", tags=["form", "html", "health"])
async def health():
    return await check_health()


@html_form_router.post("/audio", tags=["form", "html", "audio"])
async def translate(audio: UploadFile = File(...)):
    response = await apply_speech_to_text(audio)
    return response
