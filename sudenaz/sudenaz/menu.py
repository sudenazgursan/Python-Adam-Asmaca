
while True:
    print("ADAM ASMACA OYUNUNA HOSGELDINIZ")
    print("1-KELIME GIRISI")
    print("2-OYUN OYNA")
    print("3-PROGRAMI SONLANDIR")

    menu_bolumu = input("Seçiminizi yapınız: ")

    if menu_bolumu == '1':
        print("1-Kelime girişi seçildi.")
        from kelime_girisi import kelime_girişi

        kelime_girişi()

    elif menu_bolumu == '2':
        print("2-Oyun oyna seçildi.")
        from oyun import oyunu_oyna

        oyunu_oyna()


    elif menu_bolumu == '3':
        print("Program sonlandırıldı.")

        break
    else:
        print("Geçersiz seçim. Tekrar deneyin.")

