from tkinter import *
import customtkinter as ttk

Calculator = ttk.CTk()
Calculator.title("Calculator")
Calculator.geometry("384x620")
Calculator.resizable(False, False)
Calculator.config(bg="#2BCECE")


def Result():
    pass


# Output Window Frame Opens
outputFrame = ttk.CTkFrame(Calculator, bg_color="#2BCECE", fg_color="#2BCECE", height=100)

# Output Window
result = ttk.CTkCanvas(outputFrame, height=152)
result.pack(fill=BOTH)

# Output Window Frame Closes
outputFrame.pack(padx=10, pady=10, fill=X)

# Functions Frame Opens
functionFrame = ttk.CTkFrame(Calculator, height=180, fg_color="#21A2A2", bg_color="#2BCECE")

buttonClear = ttk.CTkButton(functionFrame, text="7", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("clear"))
buttonClear.grid(row=1, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="8", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("2"))
buttonClear.grid(row=1, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="9", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("3"))
buttonClear.grid(row=1, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="X", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("3"))
buttonClear.grid(row=1, column=4, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="4", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("clear"))
buttonClear.grid(row=2, column=0, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="5", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("2"))
buttonClear.grid(row=2, column=2, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="6", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("3"))
buttonClear.grid(row=2, column=3, padx=5, pady=5)

buttonClear = ttk.CTkButton(functionFrame, text="-", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("3"))
buttonClear.grid(row=2, column=4, padx=5, pady=5)

# Functions Frame Closes
functionFrame.pack(padx=10, pady=10, fill=X)

# Buttons Frame Opens
buttonFrame = ttk.CTkFrame(Calculator, fg_color="#21A2A2", bg_color="#2BCECE")

buttonClear = ttk.CTkButton(buttonFrame, text="C", font=("", 42, "bold"), width=80, fg_color="red",
                            command=lambda: print("clear"))
buttonClear.grid(row=0, column=0, padx=5, pady=5, columnspan=1)

buttonClear = ttk.CTkButton(buttonFrame, text="%", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                            command=lambda: print("2"))
buttonClear.grid(row=0, column=3, padx=5, pady=5)

buttonDivide = ttk.CTkButton(buttonFrame, text="÷", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                             command=lambda: print("3"))
buttonDivide.grid(row=0, column=4, padx=5, pady=5)

buttonSeven = ttk.CTkButton(buttonFrame, text="7", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("clear"))
buttonSeven.grid(row=1, column=0, padx=5, pady=5)

buttonEight = ttk.CTkButton(buttonFrame, text="8", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("2"))
buttonEight.grid(row=1, column=2, padx=5, pady=5)

buttonNine = ttk.CTkButton(buttonFrame, text="9", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                           command=lambda: print("3"))
buttonNine.grid(row=1, column=3, padx=5, pady=5)

buttonMultiply = ttk.CTkButton(buttonFrame, text="X", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                               command=lambda: print("3"))
buttonMultiply.grid(row=1, column=4, padx=5, pady=5)

buttonFore = ttk.CTkButton(buttonFrame, text="4", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                           command=lambda: print("clear"))
buttonFore.grid(row=2, column=0, padx=5, pady=5)

buttonFive = ttk.CTkButton(buttonFrame, text="5", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                           command=lambda: print("2"))
buttonFive.grid(row=2, column=2, padx=5, pady=5)

buttonSix = ttk.CTkButton(buttonFrame, text="6", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                          command=lambda: print("3"))
buttonSix.grid(row=2, column=3, padx=5, pady=5)

buttonSubtract = ttk.CTkButton(buttonFrame, text="-", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                               command=lambda: print("3"))
buttonSubtract.grid(row=2, column=4, padx=5, pady=5)

buttonOne = ttk.CTkButton(buttonFrame, text="1", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                          command=lambda: print("clear"))
buttonOne.grid(row=3, column=0, padx=5, pady=5)

buttonTwo = ttk.CTkButton(buttonFrame, text="2", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                          command=lambda: print("2"))
buttonTwo.grid(row=3, column=2, padx=5, pady=5)

buttonThree = ttk.CTkButton(buttonFrame, text="3", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                            command=lambda: print("3"))
buttonThree.grid(row=3, column=3, padx=5, pady=5)

buttonPlus = ttk.CTkButton(buttonFrame, text="+", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                           command=lambda: print("3"))
buttonPlus.grid(row=3, column=4, padx=5, pady=5)

buttonZero = ttk.CTkButton(buttonFrame, text="0", font=("", 42, "bold"), width=80, fg_color="#0D4242",
                           command=lambda: print("clear"))
buttonZero.grid(row=4, column=0, padx=5, pady=5, columnspan=1)

buttonDot = ttk.CTkButton(buttonFrame, text=".", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                          command=lambda: print("3"))
buttonDot.grid(row=4, column=3, padx=5, pady=5)

buttonEquals = ttk.CTkButton(buttonFrame, text="=", font=("", 42, "bold"), width=80, fg_color="#FAD200",
                             command=lambda: print("3"))
buttonEquals.grid(row=4, column=4, padx=5, pady=5)

# Buttons Frame Closes
buttonFrame.pack(padx=10, pady=10, fill=BOTH, expand=True, anchor=CENTER)
Calculator.mainloop()
