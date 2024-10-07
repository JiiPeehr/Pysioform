import tkinter as tk
import testforms

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Physioform")
        self.geometry("400x300")
        self.label = tk.Label(self, text="Ole hyvä, ja valitse, minkä testin tuloksen haluat laskea.")
        self.label.grid(row=0, column=0, columnspan=2)
        
        # Button to open the Berg Balance Test form
        self.test_button = tk.Button(self, text="Bergin tasapainotesti", command=self.open_berg_test)
        self.test_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Button to open the FsqFin Test form
        self.test_button = tk.Button(self, text="FSQfin", command=self.open_fsqfin_test)
        self.test_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Button to open NDI Test form
        self.test_button = tk.Button(self, text="NDI", command=self.open_ndi_test)
        self.test_button.grid(row=3, column=0, columnspan=2, pady=10)

    def open_berg_test(self):
        test = testforms.BergTest()
        testforms.create_gui04(test, self)

    def open_fsqfin_test(self):
        test = testforms.FsqFinTest()
        testforms.create_gui04(test, self)

    def open_ndi_test(self):
        test = testforms.NdiTest()
        testforms.create_gui_ndi(test, self)

if __name__ == "__main__":
    app = App()
    app.mainloop()