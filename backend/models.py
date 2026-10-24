
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String, text
from database import Base


class Sach(Base):
    __tablename__ = "sach"

    id = Column(Integer, primary_key=True, index=True)
    ma_sach = Column(String(30), unique=True, nullable=False)
    ten_sach = Column(String(200), nullable=False)
    tac_gia = Column(String(150), nullable=False)
    the_loai = Column(String(100), nullable=True)
    nam_xuat_ban = Column(Integer, nullable=True)
    so_luong = Column(Integer, nullable=False, server_default=text("0"))
    ngay_tao = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class DocGia(Base):
    __tablename__ = "doc_gia"

    id = Column(Integer, primary_key=True, index=True)
    ma_doc_gia = Column(String(30), unique=True, nullable=False)
    ho_ten = Column(String(150), nullable=False)
    email = Column(String(255), unique=True, nullable=True)
    so_dien_thoai = Column(String(20), nullable=True)
    ngay_tao = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class PhieuMuon(Base):
    __tablename__ = "phieu_muon"

    id = Column(Integer, primary_key=True, index=True)
    ma_phieu = Column(String(30), unique=True, nullable=False)
    doc_gia_id = Column(Integer, ForeignKey("doc_gia.id"), nullable=False)
    ngay_muon = Column(Date, nullable=False, server_default=text("CURRENT_DATE"))
    han_tra = Column(Date, nullable=False)
    trang_thai = Column(String(30), nullable=False, server_default=text("'dang_muon'"))
    ngay_tao = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class ChiTietPhieuMuon(Base):
    __tablename__ = "chi_tiet_phieu_muon"

    id = Column(Integer, primary_key=True, index=True)
    phieu_muon_id = Column(
        Integer,
        ForeignKey("phieu_muon.id", ondelete="CASCADE"),
        nullable=False,
    )
    sach_id = Column(Integer, ForeignKey("sach.id"), nullable=False)
    so_luong = Column(Integer, nullable=False, server_default=text("1"))
    ngay_tra_thuc_te = Column(Date, nullable=True)
