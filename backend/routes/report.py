from fastapi import APIRouter
from fastapi.responses import FileResponse

from services.pdf_service import generate_pdf_report

router = APIRouter(
    prefix="/report",
    tags=["Report"]
)


@router.post("/")
def create_report(data: dict):

    pdf_path = generate_pdf_report(data)

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="medical_report.pdf"
    )