from tkinter import *

import speedtest


def test():
    speed_test = speedtest.Speedtest()
    download_speed = round(speed_test.download() / (1024 ** 2), 2)
    upload_speed = round(speed_test.upload() / (1024 ** 2), 2)
    servernames =[]
    speed_test.get_servers(servernames)
    ping_ms = speed_test.results.ping

    download_lable.config(text="Скорость загрузки:\n" + str(download_speed) + "MbPs")
    upload_lable.config(text="Скорость отдачи:\n" + str(upload_speed) + "MbPs")
    ping_lable.config(text="Ping:\n" + str(ping_ms) + "ms")

root = Tk()

root.title("SpeedTest")
root.geometry("300x400")

button = Button(root, text="Измерить скорость", font=40, command=test)
button.pack(side=BOTTOM, pady=40)

download_lable = Label(root, text="Скорость загрузки:\n-", font=35)
download_lable.pack(pady=(50, 0))
upload_lable = Label(root, text="Скорость отдачи:\n-", font=35)
upload_lable.pack(pady=(10, 0))
ping_lable = Label(root, text="Ping:\n-", font=35)
ping_lable.pack(pady=(10, 0))

root.mainloop()