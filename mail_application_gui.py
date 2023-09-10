import tkinter as tk
import smtplib
from tkinter import messagebox

def send_email():
    sender_email = sender_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end-1c")

    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, password_entry.get())
        email_message = f"Subject: {subject}\n\n{message}"
        smtp_server.sendmail(sender_email, receiver_email, email_message)
        smtp_server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


window = tk.Tk()
window.title("Email Application")


sender_label = tk.Label(window, text="Your Email:")
sender_label.pack()
sender_entry = tk.Entry(window)
sender_entry.pack()


password_label = tk.Label(window, text="Your Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Receiver Email
receiver_label = tk.Label(window, text="Recipient's Email:")
receiver_label.pack()
receiver_entry = tk.Entry(window)
receiver_entry.pack()

# Subject
subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

# Message
message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=5, width=40)
message_text.pack()

# Send Button
send_button = tk.Button(window, text="Send Email", command=send_email)
send_button.pack()

# Run the GUI application
window.mainloop()
