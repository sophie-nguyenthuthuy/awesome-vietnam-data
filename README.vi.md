# Awesome Vietnam Data 🇻🇳 [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Danh sách chọn lọc các bộ dữ liệu mở, API và công cụ dữ liệu về Việt Nam — dành cho kỹ sư dữ liệu, nhà phân tích, nhà nghiên cứu và người xây dựng sản phẩm.

*Biên soạn bởi [@sophie-nguyenthuthuy](https://github.com/sophie-nguyenthuthuy). Hoan nghênh PR — xem [Đóng góp](#đóng-góp). English version: [README.md](README.md).*

## Mục lục

- [Dữ liệu trong repo này](#dữ-liệu-trong-repo-này)
- [Cơ quan nhà nước](#cơ-quan-nhà-nước)
- [Kinh tế & Tài chính](#kinh-tế--tài-chính)
- [Dữ liệu không gian](#dữ-liệu-không-gian)
- [Xử lý ngôn ngữ tiếng Việt (NLP)](#xử-lý-ngôn-ngữ-tiếng-việt-nlp)
- [Môi trường & Thời tiết](#môi-trường--thời-tiết)
- [Dân số & Phát triển](#dân-số--phát-triển)
- [Công cụ & Thư viện](#công-cụ--thư-viện)
- [Lưu ý khi làm việc với dữ liệu Việt Nam](#lưu-ý-khi-làm-việc-với-dữ-liệu-việt-nam)

## Dữ liệu trong repo này

Thư mục [`data/`](data/) chứa các bộ dữ liệu CSV nhỏ, sạch, sẵn dùng:

- [`tinh-thanh-vietnam-2025.csv`](data/tinh-thanh-vietnam-2025.csv) — 34 tỉnh, thành phố sau sắp xếp 2025 (NQ 202/2025/QH15): diện tích, dân số, các đơn vị hợp thành.
- [`kinh-te-vietnam-1960-2024.csv`](data/kinh-te-vietnam-1960-2024.csv) — dân số, GDP và tăng trưởng GDP 1960–2024 (World Bank).
- [`chi-so-phat-trien-2000-2023.csv`](data/chi-so-phat-trien-2000-2023.csv) — lạm phát CPI, tuổi thọ, tỷ lệ dùng Internet 2000–2023 (World Bank).
- [`di-san-the-gioi-unesco.csv`](data/di-san-the-gioi-unesco.csv) — 9 Di sản Thế giới UNESCO kèm năm công nhận và mã hồ sơ.
- [`dan-toc-vietnam-2019.csv`](data/dan-toc-vietnam-2019.csv) — 54 dân tộc kèm dân số (điều tra 2019) và nhóm ngôn ngữ.
- [`vuon-quoc-gia-vietnam.csv`](data/vuon-quoc-gia-vietnam.csv) — 34 vườn quốc gia kèm năm thành lập, vùng và diện tích.
- [`ty-gia-vnd-usd-1995-2024.csv`](data/ty-gia-vnd-usd-1995-2024.csv) — tỷ giá VND/USD bình quân năm 1995–2024 (World Bank).
- [`song-ngoi-vietnam.csv`](data/song-ngoi-vietnam.csv) — 16 con sông lớn kèm chiều dài, lưu vực và nơi đổ ra.
- [`san-bay-vietnam.csv`](data/san-bay-vietnam.csv) — sân bay dân dụng kèm mã IATA/ICAO theo địa giới 2025.
- [`tet-nguyen-dan-2025-2035.csv`](data/tet-nguyen-dan-2025-2035.csv) — ngày mùng 1 Tết và can chi 2025–2035.
- [`ngay-le-vietnam-2026.csv`](data/ngay-le-vietnam-2026.csv) — ngày nghỉ lễ chính thức 2026, kèm âm lịch và nghỉ bù.

Chi tiết nguồn và lưu ý: [`data/README.md`](data/README.md).

## Cơ quan nhà nước

- [Tổng cục Thống kê (GSO)](https://www.gso.gov.vn) — thống kê chính thức: CPI, GDP, dân số, thương mại, công nghiệp. Công bố theo tháng/quý/năm; nhiều bảng tải về được.
- [Cổng Dữ liệu mở Quốc gia](https://data.gov.vn) — cổng dữ liệu mở quốc gia; các bộ ngành và địa phương công bố dữ liệu tại đây.
- [Ngân hàng Nhà nước (SBV)](https://www.sbv.gov.vn) — tỷ giá, lãi suất, thống kê tiền tệ, số liệu tổ chức tín dụng.
- [Cổng đăng ký doanh nghiệp quốc gia](https://dangkykinhdoanh.gov.vn) — tra cứu đăng ký kinh doanh.
- [Hải quan Việt Nam](https://www.customs.gov.vn) — thống kê xuất nhập khẩu theo mặt hàng và đối tác.

## Kinh tế & Tài chính

- [World Bank — Việt Nam](https://data.worldbank.org/country/vietnam) — hàng trăm chỉ số vĩ mô, API sạch, chuỗi thời gian dài.
- [IMF Data — Việt Nam](https://data.imf.org) — cán cân thanh toán, tài chính công, chuỗi IFS.
- [ADB — Key Indicators](https://www.adb.org/what-we-do/data/statistics) — chỉ số so sánh được trong toàn ASEAN.
- [Sở GDCK TP.HCM (HOSE)](https://www.hsx.vn) — niêm yết, chỉ số, công bố thông tin.
- [Sở GDCK Hà Nội (HNX)](https://www.hnx.vn) — dữ liệu thị trường HNX/UPCoM.
- [vnstock (Python)](https://github.com/thinh-vu/vnstock) — thư viện Python lấy dữ liệu chứng khoán Việt Nam.

## Dữ liệu không gian

- [OpenStreetMap Việt Nam (Geofabrik)](https://download.geofabrik.de/asia/vietnam.html) — bản trích xuất OSM đầy đủ, cập nhật hằng ngày; nguồn geodata chủ lực cho VN.
- [GADM — ranh giới hành chính Việt Nam](https://gadm.org) — polygon ranh giới tỉnh/huyện/xã.
- [HDX — Việt Nam](https://data.humdata.org/group/vnm) — dữ liệu nhân đạo: ranh giới hành chính, lưới dân số, hạ tầng.
- [WorldPop — Việt Nam](https://www.worldpop.org) — ước lượng dân số dạng lưới (độ phân giải 100m).

## Xử lý ngôn ngữ tiếng Việt (NLP)

- [PhoBERT](https://github.com/VinAIResearch/PhoBERT) — BERT tiền huấn luyện cho tiếng Việt (VinAI); baseline tiêu chuẩn.
- [underthesea](https://github.com/undertheseanlp/underthesea) — bộ công cụ NLP tiếng Việt: tách từ, POS, NER, phân tích cảm xúc.
- [VnCoreNLP](https://github.com/vncorenlp/VnCoreNLP) — tách từ, POS, NER, phân tích phụ thuộc.
- [VLSP](https://vlsp.org.vn) — bộ dữ liệu và benchmark của cộng đồng Xử lý ngôn ngữ và tiếng nói tiếng Việt.
- [Hugging Face — bộ dữ liệu tiếng Việt](https://huggingface.co/datasets?language=language:vi) — danh mục corpus và benchmark tiếng Việt, lọc được.

## Môi trường & Thời tiết

- [IQAir — chất lượng không khí Việt Nam](https://www.iqair.com/vietnam) — AQI thời gian thực các thành phố VN (có API).
- [OpenAQ](https://openaq.org) — dữ liệu chất lượng không khí mở, gồm các trạm tại Việt Nam, có API.
- [Trung tâm Dự báo KTTV Quốc gia (NCHMF)](https://nchmf.gov.vn) — thời tiết, thủy văn, cảnh báo bão.
- [Open-Meteo](https://open-meteo.com) — API thời tiết miễn phí phủ VN, không cần key; hợp cho pipeline và giảng dạy.

## Dân số & Phát triển

- [UN Data — Việt Nam](https://data.un.org) — chỉ số của hệ thống thống kê Liên Hợp Quốc.
- [DHS Program — khảo sát Việt Nam](https://dhsprogram.com) — vi dữ liệu y tế và nhân khẩu học (cần đăng ký).
- [UNICEF MICS](https://mics.unicef.org) — khảo sát đa chỉ số, gồm Việt Nam.
- [Our World in Data](https://ourworldindata.org) — biểu đồ + chuỗi dữ liệu VN tải về được về y tế, năng lượng, giáo dục.

## Công cụ & Thư viện

- [vnstock](https://github.com/thinh-vu/vnstock) — dữ liệu thị trường chứng khoán (đã liệt kê ở trên).
- [underthesea](https://github.com/undertheseanlp/underthesea) / [pyvi](https://github.com/trungtv/pyvi) — xử lý văn bản tiếng Việt.
- [inflation-crawler](https://github.com/sophie-nguyenthuthuy/data-engineering/tree/main/inflation-crawler) — crawler CPI/lạm phát VN → DuckDB → FastAPI (thuộc monorepo DE của mình).
- [savings-rate-engine](https://github.com/sophie-nguyenthuthuy/data-engineering/tree/main/savings-rate-engine) — thu thập & chuẩn hóa lãi suất tiết kiệm ngân hàng VN.

## Lưu ý khi làm việc với dữ liệu Việt Nam

Vài kinh nghiệm xương máu cho kỹ sư dữ liệu:

- **Mã hóa ký tự**: file cũ có thể dùng TCVN3 hoặc VNI thay vì UTF-8; luôn dò mã hóa trước khi parse. Chuẩn hóa Unicode rất quan trọng — cùng một chữ có thể ở dạng NFC hoặc NFD (`ế` là một codepoint, hoặc `e` + hai dấu kết hợp). Chuẩn hóa về NFC ngay khi nhập liệu.
- **Tên & địa chỉ**: họ đứng trước tên; hệ thống tỉnh/huyện/xã thay đổi theo thời gian (sáp nhập hành chính diễn ra thường xuyên — từ 07/2025 cả nước còn 34 tỉnh, thành và bỏ cấp huyện; hãy giữ bảng dimension đơn vị hành chính có phiên bản theo ngày).
- **Con số**: số tiền VND rất lớn — dùng int 64-bit, tuyệt đối không dùng float; nhiều nguồn dùng dấu `.` ngăn cách hàng nghìn và dấu `,` thập phân.
- **Ngày tháng**: `dd/mm/yyyy` là phổ biến nhất; các ngày lễ âm lịch (Tết) thay đổi hằng năm và ảnh hưởng lớn đến tính mùa vụ trong chuỗi thời gian.

## Đóng góp

Tìm thấy nguồn hay, hoặc link hỏng? Mở PR — mỗi mục một dòng, định dạng `[Tên](url) — mô tả ngắn (có gì trong đó, cách truy cập)`. Nguồn phải truy cập hợp pháp; không nhận dump cào từ các trang có ToS cấm.

## Giấy phép

[CC0](https://creativecommons.org/publicdomain/zero/1.0/) — hiến tặng vào phạm vi công cộng.
