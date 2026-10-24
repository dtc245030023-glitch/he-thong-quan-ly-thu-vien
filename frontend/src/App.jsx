
import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "/api";
function App() {
  const [sach, setSach] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [form, setForm] = useState({
    ma_sach: "",
    ten_sach: "",
    tac_gia: "",
    the_loai: "",
    nam_xuat_ban: "",
    so_luong: 1,
  });

  async function taiDanhSachSach() {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(`${API_URL}/sach`);
      if (!response.ok) throw new Error("Không thể tải danh sách sách.");
      const data = await response.json();
setSach(Array.isArray(data) ? data : (data.value ?? []));
    } catch {
      setError("Không kết nối được API. Hãy kiểm tra backend đang chạy.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    taiDanhSachSach();
  }, []);

  function capNhatForm(event) {
    setForm({ ...form, [event.target.name]: event.target.value });
  }

  async function themSach(event) {
    event.preventDefault();
    setError("");

    try {
      const response = await fetch(`${API_URL}/sach`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          ...form,
          nam_xuat_ban: form.nam_xuat_ban
            ? Number(form.nam_xuat_ban)
            : null,
          so_luong: Number(form.so_luong),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.detail || "Không thể thêm sách.");
      }

      setForm({
        ma_sach: "",
        ten_sach: "",
        tac_gia: "",
        the_loai: "",
        nam_xuat_ban: "",
        so_luong: 1,
      });

      await taiDanhSachSach();
      alert("Thêm sách thành công!");
    } catch (err) {
      setError(err.message || "Không kết nối được API.");
    }
  }

  return (
    <main className="container">
      <header className="header">
        <div>
          <p className="eyebrow">HỆ THỐNG QUẢN LÝ</p>
          <h1>Thư viện</h1>
          <p className="subtitle">
            Quản lý sách và theo dõi kho sách của thư viện.
          </p>
        </div>
        <div className="book-icon" aria-hidden="true">📚</div>
      </header>

      <section className="stats">
        <div className="stat-card">
          <span>Tổng đầu sách</span>
          <strong>{sach.length}</strong>
        </div>
        <div className="stat-card">
          <span>Tổng số cuốn</span>
          <strong>
            {sach.reduce((total, item) => total + item.so_luong, 0)}
          </strong>
        </div>
      </section>

      <section className="panel">
        <h2>Thêm sách mới</h2>
        <form className="book-form" onSubmit={themSach}>
          <label>
            Mã sách *
            <input
              name="ma_sach"
              value={form.ma_sach}
              onChange={capNhatForm}
              required
              maxLength={30}
              placeholder="VD: SACH002"
            />
          </label>

          <label>
            Tên sách *
            <input
              name="ten_sach"
              value={form.ten_sach}
              onChange={capNhatForm}
              required
              maxLength={200}
              placeholder="Nhập tên sách"
            />
          </label>

          <label>
            Tác giả *
            <input
              name="tac_gia"
              value={form.tac_gia}
              onChange={capNhatForm}
              required
              maxLength={150}
              placeholder="Nhập tên tác giả"
            />
          </label>

          <label>
            Thể loại
            <input
              name="the_loai"
              value={form.the_loai}
              onChange={capNhatForm}
              maxLength={100}
              placeholder="VD: Công nghệ thông tin"
            />
          </label>

          <label>
            Năm xuất bản
            <input
              name="nam_xuat_ban"
              type="number"
              min="0"
              max="2100"
              value={form.nam_xuat_ban}
              onChange={capNhatForm}
              placeholder="VD: 2025"
            />
          </label>

          <label>
            Số lượng *
            <input
              name="so_luong"
              type="number"
              min="0"
              value={form.so_luong}
              onChange={capNhatForm}
              required
            />
          </label>

          <button type="submit">+ Thêm sách</button>
        </form>

        {error && <p className="error">{error}</p>}
      </section>

      <section className="panel">
        <div className="table-heading">
          <div>
            <h2>Danh sách sách</h2>
            <p className="subtitle">Dữ liệu được lấy từ PostgreSQL.</p>
          </div>
          <button className="secondary-button" onClick={taiDanhSachSach}>
            Làm mới
          </button>
        </div>

        {loading ? (
          <p>Đang tải dữ liệu...</p>
        ) : sach.length === 0 ? (
          <p>Chưa có sách trong thư viện.</p>
        ) : (
          <div className="table-wrap">
            <table>
              <thead>
                <tr>
                  <th>Mã sách</th>
                  <th>Tên sách</th>
                  <th>Tác giả</th>
                  <th>Thể loại</th>
                  <th>Năm XB</th>
                  <th>Số lượng</th>
                </tr>
              </thead>
              <tbody>
                {sach.map((item) => (
                  <tr key={item.id}>
                    <td>{item.ma_sach}</td>
                    <td>{item.ten_sach}</td>
                    <td>{item.tac_gia}</td>
                    <td>{item.the_loai || "—"}</td>
                    <td>{item.nam_xuat_ban || "—"}</td>
                    <td><span className="quantity">{item.so_luong}</span></td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

      <footer>Hệ thống Quản lý Thư viện · Đồ án CNTT</footer>
    </main>
  );
}

export default App;
