import logging

from fastapi import APIRouter, Body
from starlette.responses import Response

from service.native_form_service import form_template_service, form_posting_service, check_native_health

native_form_router = APIRouter()


@native_form_router.get("/native/health", tags=["native", "health"])
def health():
    return check_native_health()


@native_form_router.get("/native/form/{id}", tags=["form", "native"])
def get_form_by_id(id: int, response: Response):
    response.headers["Content-Type"] = "application/json"
    return form_template_service(id)


@native_form_router.post("/native/form", tags=["form", "native"], status_code=201)
async def post_form_by_number(body=Body(...), response=Response):
    logging.info(f"Body: {body}")
    return await form_posting_service(json_body=body)