from tkinter import *
import customtkinter as ttk

Calculator = ttk.CTk()
Calculator.title("Calculator")
Calculator.geometry("384x620")
Calculator.resizable(False, False)
Calculator.config(bg="#2BCECE")

def Result():
    pass

outputFrame = ttk.CTkFrame(Calculator,height=100)

result = Canvas(outputFrame, height=152)
result.pack(fill=BOTH)

outputFrame.pack(padx=10, pady=10, fill=X)

functionFrame = ttk.CTkFrame(Calculator, height=180, fg_color="#21A2A2")

buttonClear = ttk.CTkButton(functionFrame, text="7", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("clear"))
buttonClear.grid(row=1, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="8", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("2"))
buttonClear.grid(row=1, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="9", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=1, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="X", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=1, column=4, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="4", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("clear"))
buttonClear.grid(row=2, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="5", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("2"))
buttonClear.grid(row=2, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="6", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=2, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="-", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=2, column=4, padx=5, pady=5)


functionFrame.pack(padx=10, pady=10, fill=X)

buttonFrame = ttk.CTkFrame(Calculator, fg_color="#21A2A2")

buttonClear = ttk.CTkButton(buttonFrame, text="C", font=("",42, "bold"), width=80, fg_color="red", command=lambda:print("clear"))
buttonClear.grid(row=0, column=0, padx=5, pady=5, columnspan=1)

buttonClear = ttk.CTkButton(buttonFrame, text="%", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("2"))
buttonClear.grid(row=0, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="÷", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("3"))
buttonClear.grid(row=0, column=4, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="7", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("clear"))
buttonClear.grid(row=1, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="8", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("2"))
buttonClear.grid(row=1, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="9", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=1, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="X", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("3"))
buttonClear.grid(row=1, column=4, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="4", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("clear"))
buttonClear.grid(row=2, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="5", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("2"))
buttonClear.grid(row=2, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="6", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=2, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="-", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("3"))
buttonClear.grid(row=2, column=4, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="1", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("clear"))
buttonClear.grid(row=3, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="2", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("2"))
buttonClear.grid(row=3, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="3", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("3"))
buttonClear.grid(row=3, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="+", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("3"))
buttonClear.grid(row=3, column=4, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="0", font=("",42, "bold"), width=80,fg_color="#0D4242", command=lambda:print("clear"))
buttonClear.grid(row=4, column=0, padx=5, pady=5, columnspan=1)

buttonClear = ttk.CTkButton(buttonFrame, text=".", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("3"))
buttonClear.grid(row=4, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(buttonFrame, text="=", font=("",42, "bold"), width=80,fg_color="#FAD200", command=lambda:print("3"))
buttonClear.grid(row=4, column=4, padx=5, pady=5)

buttonFrame.pack(padx=10, pady=10, fill=BOTH, expand=True, anchor=CENTER)
Calculator.mainloop()
