import tkinter as tk
from tkinter import ttk, Frame
import webbrowser

vehicleInfoList = dict()
vehicleInfoList["Ford"] = ["Truck", "Van", "Sedan", "Compact", "SUV"]
vehicleInfoList["Dodge"] = ["Truck", "Van", "Sedan", "SUV"]
vehicleInfoList["Chevrolet"] = ["Truck", "Van", "Sedan", "SUV"]
vehicleInfoList["Toyota"]= ["Truck", "Van", "Sedan", "Compact", "SUV"]
vehicleInfoList["Honda"] = ["Truck", "Van", "Sedan", "Compact", "SUV"]
vehicleInfoList["Nissan"] = ["Sedan", "SUV"]
vehicleInfoList["Subaru"] = ["Sedan", "SUV"]

serviceCentersDict = {
    "Ford": "https://www.ford.com/dealerships/",
    "Dodge": "https://www.dodge.com/find-dealer.html",
    "Chevrolet": "https://www.chevrolet.com/certified-service-dealer-locator",
    "Toyota": "https://www.toyota.com/owners/service-centers/",
    "Honda": "https://automobiles.honda.com/tools/dealership-locator",
    "Nissan": "https://www.nissanusa.com/parts-service/en/dealer/Search",
    "Subaru": "https://www.subaru.com/owners/schedule-service.html"
}

selectedVehicleMake = None
selectedVehicleType = None

TITLES_FONT = ("Arial", 20)

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
        
        #Create oil life frame
        self.oilLifeFrame = oilLifeFrame(self)

        #Create gas mileage frame
        self.gasMileageFrame = gasMileageFrame(self)

        #Create service centers frame
        self.serviceCentersFrame = serviceCentersFrame(self)

        #Create my vehicle frame
        self.myVehicleFrame = MyVehicleFrame(self, self.updateServiceCenters)

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
        self.gasMileageFrame.renderWidget(False)
        self.serviceCentersFrame.renderWidget(False)

    def showActiveMenu(self):
        selection = self.activeSection
        self.hideAllMenus()

        if selection == "My Vehicle": 
            self.myVehicleFrame.renderWidget(True)
        
        elif selection == "Oil Life":
            self.oilLifeFrame.renderWidget(True)
        
        elif selection == "Gas Mileage":
            self.gasMileageFrame.renderWidget(True)
        
        elif selection == "Service Centers":
            self.serviceCentersFrame.renderWidget(True)

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

    def updateServiceCenters(self):
        self.serviceCentersFrame.update()

    
class MyVehicleFrame(ttk.Frame):
    def __init__(self, parent, updateServiceCenters):
        super().__init__(parent)

        self.updateServiceCenters = updateServiceCenters

        self.titleLabel = ttk.Label(self, text="Enter your vehicle", font=("Arial", 24))
        self.titleLabel.pack(pady=40)

        self.selectorsFrame = ttk.Frame(self)
        self.selectorsFrame.pack(pady=50)
        self.selectorsFrame.columnconfigure(0, weight=1, pad=30)
        self.selectorsFrame.columnconfigure(1, weight=1, pad=30)

        self.myVehicleTitleLabel = ttk.Label(self.selectorsFrame, text="Make", font=TITLES_FONT)
        self.myVehicleTitleLabel.grid(row=1, column=0)
        
        self.myVehicleTypeLabel = ttk.Label(self.selectorsFrame, text="Vehicle Type", font=TITLES_FONT)
        self.myVehicleTypeLabel.grid(row=1, column=1)
        
        vehicleMakes = list()

        for make in vehicleInfoList:
            vehicleMakes.append(make)

        self.makeSelector = ttk.Combobox(self.selectorsFrame, values=vehicleMakes, state="readonly")
        self.makeSelector.bind("<<ComboboxSelected>>", self.comboboxMakeSelected)
        self.makeSelector.grid(row=2, column=0)

        self.VehicleTypeSelector = ttk.Combobox(self.selectorsFrame, values=(), state="readonly")
        self.VehicleTypeSelector.bind("<<ComboboxSelected>>", self.comboboxVehicleTypeSelected)
        self.VehicleTypeSelector.grid(row=2, column=1)

        self.configure(style="Card")

    def renderWidget(self, show: bool):
        if show == True:
            self.place(relheight=1, relwidth=0.75, anchor=tk.W, relx=0.25, rely=0.5)
        
        else:
            self.place_forget()
    
    def comboboxMakeSelected(self, _event):
        global selectedVehicleMake
        selectedVehicleMake = self.makeSelector.get()
        selectedVehicleType = None
        self.VehicleTypeSelector.set("")

        makeTypesList = list()

        for carType in vehicleInfoList[selectedVehicleMake]:
            makeTypesList.append(carType)

        self.VehicleTypeSelector.configure(values=makeTypesList)
        self.makeSelector.selection_clear()
        self.updateServiceCenters()
        

    def comboboxVehicleTypeSelected(self, _event):
        selectedVehicleType = self.VehicleTypeSelector.get()
        self.VehicleTypeSelector.selection_clear()

class oilLifeFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #Frame widgets

        self.titleLabel = ttk.Label(self, text="Change yer oil", font=TITLES_FONT)
        self.titleLabel.pack(fill="both")

    #Class functions
    def renderWidget(self, show: bool):
        if show == True:
            self.place(relheight=1, relwidth=0.75, anchor=tk.W, relx=0.25, rely=0.5)
        else:
            self.place_forget()

class serviceCentersFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        #Frame widgets

        self.titleLabel = ttk.Label(self, text="Please select the make of your vehicle!", font=("Arial", 24))
        self.titleLabel.pack(pady=40)

        self.hyperlinkButton = ttk.Button(self, text="", style="Accent.TButton")

    #Class functions
    def renderWidget(self, show: bool):
        if show == True:
            self.place(relheight=1, relwidth=0.75, anchor=tk.W, relx=0.25, rely=0.5)
        else:
            self.place_forget()

    def update(self):
        if selectedVehicleMake is None:
            print("not")
            return
        
        dealerLocatorLink = serviceCentersDict[selectedVehicleMake]

        if dealerLocatorLink:
            self.titleLabel.configure(text="Find an official service center")
            self.hyperlinkButton.configure(text=dealerLocatorLink)
            self.hyperlinkButton.configure(command= lambda: webbrowser.open_new(dealerLocatorLink))
            self.hyperlinkButton.pack(pady=20)
        else:
            print("wtf")
            self.titleLabel.configure(text="Please select the make of your vehicle!")
            
            self.hyperlinkButton.configure(text="")
            self.hyperlinkButton.configure(command=None)
            self.hyperlinkButton.pack_forget()

            return
    

class gasMileageFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        entryLabelFont = ("Arial", 16)
        #Frame Widgets

        self.titleLabel = ttk.Label(self, text="Gas Mileage", font=("Arial", 24))
        self.titleLabel.pack(pady=50)

        self.enterInfoFrame = ttk.Frame(self)
        self.enterInfoFrame.pack(pady=20)
        self.enterInfoFrame.columnconfigure(0, pad=10)
        self.enterInfoFrame.columnconfigure(1, pad=10)
        self.enterInfoFrame.columnconfigure(2, pad=10)

        self.milesDrivenLabel = ttk.Label(self.enterInfoFrame, text="Miles Driven", font=entryLabelFont)
        self.milesDrivenLabel.grid(row=0, column=0)

        self.amountOfFuelLabel = ttk.Label(self.enterInfoFrame, text="Amount Of Fuel (GAL)", font=entryLabelFont)
        self.amountOfFuelLabel.grid(row=0, column=1)

        self.costPerGalLabel = ttk.Label(self.enterInfoFrame, text="Cost Per Gal", font=entryLabelFont)
        self.costPerGalLabel.grid(row=0, column=2)

        self.milesDrivenEntry = ttk.Entry(self.enterInfoFrame)
        self.milesDrivenEntry.grid(row=1, column=0)

        self.amountOfFuelEntry = ttk.Entry(self.enterInfoFrame)
        self.amountOfFuelEntry.grid(row=1, column=1)

        self.costPerGalEntry = ttk.Entry(self.enterInfoFrame)
        self.costPerGalEntry.grid(row=1, column=2)

        self.assumedMileageLabel = ttk.Label(self, text="Assumed national average of 10,000 miles per year.", font=("Arial", 10))
        self.assumedMileageLabel.pack(side="bottom")

    #Class functions
    def renderWidget(self, show: bool):
        if show == True:
            self.place(relheight=1, relwidth=0.75, anchor=tk.W, relx=0.25, rely=0.5)
        else:
            self.place_forget()
App() # OwO