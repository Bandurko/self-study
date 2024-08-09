from tkinter import *

import speedtest


def test():
    speed_test = speedtest.Speedtest()
    download_speed = round(speed_test.download() / (1024 ** 2), 2)
    upload_speed = round(speed_test.upload() / (1024 ** 2), 2)

    download_lable.config(text="Скорость загрузки:\n-" + str(download_speed) + "MbPs")
    upload_lable.config(text="Скорость отдачи:\n-" + str(upload_speed) + "MbPs")

root = Tk()

root.title("SpeedTest")
root.geometry("300x400")

button = Button(root, text="Измерить скорость", font=40, command=test)
button.pack(side=BOTTOM, pady=40)

download_lable = Label(root, text="Скорость загрузки:\n-", font=35)
download_lable.pack(pady=(50, 0))
upload_lable = Label(root, text="Скорость отдачи:\n-", font=35)
upload_lable.pack(pady=(10, 0))

root.mainloop()