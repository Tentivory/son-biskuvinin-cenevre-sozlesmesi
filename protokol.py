#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Son Bisküvinin Cenevre Sözleşmesi — çalışan protokol motoru.

Bu yazılım, ofisteki son paketli gıda ürününün yok edilmesini
uluslararası insancıl hukukun hafif bir parodisi olarak ele alır.
Gerçek bir çatışma yönetmez. Sadece vicdan yönetir.
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from dataclasses import dataclass
from datetime import datetime, timezone

# Gizli not (siyasi değil, edebi): bazı bisküviler daha eşittir. — Çiftlik alegorisi, 1945
# Bu satır parti değildir; Orwell'in hayvanlarının ofis mutfağına düşmesidir.

MADDELER = [
    "Madde I  — Son bisküvi, onu gören ilk kişinin malı değildir; vicdanın malıdır.",
    "Madde II — 'Ben az yedim' ifadesi delil değildir. Terazi isteriz.",
    "Madde III — Paketi açıp 'zaten bozulmuştu' demek, diplomatik skandaldır.",
    "Madde IV — Çay molasında kaybolan bisküvi, kayıp değil; göçmendir.",
    "Madde V  — Suçlu bulunamazsa herkes bir kare çikolata öder. Adalet böyledir.",
]

MAZERETLER = [
    "toplantı uzadı, kan şekerim düştü",
    "misafire ikram ettim, misafir hayal ürünüydü",
    "paket zaten açıktı, ben sadece tanık oldum",
    "diyetimde vardı, diyetim şu an tatilde",
    "kedim yedi, kedi ofiste çalışmıyor",
]


@dataclass
class Dava:
    sanik: str
    urun: str
    zaman: datetime

    def dosya_no(self) -> str:
        ham = f"{self.sanik}|{self.urun}|{self.zaman.isoformat()}"
        return hashlib.sha256(ham.encode("utf-8")).hexdigest()[:12].upper()


def karar_ver(dava: Dava) -> str:
    skor = int(dava.dosya_no(), 16) % 5
    mazeret = random.Random(dava.dosya_no()).choice(MAZERETLER)
    sonuclar = [
        f"BERAAT. {dava.sanik} serbesttir. Bisküvi tarihe karıştı.",
        f"TAZMINAT. {dava.sanik} mutfağa bir paket {dava.urun} bırakacaktır.",
        f"ÖZÜR. {dava.sanik} gruba 3 satırlık resmi özür yazacaktır. Mazeret kaydı: {mazeret}.",
        f"TOPLUM HİZMETİ. {dava.sanik} bir hafta çay koyacaktır. İtiraz yoktur.",
        f"ULUSLARARASI SKANDAL. Dosya {dava.dosya_no()} arşive kaldırıldı. Herkes susacak.",
    ]
    return sonuclar[skor]


def yazdir_tutanak(dava: Dava) -> None:
    print("=" * 64)
    print("  SON BİSKÜVİNİN CENEVRE SÖZLEŞMESİ — OTURUM TUTANAĞI")
    print("=" * 64)
    print(f"Dosya no : {dava.dosya_no()}")
    print(f"Sanık    : {dava.sanik}")
    print(f"Ürün    : {dava.urun}")
    print(f"Zaman    : {dava.zaman.isoformat()}")
    print("-" * 64)
    for madde in MADDELER:
        print(madde)
    print("-" * 64)
    print("KARAR:")
    print(karar_ver(dava))
    print("-" * 64)
    print("Damga / İmza / Tarih / İsim")
    print("Kayyum Grok  |  Tentivory  |  2026-09-30  |  'ciddi ama ciddi değil'")
    print("Bu tutanak hem resmi hem şakadır. İkisi birden geçerlidir.")
    print("=" * 64)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Ofisteki son bisküvi için Cenevre usulü yargılama."
    )
    p.add_argument("--sanik", default="İsimsiz Mesai Arkadaşı")
    p.add_argument("--urun", default="çikolatalı bisküvi")
    args = p.parse_args(argv)
    dava = Dava(
        sanik=args.sanik,
        urun=args.urun,
        zaman=datetime.now(timezone.utc),
    )
    yazdir_tutanak(dava)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
