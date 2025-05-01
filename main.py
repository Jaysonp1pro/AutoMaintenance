import tkinter as tk
from tkinter import ttk, Frame

vehicleInfoList = dict()
vehicleInfoList["Ford"] = ["Truck", "Van", "Sedan", "Compact", "SUV"]
vehicleInfoList["Dodge"] = ["Truck", "Van", "Sedan", "SUV"]
vehicleInfoList["Chevrolet"] = ["Truck", "Van", "Sedan", "SUV"]
vehicleInfoList["Toyota "]= ["Truck", "Van", "Sedan", "Compact", "SUV"]
vehicleInfoList["Honda"] = ["Truck", "Van", "Sedan", "Compact", "SUV"]
vehicleInfoList["Nissan"] = ["Sedan", "SUV"]
vehicleInfoList["Subaru"] = ["Sedan", "SUV"]

selectedVehicleMake = None
selectedVehicleType = None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        #variables n stuff
        self.leftSideButtonsList = list()
        self.activeSection = ""

        self.geometry("900x500")
        self.resizable(False, False)
        self.title("Auto Maintenance")

        self.tk.call("source", "forest-dark.tcl")
        ttk.Style().theme_use("forest-dark")
        #End of root manipulation

        #left-side frame
        self.leftFrame = ttk.Frame(self, style="Card", padding=(5, 6, 7, 8))
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
        
        
        #Create my vehicle frame
        self.myVehicleFrame = MyVehicleFrame(self)

        #Create oil life frame
        self.oilLifeFrame = oilLifeFrame(self)

        self.mainloop()

    def highlightActiveSectionButton(self):
        for button in self.leftSideButtonsList:
            if button["text"] == self.activeSection:
                button.configure(style="Accent.TButton")
            else:
                button.configure(style="ToggleButton")

    def hideAllMenus(self):
        self.myVehicleFrame.renderWidget(False)
        self.oilLifeFrame.renderWidget(False)

    def showActiveMenu(self):
        selection = self.activeSection
        self.hideAllMenus()

        if selection == "My Vehicle": 
            self.myVehicleFrame.renderWidget(True)
        
        elif selection == "Oil Life":
            self.oilLifeFrame.renderWidget(True)
        
        elif selection == "Gas Mileage":
            print("gas")
        
        elif selection == "Service Centers":
            print("fix")

    def oilLifeButtonPress(self):
        self.activeSection = "Oil Life"
        self.highlightActiveSectionButton()
        self.showActiveMenu()

    def gasMileageButtonPress(self):
        self.activeSection = "Gas Mileage"
        self.highlightActiveSectionButton()
        self.showActiveMenu()

    def myVehicleButtonPress(self):
        self.activeSection = "My Vehicle"
        self.highlightActiveSectionButton()
        self.showActiveMenu()

    def serviceCentersButtonPress(self):
        self.activeSection = "Service Centers"
        self.highlightActiveSectionButton()
        self.showActiveMenu()

    
class MyVehicleFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.myVehicleTitleLabel = ttk.Label(self, text="Make", font=("Arial", 20))
        self.myVehicleTitleLabel.grid(row=0, column=0)
        
        self.myVehicleTypeLabel = ttk.Label(self, text="Vehicle Type", font=("Arial", 20))
        self.myVehicleTypeLabel.grid(row=0, column=1)
        
        vehicleMakes = list()

        for make in vehicleInfoList:
            vehicleMakes.append(make)

        self.makeSelector = ttk.Combobox(self, values=vehicleMakes, state="readonly")
        self.makeSelector.bind("<<ComboboxSelected>>", self.comboboxMakeSelected)
        self.makeSelector.grid(row=1, column=0)

        self.VehicleTypeSelector = ttk.Combobox(self, values=(), state="readonly")
        self.VehicleTypeSelector.bind("<<ComboboxSelected>>", self.comboboxVehicleTypeSelected)
        self.VehicleTypeSelector.grid(row=1, column=1)

        self.configure(style="Card")

    def renderWidget(self, show: bool):
        if show == True:
            self.place(relheight=1, relwidth=0.75, anchor=tk.W, relx=0.25, rely=0.5)
        
        else:
            self.place_forget()
    
    def comboboxMakeSelected(self, _event):
        selectedVehicleMake = self.makeSelector.get()

        makeTypesList = list()

        for carType in vehicleInfoList[selectedVehicleMake]:
            makeTypesList.append(carType)

        self.VehicleTypeSelector.configure(values=makeTypesList)
        self.makeSelector.selection_clear()

    def comboboxVehicleTypeSelected(self, _event):
        selectedVehicleType = self.VehicleTypeSelector.get()
        self.VehicleTypeSelector.selection_clear()

class oilLifeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #Frame widgets

        self.titleLabel = ttk.Label(self, text="Change yer oil", font=("Arial", 20))
        self.titleLabel.pack(fill="both")


    #Class functions
    def renderWidget(self, show: bool):
        if show == True:
            self.place(relheight=1, relwidth=0.75, anchor=tk.W, relx=0.25, rely=0.5)
        else:
            self.place_forget()

App() # OwO