from fastapi import APIRouter, Request
from app.extension import templates

router = APIRouter()

@router.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request,             
        "index.html",
        {"request": request}
    )

@router.post('/submit')
async def submit(request: Request):
    data = await request.json

    name = data.get('name')
    message = data.get('message')

    return {"status":"ok"}