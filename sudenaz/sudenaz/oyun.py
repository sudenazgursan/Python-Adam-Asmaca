import sqlite3
import random

def random_kelime():
    conn = sqlite3.connect('ogrencinonuz.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT kelime FROM T_KELIME ORDER BY RANDOM() LIMIT 1")
    kelime = cursor.fetchone()[0]
    conn.close()
    return kelime

def kelime_goster(kelime, tahmin_edilen_harfler):
    return " ".join(harf if harf in tahmin_edilen_harfler else "_" for harf in kelime)

def sekilbas(kalanHak):
    if kalanHak == 8:
        print("xxxxx")
        print("kalan hakkınız = " + str(kalanHak))

    elif kalanHak == 7:
        print("xxxxx")
        print("  |  ")
        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 6:
        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 5:
        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print(" /   ")
        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 4:
        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print(" / \\")
        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 3:
        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print(" / \\ ")

        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 2:
        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print(" / \\ ")
        print("  | ")
        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 1:
        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print(" / \\ ")
        print("  | ")
        print(" /  ")

        print("kalan hakkınız = " + str(kalanHak))
    elif kalanHak == 0:

        print("xxxxx")
        print("  |  ")
        print("  O  ")
        print(" / \\ ")
        print(" / \\ ")
        print("kalan hakkınız = " + str(kalanHak))


def oyunu_oyna():
    kelime_tahmin = random_kelime().upper()
    tahmin_edilen_harfler = set()
    yanlis_tahmin = 8
    joker_kullanildi = False

    print("Oyun başladı! Kelimeyi tahmin etmeye çalışın.")

    while 0 < yanlis_tahmin < 9:
        if not joker_kullanildi:
            joker_kullanimi = input("JOKER hakkınızı kullanmak ister misiniz? (E/H): ").upper()
            if joker_kullanimi == "E":
                joker_harf = random.choice(kelime_tahmin)
                tahmin_edilen_harfler.add(joker_harf)
                print(f"Jokeri kullandınız! Rastgele harf: {joker_harf}")
                joker_kullanildi = True
                continue

        sonuc = kelime_goster(kelime_tahmin, tahmin_edilen_harfler)
        print(f"Soru: {sonuc}")
        sekilbas(yanlis_tahmin)
        tahmin = input("Harf giriniz: ").upper()




        if tahmin.isalpha() and tahmin not in tahmin_edilen_harfler:
            tahmin_edilen_harfler.add(tahmin)
            if tahmin not in kelime_tahmin:
                yanlis_tahmin -= 1


            if set(kelime_tahmin) <= tahmin_edilen_harfler:
                    print(f"Tebrikler Kelimeyi doğru tahmin ettiniz. Kelime: {kelime_tahmin}")
                    break
    if set(kelime_tahmin) != tahmin_edilen_harfler:
        sekilbas(yanlis_tahmin)
        print(f"KAZANAMADINIZ. Doğru kelime: {kelime_tahmin}")


        menu_bolumu = input("MENUYE DONMEK İÇİN 1\nBITIRMEK İÇİN Q\nSeçiminizi yapınız:  ")

        if menu_bolumu == '1':
            print("Menüye dön.")
            from menu import menu_bolumu


        elif menu_bolumu == 'Q':
            print("Oyun bitti")



if oyunu_oyna() == "oyun":
 oyunu_oyna()
