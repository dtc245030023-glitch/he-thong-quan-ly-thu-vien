# Hệ thống quản lý thư viện

## 1. Giới thiệu
Xây dựng website quản lý thư viện sử dụng React, FastAPI và PostgreSQL, triển khai bằng Docker Compose.

## 2. Công nghệ
- Frontend: React, Vite
- Backend: Python, FastAPI, SQLAlchemy
- Database: PostgreSQL 17
- Quản lý database: pgAdmin 4
- Reverse proxy: Nginx
- Giám sát: Prometheus, Grafana
- Logging: Loki, Promtail
- Triển khai: Docker Compose

## 3. Cấu trúc dự án
- backend/: mã nguồn API
- frontend/: giao diện website
- monitoring/: cấu hình giám sát và logging
- nginx/: cấu hình reverse proxy
- docker-compose.yml: cấu hình triển khai
- .gitignore: loại trừ file riêng tư

## 4. Cài đặt
Cần cài Docker Desktop và Git.

## 5. Cấu hình môi trường
Tạo file .env tại thư mục gốc, khai báo POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, PGADMIN_DEFAULT_EMAIL và PGADMIN_DEFAULT_PASSWORD.

Không đưa file .env lên GitHub.

## 6. Khởi chạy
Tại thư mục gốc, chạy:

    docker compose config --quiet
    docker compose up -d --build
    docker compose ps

## 7. Địa chỉ truy cập
- Website: http://localhost:8080
- Backend: http://localhost:8000
- API sách: http://localhost:8080/api/sach
- pgAdmin: http://localhost:5050
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000
- Loki: http://localhost:3100

## 8. Nginx và bảo mật
Nginx chuyển tiếp yêu cầu API đến FastAPI và yêu cầu giao diện đến frontend. Các header bảo mật gồm X-Content-Type-Options, X-Frame-Options, Referrer-Policy và Permissions-Policy.

Hiện tại hệ thống sử dụng HTTP trên localhost; HTTPS chưa được cấu hình.

## 9. Giám sát và logging
Prometheus thu thập chỉ số theo cấu hình. Grafana hiển thị dữ liệu giám sát. Promtail thu thập log và Loki lưu trữ, hỗ trợ truy vấn bằng LogQL.

Ví dụ truy vấn LogQL, tùy theo nhãn thực tế:
- {container="library_backend"}
- {container="library_nginx"}
- {container="library_backend"} |= "ERROR"

## 10. Kiểm tra
    docker compose ps
    docker compose exec nginx nginx -t
    curl.exe -i http://localhost:8080/api/sach

## 11. Bảo vệ dữ liệu
PostgreSQL lưu dữ liệu trong volume postgres_data. Không xóa volume nếu chưa sao lưu dữ liệu cần giữ. Không công khai mật khẩu trên GitHub.

## 12. Thông tin sinh viên
- Họ tên: Bùi Doãn Minh
- Mã sinh viên: Bổ sung mã sinh viên
- Lớp: Bổ sung lớp
- Học phần: Bổ sung tên học phần
