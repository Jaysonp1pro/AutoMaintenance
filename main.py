import tkinter as tk
from tkinter import ttk

class mainGui:
    def __init__(self):
        #variables n stuff
        self.leftSideButtonsList = list()
        self.activeSection = ""

        self.root = tk.Tk()
        self.root.geometry("900x500")
        self.root.resizable(False, False)
        self.root.title("Auto Maintenance")

        self.root.tk.call("source", "forest-dark.tcl")
        ttk.Style().theme_use("forest-dark")
        #End of root manipulation

        #left-side frame
        self.leftFrame = ttk.Frame(self.root, style="Card", padding=(5, 6, 7, 8))
        self.leftFrame.columnconfigure(0, weight=1)
        self.leftFrame.place(relheight=1, relwidth=0.25)

        #active Vehicle button
        self.activeVehicleButton = ttk.Button(self.leftFrame, text="My Vehicle", style="ToggleButton", command=self.myVehicleButtonPress)
        self.activeVehicleButton.grid(row=0, column=0, sticky="NESW", padx=8, pady=8)
        self.leftSideButtonsList.insert(0, self.activeVehicleButton)

        #gas mileage button
        self.gasMileageButton = ttk.Button(self.leftFrame, text="Gas Mileage", style="ToggleButton", command=self.gasMileageButtonPress)
        self.gasMileageButton.grid(row=1, column=0, sticky="NESW", padx=8, pady=8)
        self.leftSideButtonsList.insert(1, self.gasMileageButton)

        #Oil life button
        self.oilLifeButton = ttk.Button(self.leftFrame, text="Oil Life", style="ToggleButton", command=self.oilLifeButtonPress)
        self.oilLifeButton.grid(row=2, column=0, sticky="NESW", padx=8, pady=8)
        self.leftSideButtonsList.insert(2, self.oilLifeButton)

        #Service centers button
        self.serviceCentersButton = ttk.Button(self.leftFrame, text="Service Centers", style="ToggleButton", command=self.serviceCentersButtonPress)
        self.serviceCentersButton.grid(row=3, column=0, sticky="NESW", padx=8, pady=8)
        self.leftSideButtonsList.insert(3, self.serviceCentersButton)
        
        for i in self.leftSideButtonsList:
            self.leftFrame.rowconfigure(i, weight=1)
        
        self.root.mainloop()

    def highlightActiveSectionButton(self):
        for button in self.leftSideButtonsList:
            if button["text"] == self.activeSection:
                button.configure(style="Accent.TButton")
            else:
                button.configure(style="ToggleButton")

    def oilLifeButtonPress(self):
        self.activeSection = "Oil Life"
        self.highlightActiveSectionButton()

    def gasMileageButtonPress(self):
        self.activeSection = "Gas Mileage"
        self.highlightActiveSectionButton()

    def myVehicleButtonPress(self):
        self.activeSection = "My Vehicle"
        self.highlightActiveSectionButton()

    def serviceCentersButtonPress(self):
        self.activeSection = "Service Centers"
        self.highlightActiveSectionButton()

    

mainGui()