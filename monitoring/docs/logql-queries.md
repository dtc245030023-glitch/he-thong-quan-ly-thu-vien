# Các truy vấn LogQL kiểm thử hệ thống quản lý thư viện

## 1. Toàn bộ log Backend
```logql
{container="library_backend"}
```

## 2. Lọc log ERROR
```logql
{container="library_backend"} |= "ERROR"
```

Kết quả: Không tìm thấy log ERROR trong khoảng thời gian đã kiểm tra.

## 3. Lọc log GET
```logql
{container="library_backend"} |= "GET"
```

Kết quả: Đã thấy log GET /metrics trả về HTTP 200 OK.
