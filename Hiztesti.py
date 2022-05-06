import speedtest
import os
test = speedtest.Speedtest()

print("Sunucu Listesi Yükleniyor...")
test.get_servers()
print("En iyi sunucu seçiliyor...")
best = test.get_best_server()

print(f"Sunucu Adı: {best['host']} \nBulunduğu Ülke : {best['country']}")

print("İndirme Hızı Test Ediliyor...")
download_result = test.download()
print("Yükleme Hızı Test Ediliyor...")
upload_result = test.upload()
ping_result = test.results.ping

clear = lambda: os.system('cls')
clear()

print(f"İndirme Hızınız : {download_result / 1024 / 1024:.2f}Mbit/s")
print(f"Yükleme Hızınız : {upload_result / 1024 / 1024:.2f}Mbit/s")
print(f"Ping : {ping_result}ms")
input('Çıkmak için ENTER tuşuna basınız...')