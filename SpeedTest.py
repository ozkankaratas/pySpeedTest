import speedtest
import os
test = speedtest.Speedtest()

print("Loading Server List...")
test.get_servers()
print("Choosing the best server...")
best = test.get_best_server()

print(f"Server Name: {best['host']} \Country : {best['country']}")

print("Testing the download speed...")
download_result = test.download()
print("Testing the upload speed...")
upload_result = test.upload()
ping_result = test.results.ping

clear = lambda: os.system('cls')
clear()

print(f"Download Speed : {download_result / 1024 / 1024:.2f}Mbit/s")
print(f"Upload Speed : {upload_result / 1024 / 1024:.2f}Mbit/s")
print(f"Ping : {ping_result}ms")
input('Press ENTER for close...')
