from scipy.optimize import linprog
import tkinter as tk


'''
Клас головного вікна програми
'''


class MainWindow:
    def __init__(self, limits_num):
        super().__init__()
        # Створення головного вікна Tkinter
        self.lottery = tk.Tk()
        self.lottery.title('Лінійне програмування')
        self.lottery.geometry('530x470')
        self.lottery.resizable(True, True)
        self.lottery.config(bg='#DCF4FF')
        self.limits = limits_num
        self.condition_entries = []
        self.MIN_MAX_var = tk.BooleanVar(self.lottery)
        self.error_label = tk.Label(self.lottery, fg="red", font=("Times New Roman", 16), bg='#DCF4FF', pady=15)
        self.error_label.pack(side=tk.BOTTOM)

    # Метод для створення віджетів на головному вікні
    def create_widgets(self):
        self.lottery.configure(bg='#DCF4FF')

        # Додавання заголовка "Головна функція"
        main_function_label = tk.Label(self.lottery, text='Головна функція', font=("Times New Roman", 16), bg='#DCF4FF')
        main_function_label.pack(pady=10)

        # Створення фрейму для введення A, B
        input_frame = tk.Frame(self.lottery, bg='#DCF4FF')
        input_frame.pack(pady=10)
        self.A_entr = tk.Entry(input_frame, width=5)
        self.B_entr = tk.Entry(input_frame, width=5)
        self.A_entr.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text='A', bg='#DCF4FF').pack(side=tk.LEFT, padx=5)
        self.B_entr.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text='B', bg='#DCF4FF').pack(side=tk.LEFT, padx=5)

        # Створення фрейму для MAX
        max_frame = tk.Frame(self.lottery, bg='#DCF4FF')
        max_frame.pack(pady=10)
        MIN_MAX_check = tk.Checkbutton(max_frame, variable=self.MIN_MAX_var, bg='#DCF4FF')
        MIN_MAX_check.pack(side=tk.LEFT, padx=5)
        tk.Label(max_frame, text='MAX', bg='#DCF4FF', font=("Times New Roman", 16)).pack(side=tk.LEFT, padx=5)

        # Фрейм для умов
        conditions_frame = tk.Frame(self.lottery, bg='#DCF4FF')
        conditions_frame.pack(pady=10)
        condition_lbl = tk.Label(conditions_frame, text='Обмеження', font=("Times New Roman", 16), bg='#DCF4FF')
        condition_lbl.pack()

        for i in range(self.limits):
            condition_frame = tk.Frame(conditions_frame, bg='#DCF4FF')
            condition_frame.pack()

            condition_X1 = tk.Entry(condition_frame, width=5)
            condition_X2 = tk.Entry(condition_frame, width=5)
            condition_const_x1 = tk.Label(condition_frame, width=5, text='x1', bg='#DCF4FF')
            condition_const_x2 = tk.Label(condition_frame, width=5, text='x2', bg='#DCF4FF')
            condition_EQ = tk.Label(condition_frame, text='<=', bg='#DCF4FF')
            condition_OP = tk.Label(condition_frame, text='+', bg='#DCF4FF')
            condition_S = tk.Entry(condition_frame, width=5)

            condition_X1.pack(side=tk.LEFT, padx=5)
            condition_const_x1.pack(side=tk.LEFT, padx=5)
            condition_OP.pack(side=tk.LEFT, padx=5)
            condition_X2.pack(side=tk.LEFT, padx=5)
            condition_const_x2.pack(side=tk.LEFT, padx=5)
            condition_EQ.pack(side=tk.LEFT, padx=5)
            condition_S.pack(side=tk.LEFT, padx=5)

            self.condition_entries.append((condition_X1, condition_X2, condition_S))
        decision_btn = tk.Button(self.lottery, text='Рішення', font=("Times New Roman", 16), command=self.calculate)
        decision_btn.pack(pady=10)

    # Метод для виконання розрахунків
    def calculate(self):
        try:
            if self.MIN_MAX_var.get() == True:
                c = [-1 * float(self.A_entr.get()), -1 * float(self.B_entr.get())]
            else:
                c = [float(self.A_entr.get()), float(self.B_entr.get())]
            A_arr = []
            b_arr = []
            for condition_X1, condition_X2, condition_S in self.condition_entries:
                A = [float(condition_X1.get()), float(condition_X2.get())]
                b = float(condition_S.get())
                A_arr.append(A)
                b_arr.append(b)
            res = linprog(c, A_ub=A_arr, b_ub=b_arr)
            print(f"Полки типа А: {round(res.x[0])}, Полки типа B: {round(res.x[1])},"
                f" Прибуток: {round(res.x[0]) * float(self.A_entr.get()) + round(res.x[1]) * float(self.B_entr.get())}")
        except Exception:
            self.error_label.config(text="Перевірте вхідні дані")

    # Метод для запуску
    def run(self):
        self.lottery.mainloop()
