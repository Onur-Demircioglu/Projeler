def sifrele():
    yazı=input("şifrelenecek metni gir")
    anahtar=int(input("anahtar değirini giriniz"))
    sifre=""
    for i in yazı:
        print(i,"=",chr(ord(i)+anahtar))
        a=chr(ord(i)+anahtar)
        sifre=sifre+a
    print(sifre)
    return sifre
"""
burda bir sezar şifreleme algoritması yaptık ord:karakterlerin
ascii deki numara karşılığını gösterir ve sonra bu numaraya eklenecek
anahtar değeri istenir bu anahtar değerinden sonra karakter girilen değer
kadar kaydırma yapılır
chr:ise ascii deki sayısal karşılığı karaktere çeviren komuttur
"""
def sifrecoz():
    sifremetin=input("şifresi çözülecek metni gir")
    anahtar=int(input("anahtar değirini giriniz"))
    cözüm=""
    for j in sifremetin:
        print(j,"=",chr(ord(j)-anahtar))
        a=chr(ord(j)-anahtar)
        cözüm=cözüm+a
    print(cözüm)
    return cözüm
"""
üstteki satırlarda metin şifrelenir bunu yaparkene harfler kaydırılır
alttaki satırlarda üstteki satırdan aldığı şifreli metni geri tersine bir işlem
yaparak kırar ve normal metne çevirir.
"""
#not:bu algoritmayı geliştir.
while(True):
    secim=int(input("1_ŞİFRELE:\n2_ŞİFREÇÖZ:\nSeçim yapınız:"))
    if secim==1:
        sifrele()
    elif secim==2:
        sifrecoz()

