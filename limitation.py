import tkinter as tk
from main_frame import MainWindow

class LimitationWindow:
    def __init__(self):
        super().__init__()
        self.limit = tk.Tk()
        self.limit.title('Лінійне програмування')
        self.limit.geometry('400x270')
        self.limit.resizable(True, True)
        self.limit.config(bg='#DCF4FF')
        self.entry_var = tk.IntVar()

    def create_widgets(self):
        limits = tk.Label(self.limit, text='Введить кількість обмежень', background='#DCF4FF',
                          font=("Times New Roman", 16))
        lim_num = tk.Entry(self.limit, textvariable=self.entry_var, font=("Times New Roman", 11))
        next_btn = tk.Button(self.limit, text='Обчисліти', background='#DCF4FF', command=self.next_page,
                             font=("Times New Roman", 11))

        limits.place(relx=0.5, rely=0.2, anchor='center')
        lim_num.place(relx=0.5, rely=0.4, anchor='center')
        next_btn.place(relx=0.5, rely=0.7, anchor='center')

    def next_page(self):
        starting = MainWindow(self.entry_var.get())
        self.limit.withdraw()
        starting.create_widgets()
        starting.run()
        self.limit.destroy()

    def run(self):
        self.limit.mainloop()