import tkinter as tk
from MailOperations import MailOperations
from Page import Page


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        file = ""

        mesages = MailOperations("i.love.smtp.5785@gmail.com", "testSMTP$$").readMail()
        print(mesages)

        label = tk.Text(self, width="80", height="35")
        label.insert(tk.END, mesages)
        label.pack(expand=True)
