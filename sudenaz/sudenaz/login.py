import sqlite3


giris = sqlite3.connect('ogrencinonuz.sqlite3')
cursor = giris.cursor()

while True:
    kullanici = input("Kullanıcı Adı: ")
    sifre = input("Kullanıcı Şifre: ")

    cursor.execute("SELECT * FROM T_USERS WHERE kullanici=? AND sifre=?", (kullanici, sifre))
    user = cursor.fetchone()

    if user:
        kullanici_ismi, parola = user
        if kullanici_ismi == kullanici and parola == sifre:
         from menu import menu_bolumu
        menu_bolumu()
        break
    else:
        print("Hatalı kullanıcı adı veya şifre. Tekrar deneyin.")

giris.close()


