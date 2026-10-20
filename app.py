print("=" * 40)
print("       SIRKET FINANS RAPORU")
print("=" * 40)

# 1. Aylik gelir ve giderler
ciro = 11000000
personel_gideri = 2500000
elektrik_sgk = 1000000
kira = 300000
Ham_madde = ciro *40/100
yemek_gideri = 150000
diger_giderler = 500000

# 2. Toplam gideri hesapla
toplam_gider = (
    personel_gideri
    + elektrik_sgk
    + kira
    + yemek_gideri
    + diger_giderler+ Ham_madde
)

# 3. Faaliyet sonucunu hesapla
faaliyet_sonucu = ciro - toplam_gider

# 4. Kar marjini hesapla
kar_marji = faaliyet_sonucu / ciro * 100

# 5. Raporu ekrana yazdir
print("Aylik ciro:", format(ciro, ","))
print("Toplam gider:", format(toplam_gider, ","))
print("Faaliyet sonucu:", format(faaliyet_sonucu, ","))
print("Kar marji: %", round(kar_marji, 2))

# 6. Finansal durum yorumu
print("-" * 40)

if faaliyet_sonucu > 0:
    print("SONUC: Gelirler giderlerden yuksek.")
elif faaliyet_sonucu < 0:
    print("UYARI: Sirket zarar ediyor.")
else:
    print("SONUC: Sirket basa bas noktasinda.")

print("=" * 40)

