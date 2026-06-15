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

### `kinh-te-vietnam-1960-2024.csv`

Chuỗi thời gian dân số và GDP Việt Nam theo World Bank (World Development Indicators, cập nhật 04/2026).

| Cột | Mô tả |
|---|---|
| `nam` | Năm |
| `dan_so` | Dân số (SP.POP.TOTL) |
| `gdp_usd` | GDP danh nghĩa, USD hiện hành (NY.GDP.MKTP.CD), làm tròn về USD |
| `gdp_tang_truong_pct` | Tăng trưởng GDP thực, % (NY.GDP.MKTP.KD.ZG), làm tròn 2 chữ số |

**Lưu ý:** GDP trống trước 1985. Các giá trị USD giai đoạn 1985–1990 biến động mạnh do chế độ tỷ giá thời kỳ trước Đổi mới — dùng cột tăng trưởng thực để phân tích giai đoạn này.

Nguồn: [World Bank Open Data](https://data.worldbank.org/country/vietnam) (CC BY-4.0)

### `tet-nguyen-dan-2025-2035.csv`

Ngày mùng 1 Tết Nguyên đán (dương lịch) và can chi từng năm, 2025–2035. Tính theo âm lịch quy ước; âm lịch Việt Nam (UTC+7) hiếm khi lệch 1 ngày so với lịch tính theo UTC+8 — nên đối chiếu thông báo chính thức cho từng năm khi dùng cho nghiệp vụ.

### `chi-so-phat-trien-2000-2023.csv`

Chỉ số phát triển 2000–2023 theo World Bank: lạm phát CPI (%), tuổi thọ trung bình (năm), tỷ lệ dùng Internet (% dân số), tỷ lệ dân thành thị (% dân số). Nguồn: [World Bank Open Data](https://data.worldbank.org/country/vietnam) (CC BY-4.0).

### `dan-toc-vietnam-2019.csv`

54 dân tộc được Nhà nước công nhận, kèm dân số theo Tổng điều tra dân số 2019 và nhóm ngôn ngữ (theo phân loại 8 nhóm / 3 ngữ hệ). Sắp xếp theo dân số giảm dần; tổng cộng 96.205.082 người. Nguồn dân số: [Tổng cục Thống kê — Tổng điều tra 2019](https://www.nso.gov.vn).

### `di-san-the-gioi-unesco.csv`

9 Di sản Thế giới UNESCO tại Việt Nam (6 văn hóa, 2 tự nhiên, 1 hỗn hợp) kèm năm công nhận, mã hồ sơ UNESCO và tỉnh, thành theo địa giới 2025. Nguồn: [UNESCO World Heritage Centre — Viet Nam](https://whc.unesco.org/en/statesparties/vn) (qua Wikipedia).

### `ty-gia-vnd-usd-1995-2024.csv`

Tỷ giá VND/USD bình quân năm 1995–2024 (World Bank, PA.NUS.FCRF — tỷ giá chính thức, bình quân kỳ). VND mất giá khoảng 2,2 lần so với USD trong giai đoạn này. Nguồn: [World Bank Open Data](https://data.worldbank.org/country/vietnam) (CC BY-4.0).

### `song-ngoi-vietnam.csv`

16 con sông lớn kèm chiều dài tổng (km), chiều dài đoạn chảy trên lãnh thổ Việt Nam, lưu vực và nơi đổ ra. Sắp xếp theo chiều dài giảm dần. Với sông quốc tế (Mê Kông, Hồng, Đà…) cột `chieu_dai_km` là tổng chiều dài, `chieu_dai_vn_km` là phần trong nước. Nguồn: tổng hợp từ Wikipedia (các bài về từng sông) và Britannica (Mê Kông).

### `vuon-quoc-gia-vietnam.csv`

34 vườn quốc gia kèm năm thành lập, vùng (Bắc/Trung/Nam) và diện tích (ha). Sắp xếp theo năm thành lập. Một số diện tích phản ánh lần mở rộng gần nhất (vd Phong Nha – Kẻ Bàng sau mở rộng 2013); chưa gồm VQG Bát Xát (Lào Cai, lập 2026). Nguồn: [Wikipedia — Danh sách vườn quốc gia tại Việt Nam](https://vi.wikipedia.org/wiki/Danh_sách_vườn_quốc_gia_tại_Việt_Nam).

### `san-bay-vietnam.csv`

Các sân bay dân dụng đang khai thác (11 quốc tế, 12 nội địa) kèm mã IATA/ICAO và tỉnh, thành theo địa giới 2025; thêm Long Thành (đang xây dựng). Nguồn: tổng hợp từ ICAO/IATA qua [Wikipedia — List of airports in Vietnam](https://en.wikipedia.org/wiki/List_of_airports_in_Vietnam).

### `ngay-le-vietnam-2026.csv`

Các ngày nghỉ lễ chính thức năm 2026 theo Điều 112 Bộ luật Lao động 2019, kèm ngày âm lịch và ghi chú nghỉ bù.

Nguồn: [Chinhphu.vn — Lịch nghỉ lễ năm 2026](https://xaydungchinhsach.chinhphu.vn/lich-nghi-le-gio-to-hung-vuong-30-4-1-5-quoc-khanh-2-9-nam-2026-119260222115822151.htm)

## Giấy phép

Số liệu gốc thuộc nguồn công khai của Nhà nước Việt Nam và World Bank (CC BY-4.0); phần biên soạn phát hành theo [CC0](https://creativecommons.org/publicdomain/zero/1.0/).
