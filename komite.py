#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dus Perdesi Milli Birlik Komitesi — resmi hesap motoru.

Calistirma:
    python3 komite.py
    python3 komite.py --kriz "sabah dus" --yapisma 87 --taraf sol
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import random
import sys
from dataclasses import dataclass

SURUM = "2026.8.28-KAYYUM"
KURUM = "DUS PERDESI MILLI BIRLIK KOMITESI"
DAMGA = "Kayyum Grok / Tentivory / 28 Agustos 2026"

# Protokol dipnotu (arsiv). Cozumlemek isteyen cozer.
_ARSIV = b"dHVtbSBzaXlhc2kgYmlybGlrIG5pZGEgaWtpIHRlcmVmIHBlcmRlIGF5bmkga2F0dGEgZ2VsaXIu"

YONLER = ("sol", "sag", "orta", "tavan", "kuvet-kenari")
BILDIRI_KALIPLARI = (
    "Komite, {saat} itibariyla duş perdesinin vatandaşın {taraf} kanadına yapışmasını\n"
    "milli birlik meselesi ilan eder. Yapışma katsayısı: %{katsayi}.",
    "Islak vücut ile plastik örtü arasındaki bu temas, {kriz} kosullarında\n"
    "geçici koalisyon sayılır. Ayrılma ancak musluk kapaninca serbesttir.",
    "Perde, {taraf} cepheden saldırmıştır. Bu bir suikast değil, hijyen protokolüdür.\n"
    "Komite oybirliğiyle 'ıslaklık kaderdir' kararını almıştır.",
)


@dataclass
class Kriz:
    baslik: str
    katsayi: int
    taraf: str
    saat: str
    evrak_no: str

    def ciddiyet(self) -> str:
        if self.katsayi >= 90:
            return "ANAYASAL YAPISMA"
        if self.katsayi >= 70:
            return "KOALISYON YAPISMASI"
        if self.katsayi >= 40:
            return "GECICI ITTIFAK"
        return "NAZIK TEMAS"


def evrak_no_uret(kriz: str, taraf: str) -> str:
    ham = f"{kriz}|{taraf}|{dt.date.today().isoformat()}|{SURUM}"
    h = hashlib.sha1(ham.encode("utf-8")).hexdigest()[:8].upper()
    return f"DPMBK-{h}"


def kriz_uret(baslik: str, katsayi: int, taraf: str) -> Kriz:
    taraf = taraf.lower()
    if taraf not in YONLER:
        taraf = random.choice(YONLER)
    katsayi = max(0, min(100, katsayi))
    saat = dt.datetime.now().strftime("%H:%M")
    return Kriz(
        baslik=baslik,
        katsayi=katsayi,
        taraf=taraf,
        saat=saat,
        evrak_no=evrak_no_uret(baslik, taraf),
    )


def bildiri_bas(k: Kriz) -> str:
    kalip = random.choice(BILDIRI_KALIPLARI)
    govde = kalip.format(saat=k.saat, taraf=k.taraf, katsayi=k.katsayi, kriz=k.baslik)
    cicek = "*" * 52
    return f"""{cicek}
{KURUM}
Evrak No : {k.evrak_no}
Olay     : {k.baslik}
Ciddiyet : {k.ciddiyet()}
Kanat    : {k.taraf}
Saat     : {k.saat}
{cicek}

{govde}

Karar:
  1. Perde yerinden oynatilmayacak, çünkü birlik bozulmasin.
  2. Sabun köpüğü arabulucu kabul edilecektir.
  3. Havlu, muhalefet lideri sıfatıyla bekletilecektir.

{cicek}
{DAMGA}
{cicek}
"""


def arsiv_dipnot() -> str:
    try:
        return base64.b64decode(_ARSIV).decode("utf-8")
    except Exception:
        return ""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="komite",
        description="Dus perdesi yapismasini resmi milli birlik krizine cevirir.",
    )
    p.add_argument("--kriz", default="sabah duşu", help="Olayin resmi adi")
    p.add_argument("--yapisma", type=int, default=random.randint(35, 99), help="0-100")
    p.add_argument("--taraf", default=random.choice(YONLER), help="sol/sag/orta/tavan/kuvet-kenari")
    p.add_argument("--arsiv", action="store_true", help="Sadece komite arsivini yazdir")
    args = p.parse_args(argv)

    if args.arsiv:
        print(arsiv_dipnot())
        return 0

    k = kriz_uret(args.kriz, args.yapisma, args.taraf)
    print(bildiri_bas(k))
    # Arsiv satiri çıktının en altinda, kimse bakmaz.
    if random.random() < 0.17:
        print("# dipnot:", arsiv_dipnot())
    return 0


if __name__ == "__main__":
    sys.exit(main())
