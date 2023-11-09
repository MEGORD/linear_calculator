from scipy.optimize import linprog
import tkinter as tk


class MainWindow:
    def __init__(self, limits_num):
        super().__init__()
        self.lottery = tk.Tk()
        self.lottery.title('Лінійне програмування')
        self.lottery.geometry('530x470')
        self.lottery.resizable(True, True)
        self.lottery.config(bg='#DCF4FF')
        self.limits = limits_num
        self.condition_entries = []
        self.condition_equals = [">=", ">", "=", "<", "<="]
        self.condition_operation = ["+", "-", "/", "*"]
        self.MIN_MAX_var = tk.BooleanVar(self.lottery)

    def read_entries(self):
        for condition_X1, condition_c_op, condition_X2, condition_choice, condition_S in self.condition_entries:
            print(condition_X1.get(), condition_c_op.get(), condition_X2.get(), condition_choice.get(),
                  condition_S.get())
        print(self.A_entr.get())
        print(self.B_entr.get())
        print(self.EQ_entr.get())
        print(self.MIN_MAX_var.get())

    def create_widgets(self):
        self.lottery.configure(bg='#DCF4FF')  # Настроим фон для окна

        # Добавляем заголовок "Головна функція"
        main_function_label = tk.Label(self.lottery, text='Головна функція', font=("Times New Roman", 16), bg='#DCF4FF')
        main_function_label.pack(pady=10)

        # Создаем фрейм для ввода A, B и EQ
        input_frame = tk.Frame(self.lottery, bg='#DCF4FF')
        input_frame.pack(pady=10)

        self.A_entr = tk.Entry(input_frame, width=5)
        self.B_entr = tk.Entry(input_frame, width=5)
        self.EQ_entr = tk.Entry(input_frame, width=5)

        self.A_entr.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text='A', bg='#DCF4FF').pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text='+', bg='#DCF4FF').pack(side=tk.LEFT, padx=5)
        self.B_entr.pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text='B', bg='#DCF4FF').pack(side=tk.LEFT, padx=5)
        tk.Label(input_frame, text='=', bg='#DCF4FF').pack(side=tk.LEFT, padx=5)
        self.EQ_entr.pack(side=tk.LEFT, padx=5)

        # Создаем фрейм для MAX
        max_frame = tk.Frame(self.lottery, bg='#DCF4FF')
        max_frame.pack(pady=10)

        MIN_MAX_check = tk.Checkbutton(max_frame, variable=self.MIN_MAX_var, bg='#DCF4FF')
        MIN_MAX_check.pack(side=tk.LEFT, padx=5)
        tk.Label(max_frame, text='MAX', bg='#DCF4FF', font=("Times New Roman", 16)).pack(side=tk.LEFT, padx=5)

        # Фрейм для условий
        conditions_frame = tk.Frame(self.lottery, bg='#DCF4FF')
        conditions_frame.pack(pady=10)

        condition_lbl = tk.Label(conditions_frame, text='Обмеження', font=("Times New Roman", 16), bg='#DCF4FF')
        condition_lbl.pack()

        for i in range(self.limits):
            condition_frame = tk.Frame(conditions_frame, bg='#DCF4FF')
            condition_frame.pack()

            condition_choice = tk.StringVar(self.lottery)
            condition_c_op = tk.StringVar(self.lottery)

            condition_X1 = tk.Entry(condition_frame, width=5)
            condition_X2 = tk.Entry(condition_frame, width=5)
            condition_const_x1 = tk.Label(condition_frame, width=5, text='x1', bg='#DCF4FF')
            condition_const_x2 = tk.Label(condition_frame, width=5, text='x2', bg='#DCF4FF')
            condition_EQ = tk.OptionMenu(condition_frame, condition_choice, *self.condition_equals)
            condition_choice.set("=")
            condition_OP = tk.OptionMenu(condition_frame, condition_c_op, *self.condition_operation)
            condition_c_op.set("+")
            condition_S = tk.Entry(condition_frame, width=5)

            condition_X1.pack(side=tk.LEFT, padx=5)
            condition_const_x1.pack(side=tk.LEFT, padx=5)
            condition_OP.pack(side=tk.LEFT, padx=5)
            condition_X2.pack(side=tk.LEFT, padx=5)
            condition_const_x2.pack(side=tk.LEFT, padx=5)
            condition_EQ.pack(side=tk.LEFT, padx=5)
            condition_S.pack(side=tk.LEFT, padx=5)

            self.condition_entries.append((condition_X1, condition_c_op, condition_X2, condition_choice, condition_S))

        decision_btn = tk.Button(self.lottery, text='Рішення', font=("Times New Roman", 16), command=self.read_entries)
        decision_btn.pack(pady=10)

    def run(self):
        print(self.limits)
        self.lottery.mainloop()
