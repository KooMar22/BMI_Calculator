# Import modules
from tkinter import *
from PIL import ImageTk, Image


class BMICalculator:
    def __init__(self):
        self.root = Tk()
        self.root.title("BMI Calculator App")
        self.root.config(bg="light yellow")

        # Window dimensions
        self.win_width = 380
        self.win_height = 530
        
        # Screen dimensions
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        # Center it
        self.x_coord = (self.screen_width - self.win_width) // 2
        self.y_coord = (self.screen_height - self.win_height) // 2
        self.root.geometry("{}x{}+{}+{}".format(self.win_width,
                    self.win_height, self.x_coord, self.y_coord))

        # Define the show bmi label as None so we can destroy it later
        self.show_bmi_lbl = None
        self.show_bmi_img = None

        # Create entries, label, button
        self.opis = Label(self.root, text="Ova aplikacija izračunat će Vaš BMI indeks.",
                          bg="light yellow", font=("Arial", 12, "bold"))
        self.height_lbl = Label(self.root, bg="light yellow", font=("Arial", 12),
                                text="Upišite visinu u metrima (odvojeno \".\"):")
        self.height_ent = Entry(self.root, width=10, justify="center", borderwidth=5)
        self.height_ent.bind("<KeyRelease>", self.activate_btn)
        
        self.weight_lbl = Label(self.root, bg="light yellow", font=("Arial", 12),
                                text="Upišite težinu u kg:")
        self.weight_ent = Entry(self.root, width=10, justify="center", borderwidth=5)
        self.weight_ent.bind("<KeyRelease>", self.activate_btn)
        
        self.pretvori_btn = Button(self.root, bg="light grey", text="Pretvori",
                                   borderwidth=8, state="disabled", command=self.show_result)
        

        # Put everything to the screen
        self.opis.grid(column=0, row=0, columnspan=2,
                       sticky="ew", pady=(0, 10))
        self.height_lbl.grid(column=0, row=1, sticky="w", padx=(0, 10))
        self.height_ent.grid(column=1, row=1)
        self.weight_lbl.grid(column=0, row=2, sticky="w", padx=(0, 10))
        self.weight_ent.grid(column=1, row=2)
        self.pretvori_btn.grid(column=1, row=3)


    def activate_btn(self, event):
        """Function to activate the Pretvori button when weight and height are entered."""
        weight = self.weight_ent.get()
        height = self.height_ent.get()
        if weight.isdigit() and height.replace(".", "").isnumeric():
            self.pretvori_btn.config(state="normal", bg="green")


    def calculate(self):
        """Function to calculate the BMI index"""      
        height = float(self.height_ent.get())
        weight = float(self.weight_ent.get())

        bmi = weight / (height ** 2)
        return bmi

    def show_result(self):
        """Function to show the result and appropriate message"""
        # Destroy previously given results
        if self.show_bmi_lbl and self.show_bmi_img:
            self.show_bmi_lbl.destroy()
            self.show_bmi_img.destroy()
        
        # Get the result
        res = self.calculate()
        
        # Appropriate message 
        if res > 40:
            msg = "Čestitamo! Dosegli ste rang nilskog konja!"
            image = Image.open("./imgs/hippo.jpg")
        elif res >= 35 and res <= 40:
            msg = "Pričekajte, uskoro će bager doći po Vas!"
            image = Image.open("./imgs/obese.jpg")
        elif res >= 30 and res < 35:
            msg = "Terapija plivanjem dobra je za mršavljenje.\nSamo nemojte skakati u bazen!"
            image = Image.open("./imgs/jade-destiny.jpg")
        elif res >= 25 and res < 30:
            msg = "Kebab s piletinom nije zdrava hrana!"
            image = Image.open("./imgs/kebab.jpg")
        elif res >= 18.5 and res < 25:
            msg = "Čestitamo! U idealnoj ste kategoriji!"
            image = Image.open("./imgs/athlete.jpg")
        elif res >= 17 and res < 18.5:
            msg = "Da niste možda pretjerali s dijetom?"
            image = Image.open("./imgs/skinny.jpg")
        elif res >= 16 and res < 17:
            msg = "Pojedite nešto, hrana Vas neće ubiti!"
            image = Image.open("./imgs/skinnier.jpg")
        else:
            msg = "Anoreksija nije rješenje!"
            image = Image.open("./imgs/anorexia.jpg")

        # Create the Label and put it on the screen
        self.show_bmi_lbl = Label(self.root, bg="light yellow",
                                  font=("Arial", 12, "italic"),
                                      text=f"Vaš indeks tjelesne mase je: {res:.2f}!\n{msg}")
        self.show_bmi_lbl.grid(column=0, row=4, columnspan=2, pady=10)

        # Get the appropriate image
        loaded_image = ImageTk.PhotoImage(image)
        self.show_bmi_img = Label(self.root, image=loaded_image)
        self.show_bmi_img.image = loaded_image
        self.show_bmi_img.grid(column=0, row=5, columnspan=2,
                               padx=10, pady=(10, 0), sticky="ew")

        self.clear()

    def clear(self):
        """Function to clear old values from the screen upon new entry."""
        self.weight_ent.delete(0, END)
        self.height_ent.delete(0, END)
        self.pretvori_btn.config(bg="light grey", state="disabled")


if __name__ == "__main__":
    bmi_calc = BMICalculator()
    bmi_calc.root.mainloop()