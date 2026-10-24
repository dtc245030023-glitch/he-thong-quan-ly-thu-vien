
from datetime import datetime, timezone

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from prometheus_client import Counter, CONTENT_TYPE_LATEST, generate_latest
from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import Base, engine, get_db
import models
from models import Sach
from schemas import SachCreate, SachResponse

app = FastAPI(
    title="Hệ thống Quản lý Thư viện",
    description="API quản lý thư viện sử dụng PostgreSQL",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
)

REQUEST_COUNT = Counter(
    "library_api_requests_total",
    "Tong so request den API thu vien",
)


@app.middleware("http")
async def count_requests(request, call_next):
    REQUEST_COUNT.inc()
    response = await call_next(request)
    return response


@app.get("/")
def home():
    return {
        "message": "He thong Quan ly Thu vien dang hoat dong",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/health")
def health():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "healthy", "database": "connected"}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database connection failed",
        )


@app.get("/sach", response_model=list[SachResponse], tags=["Quản lý sách"])
def danh_sach_sach(db: Session = Depends(get_db)):
    return db.query(Sach).order_by(Sach.id.desc()).all()


@app.post(
    "/sach",
    response_model=SachResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Quản lý sách"],
)
def them_sach(du_lieu: SachCreate, db: Session = Depends(get_db)):
    sach = Sach(**du_lieu.model_dump())
    db.add(sach)

    try:
        db.commit()
        db.refresh(sach)
        return sach
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Mã sách đã tồn tại hoặc dữ liệu vi phạm ràng buộc.",
        )


@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(
        content=generate_latest(),
        media_type=CONTENT_TYPE_LATEST,
    )
