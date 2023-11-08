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

    def read_entries(self):
        for condition_X1, condition_c_op, condition_X2, condition_choice, condition_S in self.condition_entries:
            print(condition_X1.get(), condition_c_op.get(), condition_X2.get(), condition_choice.get(),
                  condition_S.get())

    def create_widgets(self):
        A_entr = tk.Entry(self.lottery)
        B_entr = tk.Entry(self.lottery)
        A_lbl = tk.Label(self.lottery, text='A = ', background='#DCF4FF')
        B_lbl = tk.Label(self.lottery, text='B = ', background='#DCF4FF')
        MIN_MAX = tk.Label(self.lottery, text='MAX', background='#DCF4FF')
        MIN_MAX_check = tk.Checkbutton(self.lottery, background='#DCF4FF')
        condition_lbl = tk.Label(self.lottery, text='Conditions', background='#DCF4FF')

        for i in range(self.limits):
            condition_choice = tk.StringVar(self.lottery)
            condition_c_op = tk.StringVar(self.lottery)

            condition_X1 = tk.Entry(self.lottery)
            condition_X2 = tk.Entry(self.lottery)
            condition_EQ = tk.OptionMenu(self.lottery, condition_choice, *self.condition_equals)
            condition_choice.set("=")
            condition_OP = tk.OptionMenu(self.lottery, condition_c_op, *self.condition_operation)
            condition_c_op.set("+")
            condition_S = tk.Entry(self.lottery)

            condition_X1.grid(row=5+i, column=1, sticky='wens')
            condition_OP.grid(row=5+i, column=2, sticky='wens')
            condition_X2.grid(row=5+i, column=3, sticky='wens')
            condition_EQ.grid(row=5+i, column=4, sticky='wens')
            condition_S.grid(row=5+i, column=5, sticky='wens')

            self.condition_entries.append((condition_X1, condition_c_op, condition_X2, condition_choice, condition_S))

        decision_btn = tk.Button(self.lottery, text='Decision', command=self.read_entries)

        A_entr.grid(row=1, column=1, sticky='wens')
        B_entr.grid(row=1, column=3, sticky='wens')
        A_lbl.grid(row=1, column=0, sticky='wens')
        B_lbl.grid(row=1, column=2, sticky='wens')
        MIN_MAX_check.grid(row=1, column=5, sticky='wens')
        MIN_MAX.grid(row=1, column=4, sticky='wens')
        condition_lbl.grid(row=4, column=1, sticky='wens')
        decision_btn.grid(row=10, column=2, sticky='wens')

    def run(self):
        print(self.limits)
        self.lottery.mainloop()
