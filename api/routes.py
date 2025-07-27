# backend/api/routes.py

from fastapi import APIRouter, Request
from main_pipeline import run_pipeline

router = APIRouter()

@router.post("/run-pipeline")
async def run_pipeline_endpoint(request: Request):
    params = await request.json()
    result = run_pipeline(params)
    return result
