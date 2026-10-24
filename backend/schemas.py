
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class SachCreate(BaseModel):
    ma_sach: str = Field(min_length=1, max_length=30)
    ten_sach: str = Field(min_length=1, max_length=200)
    tac_gia: str = Field(min_length=1, max_length=150)
    the_loai: str | None = Field(default=None, max_length=100)
    nam_xuat_ban: int | None = Field(default=None, ge=0, le=2100)
    so_luong: int = Field(default=0, ge=0)


class SachResponse(SachCreate):
    model_config = ConfigDict(from_attributes=True)

    id: int
    ngay_tao: datetime
