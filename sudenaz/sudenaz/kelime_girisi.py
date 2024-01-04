import sqlite3


conn = sqlite3.connect('ogrencinonuz.sqlite3')
cursor = conn.cursor()


conn.commit()

def kelime_girisi():
    while True:
        girilen_kelime = input("Girilecek kelimeyi giriniz: ").upper()

        if len(girilen_kelime) < 5:
            print("Kelime en az 5 harf içermeli. Tekrar deneyin.")
        else:
            print("Kelime başarıyla eklendi.")
            cursor.execute("INSERT INTO T_KELIME (kelime) VALUES (?)", (girilen_kelime,))
            conn.commit()

        kelime2 = input("Başka bir kelime girmek istiyor musunuz? (e/h) ").lower()
        if kelime2 != 'e':
            from oyun import oyunu_oyna
            oyunu_oyna()
            break

    conn.close()

kelime_girisi()
