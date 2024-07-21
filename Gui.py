import tkinter as ttk
from tkinter import filedialog
from main import get_info_by_ip
import re


def open_file():
    file_path = filedialog.askopenfilename(
        title="Выберете файл с IP-адресами", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open('report.txt', 'w', encoding='UTF-8') as f:
            with open(file_path, "r", encoding='UTF-8') as file:
                ip_lst = re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', file.read())
                for ip in ip_lst:
                    get_info_by_ip(ip=ip.strip())
                    open('report.txt', 'a', encoding='UTF-8').write("_____________________________ \n")
            f.close()
        root.destroy()


# Create the main window
root = ttk.Tk()
root.geometry("350x250+450+150")
root.title("Откройте файл с IP-адресами")
root.iconbitmap(default="img.ico")

# Create a button to open the file
open_button = ttk.Button(root, text="Открыть файл", command=open_file)
open_button.place(relx=.5, rely=.8, anchor="c")

# Run the Tkinter event loop
root.mainloop()
