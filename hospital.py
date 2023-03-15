import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Hospital(): 
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")

        ## Variable Declaration ## 
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))

        Ref = StringVar()
        cmbTabletNames = StringVar()
        HospitalCode = StringVar()
        Number_of_Tablets = StringVar()
        Lot = StringVar()
        IssuedDate = StringVar()
        ExpiryDate = StringVar()
        DailyDose = StringVar()
        SideEffects = StringVar()
        MoreInformation = StringVar()
        StorageAdvice = StringVar()
        Medication = StringVar()
        PatientId = StringVar()
        PatientNHSnumber = StringVar()
        Patientname = StringVar()
        Dateofbirth = StringVar()
        PatientAddress = StringVar()
        Prescription = StringVar()
        NHSnumber = StringVar()

        ## To generate random number ## 
        def Reference_numfunc():
            ranumber = random.randint(10000,9999999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber)

        def prescriptiondatafunc():
            Reference_numfunc()
            TextPrescription.insert(END, "Patient ID: \t\t"+PatientId.get()+"\n")
            TextPrescription.insert(END, "Patient Name: \t\t"+Patientname.get()+"\n")
            TextPrescription.insert(END, "Tablet: \t\t"+cmbTabletNames.get()+"\n")
            TextPrescription.insert(END, "Number of Tablet: \t\t"+Number_of_Tablets.get()+"\n")
            TextPrescription.insert(END, "Daily Dose: \t\t"+DailyDose.get()+"\n")
            TextPrescription.insert(END, "Issued Date: \t\t"+IssuedDate.get()+"\n")
            TextPrescription.insert(END, "Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            TextPrescription.insert(END, "Storage: \t\t"+StorageAdvice.get()+"\n")
            TextPrescription.insert(END, "More Information: \t\t"+MoreInformation.get()+"\n")


        def receiptdatafunc():
            Reference_numfunc()
            TextPrescriptionData.insert(END, Date_of_Registration.get()+"\t\t"+PatientId.get()+"\t\t"+Patientname.get()+"\t"+Dateofbirth.get()+"\t\t"+ NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"+Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+StorageAdvice.get()+"\t"+PatientId.get()+"\n") 
            return 

        def exitbtn(): 
            exitbtn = tkinter.message.askyesno("Hospital Management System", "Are you sure you want to exit?") 
            if exitbtn > 0: 
                root.destroy()  
            return 
        
        def deletefunc(): 
            Ref.set("")
            cmbTabletNames.set("")
            HospitalCode.set("")
            Number_of_Tablets.set("")
            Lot.set("")
            IssuedDate.set("")
            ExpiryDate.set("")
            DailyDose.set("")
            SideEffects.set("")
            MoreInformation.set("")
            StorageAdvice.set("")
            Medication.set("")
            PatientId.set("")
            PatientNHSnumber.set("")
            Patientname.set("")
            Dateofbirth.set("")
            PatientAddress.set("")
            Prescription.set("")
            NHSnumber.set("")
            

############ TITLE ######################
        title = Label(self.root,text = "Hospital Management System", font =("monotype corsiva",42,"bold"),bd = 5, relief= GROOVE,bg = "#2eb8b8",fg = "black")
        title.pack(side = TOP, fill = X)

############ FRAMES #####################
        Manage_Frame = Frame(self.root,width = 1510 , height = 400, bd=5, relief = RIDGE, bg = "#0099cc")
        Manage_Frame.place(x=10, y=80)

        Button_Frame = Frame(self.root,width = 1510 , height = 55, bd=4, relief = RIDGE, bg = "#328695")
        Button_Frame.place(x=10, y=460)

        Data_Frame = LabelFrame(self.root,width = 1510 , height = 270, bd=4, relief = RIDGE, bg = "#266e73")
        Data_Frame.place(x=10, y=510)

        ## Inner Frames ## 

        Data_FrameLeft = LabelFrame(Manage_Frame,width = 1050,text = "General Information", font = ("arial",20,"italic bold"), height = 390, bd = 7 , relief = RIDGE , bg = "#0099cc")
        Data_FrameLeft.pack(side = LEFT)

        Data_FrameRight = LabelFrame(Manage_Frame,width = 1050,text = "Prescription", font = ("arial",15,"italic bold"), height = 390, bd = 7 , relief = RIDGE , bg = "#0099cc")
        Data_FrameRight.pack(side = RIGHT) 

        Data_Framedata = LabelFrame(Data_Frame, width = 1050, text = "Prescription Data", font = ("arial",12,"italic bold"), height = 390 , bd = 4 , relief = RIDGE , bg = "#3eb7bb")
        Data_Framedata.pack(side = LEFT)

        ## Labels ## 
        Datelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date", padx = 2, bg ="#0099cc")
        Datelbl.grid(row = 0 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        Datetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Date_of_Registration)
        Datetxt.grid(row = 0 , column = 1 , padx = 10 , pady = 5, sticky = E) 

        ## Ref ## 
        Reflbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Reference Number", padx = 2, bg ="#0099cc")
        Reflbl.grid(row = 1 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        Reftxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Ref)
        Reftxt.grid(row = 1 , column = 1 , padx = 10 , pady = 5, sticky = E) 

        ## Patient ID ## 
        PatientIdlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Patient Id", padx = 2, bg ="#0099cc")
        PatientIdlbl.grid(row = 2 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        PatientIdtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientId)
        PatientIdtxt.grid(row = 2 , column = 1 , padx = 10 , pady = 5, sticky = E) 

        ## Patient Name ##
        PatientNamelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Patient Name", padx = 2, bg ="#0099cc")
        PatientNamelbl.grid(row = 3 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        PatientNametxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Patientname)
        PatientNametxt.grid(row = 3 , column = 1 , padx = 10 , pady = 5, sticky = E) 
        
        ## Date of Birth ## 
        Dateofbirthlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of Birth", padx = 2, bg ="#0099cc")
        Dateofbirthlbl.grid(row = 4 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        Dateofbirthtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Dateofbirth)
        Dateofbirthtxt.grid(row = 4 , column = 1 , padx = 10 , pady = 5, sticky = E)

        ## Address ## 
        Addresslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Address", padx = 2, bg ="#0099cc")
        Addresslbl.grid(row = 5 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        Addresstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientAddress)
        Addresstxt.grid(row = 5 , column = 1 , padx = 10 , pady = 5, sticky = E)

        ## NHS number ## 
        NHSnumberlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "NHS unique number", padx = 2, bg ="#0099cc")
        NHSnumberlbl.grid(row = 6 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        NHSnumbertxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = NHSnumber)
        NHSnumbertxt.grid(row = 6 , column = 1 , padx = 10 , pady = 5, sticky = E)

        ## Tablet Name ## 
        Tabletlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Tablet", padx = 2, bg ="#0099cc")
        Tabletlbl.grid(row = 7 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        
        Tabletcmb = ttk.Combobox(Data_FrameLeft , textvariable = cmbTabletNames , width = 25 , state = "readonly", font = ("arial",12,"bold"))
        Tabletcmb['values'] = ("", "Paracetamol", "Dan-p", "Dio-1 One", "Calpol", "Amlodipine Besylate","Nexium", "Singular", "Plavix", "Amoxicillian", "Azithromycin","Limcin-900")
        Tabletcmb.current(0) 
        Tabletcmb.grid(row = 7 , column = 1, padx = 10 , pady = 5) 

        ##  No of tablets to take ## 
        No_of_Tabletslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Number of Tablets", padx = 2, bg ="#0099cc")
        No_of_Tabletslbl.grid(row = 8 , column = 0 , padx = 10 , pady = 5 , sticky = W) 
        No_of_Tabletstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8 , column = 1 , padx = 10 , pady = 5, sticky = E)

        ## Hospital Code ##
        HospitalCodelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Hospital Code", padx = 2, bg ="#0099cc")
        HospitalCodelbl.grid(row = 0 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        HospitalCodetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = HospitalCode)
        HospitalCodetxt.grid(row = 0 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Storage Advice ## 
        StorageAdvicelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Storage Advice", padx = 2, bg ="#0099cc")
        StorageAdvicelbl.grid(row = 1 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        
        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft , textvariable = StorageAdvice , width = 25 , state = "readonly", font = ("arial",12,"bold"))
        StorageAdvicecmb['values'] = ("", "Under room temp","below 5*C","below 0*C","Refrigiration") 
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row = 1 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Lot number of medicine ## 
        Lot_nolbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Lot number", padx = 2, bg ="#0099cc")
        Lot_nolbl.grid(row = 2 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        Lot_nolbltxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Lot)
        Lot_nolbltxt.grid(row = 2 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Issued Date ## 
        IssuedDatelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of Issue", padx = 2, bg ="#0099cc")
        IssuedDatelbl.grid(row = 3 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        IssuedDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = IssuedDate)
        IssuedDatetxt.grid(row = 3 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Expiry Date ## 
        IssuedDatalbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of Expiry", padx = 2, bg ="#0099cc")
        IssuedDatalbl.grid(row = 4 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        IssuedDatatxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = ExpiryDate)
        IssuedDatatxt.grid(row = 4 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Daily Dose ## 
        Dailydoselbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Dose", padx = 2, bg ="#0099cc")
        Dailydoselbl.grid(row = 5 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        Dailydosetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = DailyDose)
        Dailydosetxt.grid(row = 5 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Side Effects ## 
        SideEffectslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Side Effects", padx = 2, bg ="#0099cc")
        SideEffectslbl.grid(row = 6 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        SideEffectstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = SideEffects)
        SideEffectstxt.grid(row = 6 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## More Information ## 
        MoreInformationlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "More Information", padx = 2, bg ="#0099cc")
        MoreInformationlbl.grid(row = 7 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        MoreInformationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = MoreInformation)
        MoreInformationtxt.grid(row = 7, column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Medication (Yes/No) ##
        Medicationlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Medication", padx = 2, bg ="#0099cc")
        Medicationlbl.grid(row = 8 , column = 2 , padx = 10 , pady = 5 , sticky = W) 
        Medicationlbltxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Medication)
        Medicationlbltxt.grid(row = 8 , column = 3 , padx = 10 , pady = 5, sticky = E)

        ## Text Field for prescription ## 
        TextPrescription = Text(Data_FrameRight , font = ("arial",12,"bold"), width = 55 , height = 17 , padx = 3, pady = 5)
        TextPrescription.grid(row = 0, column = 0)

        ## Text for Prescription Data

        TextPrescriptionData = Text(Data_Framedata , font = ("arial",12,"bold"), width = 203 , height = 12) 
        TextPrescriptionData.grid(row = 1, column = 0) 

        ## Now we will add buttons to our middle frame ## 

        Prescriptionbtn = Button(Button_Frame, text = "Prescription" , bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial",15,"bold"), width = 22, command = prescriptiondatafunc)  
        Prescriptionbtn.grid(row = 0, column = 0, padx = 15)

        Receiptbtn = Button(Button_Frame, text = "Prescription Data" , bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial",15,"bold"), width = 22, command = receiptdatafunc ) 
        Receiptbtn.grid(row = 0, column = 1, padx = 15)

        Resetbtn = Button(Button_Frame, text = "Reset" , bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial",15,"bold"), width = 22) 
        Resetbtn.grid(row = 0, column = 2, padx = 15)

        Deletebtn = Button(Button_Frame, text = "Delete" , bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial",15,"bold"), width = 22, command = deletefunc ) 
        Deletebtn.grid(row = 0, column = 3, padx = 15)

        Exitbtn = Button(Button_Frame, text = "Exit" , bg = "#ffaab0", activebackground = "#fcceb2", font = ("arial",15,"bold"), width = 22, command = exitbtn) 
        Exitbtn.grid(row = 0, column = 4, padx = 15)

        prescriptiondatarow = Label(Data_Framedata , bg = "white", font = ("arial",12,"bold"), 
        text = "Date\tReference Id\tPatient Name\t Date of Birth\tNHS Number\tTablet\tNo. of Tablet\tIssued Date\tExpiry Date\tDaily Dose\tStorage Advice\tPatient ID") 
        prescriptiondatarow.grid(row = 0 , column = 0 , sticky = W) 


if __name__=="__main__":
    root = Tk()
    app = Hospital(root)
    root.mainloop()

