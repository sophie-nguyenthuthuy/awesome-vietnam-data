# Bộ dữ liệu khởi đầu / Starter datasets

Các bộ dữ liệu nhỏ, sạch, sẵn dùng về Việt Nam. Tất cả ở định dạng CSV, mã hóa UTF-8 (NFC), phân cách bằng dấu phẩy, dấu thập phân là dấu chấm.

## 📁 Danh sách

### `tinh-thanh-vietnam-2025.csv`

34 đơn vị hành chính cấp tỉnh của Việt Nam sau sắp xếp năm 2025 (Nghị quyết 202/2025/QH15, hiệu lực từ 12/06/2025; chính quyền mới hoạt động từ 01/07/2025). Gồm 28 tỉnh và 6 thành phố.

| Cột | Mô tả |
|---|---|
| `stt` | Số thứ tự |
| `ten` | Tên đơn vị hành chính |
| `loai` | Tỉnh / Thành phố |
| `mien` | Bắc / Trung / Nam |
| `sap_nhap_tu` | Các đơn vị cũ hợp thành (hoặc "Giữ nguyên") |
| `dien_tich_km2` | Diện tích tự nhiên (km²) |
| `dan_so` | Quy mô dân số (người) |
| `nguon_dan_so` | Nguồn số liệu của dòng đó |

**Lưu ý về nguồn số liệu:** 23 đơn vị hình thành sau sắp xếp dùng số liệu chính thức trong Nghị quyết 202/2025/QH15 (cột `nguon_dan_so` = `NQ 202/2025/QH15`). 11 đơn vị giữ nguyên dùng số liệu Tổng cục Thống kê (`GSO 2023`). Hai nguồn có phương pháp tính khác nhau — không nên cộng trực tiếp để ra tổng dân số cả nước.

Nguồn: [Chinhphu.vn — Chi tiết 34 đơn vị hành chính cấp tỉnh](https://xaydungchinhsach.chinhphu.vn/chi-tiet-34-don-vi-hanh-chinh-cap-tinh-tu-12-6-2025-119250612141845533.htm)

### `ngay-le-vietnam-2026.csv`

Các ngày nghỉ lễ chính thức năm 2026 theo Điều 112 Bộ luật Lao động 2019, kèm ngày âm lịch và ghi chú nghỉ bù.

Nguồn: [Chinhphu.vn — Lịch nghỉ lễ năm 2026](https://xaydungchinhsach.chinhphu.vn/lich-nghi-le-gio-to-hung-vuong-30-4-1-5-quoc-khanh-2-9-nam-2026-119260222115822151.htm)

## Giấy phép

Số liệu gốc thuộc nguồn công khai của Nhà nước Việt Nam; phần biên soạn phát hành theo [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
