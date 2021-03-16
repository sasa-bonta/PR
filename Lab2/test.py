from tkinter import *
# from MailOperations import MailOperations


def send_message():
    address_info = str(address.get())
    subject_info = str(subject.get())
    email_body_info = str(email_body.get())

    print(address_info, subject_info, email_body_info)

    sender_email = "labexemplu@gmail.com"

    sender_password = "Damean.99"

    # server = smtplib.SMTP('smtp.gmail.com', 587)
    #
    # MailOperations(sender_password, sender_email).send_email(subject_info,
    #                                                          email_body_info,
    #                                                          address_info)

    address_entry.delete(0, END)
    subject_entry.delete(0, END)
    email_body_entry.delete(0, END)


# fereastra

app = Tk()

app.geometry("800x500")

app.title("Mini aplicația mea în Python!")

heading = Label(text="Mini aplicația mea în Python", bg="#454a52", fg="#c2c6cf", font="10", width="500", height="3")

heading.pack()

address_field = Label(text="Recipient Address :")
subject_field = Label(text="Subject :")
email_body_field = Label(text="Message :")

address_field.place(x=300, y=70)
subject_field.place(x=300, y=140)
email_body_field.place(x=300, y=210)

address = StringVar()
subject = StringVar()
email_body = StringVar()

address_entry = Entry(textvariable=address, width="30")
subject_entry = Entry(textvariable=subject, width="30")
email_body_entry = Entry(textvariable=email_body, width="30")

address_entry.place(x=300, y=100)
subject_entry.place(x=300, y=180)
email_body_entry.place(x=300, y=260)

button = Button(app, text="Send Message", command=send_message, width="30", height="2", bg="red")

button.place(x=150, y=310)


def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(app)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("800x500")

    # A Label widget to show in toplevel
    Label(newWindow,
          text="Inbox").pack()


btn = Button(app,
             text="Inbox",
             command=openNewWindow, width="30", height="2", bg="gray")
btn.place(x=400, y=310)


# def read_email_from_gmail():
#     mail = imaplib.IMAP4_SSL('imap.gmail.com')
#     mail.login('labexemplu@gmail.com', 'Damean.99')
#     mail.select('inbox')
#
#     result, data = mail.search(None, 'ALL')
#     mail_ids = data[0]
#
#     id_list = mail_ids.split()
#     first_email_id = int(id_list[0])
#     latest_email_id = int(id_list[-1])
#
#     for i in range(latest_email_id, first_email_id, -1):
#         # need str(i)
#         result, data = mail.fetch(str(i), '(RFC822)')
#
#         for response_part in data:
#             if isinstance(response_part, tuple):
#                 # from_bytes, not from_string
#                 msg = email.message_from_bytes(response_part[1])
#
#                 email_from = msg['from']
#                 print('From : ' + email_from + '\n')
#
#
# # nothing to print here
# read_email_from_gmail()

mainloop()
