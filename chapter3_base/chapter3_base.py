import time
time.sleep(5)
for i in range(1,101):
    print(f'\r下载进度{i * 1}%', end='',flush=True)
    time.sleep(0.1)