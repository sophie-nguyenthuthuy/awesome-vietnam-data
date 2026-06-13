#!/usr/bin/env python3
"""Quickstart: nạp các bộ dữ liệu trong data/ và in vài thống kê nhanh.

Chỉ dùng thư viện chuẩn (csv) — không cần cài thêm gì.
    python examples/quickstart.py
"""
import csv
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    tinh = load("tinh-thanh-vietnam-2025.csv")
    print(f"Số đơn vị hành chính cấp tỉnh: {len(tinh)}")

    # Tỉnh/thành đông dân nhất
    dong_nhat = max(tinh, key=lambda r: int(r["dan_so"]))
    print(f"Đông dân nhất: {dong_nhat['ten']} "
          f"({int(dong_nhat['dan_so']):,} người)")

    # Tỉnh/thành rộng nhất
    rong_nhat = max(tinh, key=lambda r: float(r["dien_tich_km2"]))
    print(f"Rộng nhất: {rong_nhat['ten']} "
          f"({float(rong_nhat['dien_tich_km2']):,.0f} km²)")

    # GDP & dân số mới nhất
    kt = load("kinh-te-vietnam-1960-2024.csv")
    moi = kt[-1]
    print(f"\nNăm {moi['nam']}: dân số {int(moi['dan_so']):,}, "
          f"GDP {float(moi['gdp_usd'])/1e9:,.0f} tỷ USD, "
          f"tăng trưởng {moi['gdp_tang_truong_pct']}%")

    # Internet
    cs = load("chi-so-phat-trien-2000-2023.csv")
    print(f"Tỷ lệ dùng Internet: {cs[0]['nam']} = "
          f"{cs[0]['ty_le_dung_internet_pct']}% → "
          f"{cs[-1]['nam']} = {cs[-1]['ty_le_dung_internet_pct']}%")

    # Tết năm nay/sắp tới
    tet = load("tet-nguyen-dan-2025-2035.csv")
    print("\n3 Tết sắp tới:")
    for r in tet[:3]:
        print(f"  {r['nam']} ({r['can_chi']}): "
              f"mùng 1 = {r['mung_1_tet_duong_lich']} ({r['thu']})")


if __name__ == "__main__":
    main()
