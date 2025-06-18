yosh = int(input("Yoshingizni kriting: "))
Narx = int(input("Chipta narxini kriting: "))
if 0 <= yosh <= 6:
    chegirma1 = Narx*0.5
    print(f"Siz uchun chipta narxi 50% chegirmada: {chegirma1} so'm")
if 7 <= yosh <= 17:
    chegirma2 = Narx*0.8
    print(f"Siz uchun chipta narxi 20% chegirmada: {chegirma2} so'm")
if 17 <= yosh <= 60:
    print(f"Siz uchun chegirma yo'q chipta narxi: {Narx} so'm")
if 60 <= yosh:
    chegirma3 = Narx*0.7
    print(f"Siz uchun chipta narxi 30% chegirmada: {chegirma3} so'm")