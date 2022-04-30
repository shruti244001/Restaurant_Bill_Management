from tkinter import *
import math,random,os
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.title("Billing Software")
        #bgcolor="#F8590A"
        #bgcolor="#02F7BA"
        #bgcolor="#FF8CED"
        #bgcolor="#074466"
        bgcolor="#FF002C"
        bgcolor="black"
        textcolor="#F3F4AF"
        title=Label(self.root,text="Billing Software",bd=10,relief=GROOVE,fg="white",bg=bgcolor,font=("times new roman",30,"bold"),pady=2)
        title.pack(fill=X)
        #------------------variables--------------------------------
        self.item1=IntVar()
        self.item2=IntVar()
        self.item3=IntVar()
        self.item4=IntVar()
        self.item5=IntVar()
        self.item6=IntVar()

        self.item7=IntVar()
        self.item8=IntVar()
        self.item9=IntVar()
        self.item10=IntVar()
        self.item11=IntVar()
        self.item12=IntVar()

        self.item13=IntVar()
        self.item14=IntVar()
        self.item15=IntVar()
        self.item16=IntVar()
        self.item17=IntVar()
        self.item18=IntVar()

        self.item19=IntVar()
        self.item20=IntVar()
        self.item21=IntVar()
        self.item22=IntVar()
        self.item23=IntVar()
        self.item24=IntVar()
        
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.c_table=StringVar()
        self.c_bill=StringVar()
        x=random.randint(1000,9999)
        self.c_bill.set(str(x))
        self.c_search=StringVar()

        #-----------------------price variables---------------
        self.total_drink=IntVar()
        self.total_snack=IntVar()
        self.total_food=IntVar()
        self.total_desert=IntVar()
        self.tax_drink=IntVar()
        self.tax_snack=IntVar()
        self.tax_food=IntVar()
        self.tax_desert=IntVar()
        #-------------------------coustomer detail-----------------------------
        F1=LabelFrame(self.root,text="Customer Detail",bd=10,relief=SUNKEN,fg="yellow",bg=bgcolor,font=("times new roman",18,"bold"))
        F1.place(x=0,y=70,relwidth=1)

        cname_lbl=Label(F1,text="Customer name",fg="white",bg=bgcolor,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_lbl=Label(F1,text="Contact no.",fg="white",bg=bgcolor,font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_txt=Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_lbl=Label(F1,text="Table no.",fg="white",bg=bgcolor,font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.c_table,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        cbill_lbl=Label(F1,text="Bill no.",fg="white",bg=bgcolor,font=("times new roman",15,"bold")).grid(row=0,column=6,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.c_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=7,padx=10,pady=5)

        #bill_btn=Button(F1,text="Search",width=10,bd=7,font="arial 12 bold").grid(row=0,column=8,pady=10,padx=10)
        #-----------------------soft Drink----------------------------------------------
        F2=LabelFrame(self.root,text="Drinks",bd=10,relief=SUNKEN,fg="yellow",bg=bgcolor,font=("times new roman",18,"bold"))
        F2.place(x=0,y=160,width=260,height=440)
        coffe_lbl=Label(F2,text="Items",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        coffe_lbl=Label(F2,text="Quantity",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=5,pady=10,sticky="w")
        
        coffe_lbl=Label(F2,text="coffee-₹15",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F2,width=6,textvariable=self.item1,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)

        coffe_lbl=Label(F2,text="Tea-₹20",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F2,width=6,textvariable=self.item2,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        coffe_lbl=Label(F2,text="Juice-₹60",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F2,width=6,textvariable=self.item3,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        coffe_lbl=Label(F2,text="Limca-₹40",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F2,width=6,textvariable=self.item4,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        coffe_lbl=Label(F2,text="Slice-₹50",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F2,width=6,textvariable=self.item5,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        coffe_lbl=Label(F2,text="cocacola-₹70",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F2,width=6,textvariable=self.item6,font="arial 15",bd=7,relief=SUNKEN).grid(row=6,column=1,padx=10,pady=10)
        #-------------------------snacks--------------------------------------------------
        F3=LabelFrame(self.root,text="Snacks",bd=10,relief=SUNKEN,fg="yellow",bg=bgcolor,font=("times new roman",18,"bold"))
        F3.place(x=260,y=160,width=305,height=440)
        
        coffe_lbl=Label(F3,text="Items",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        coffe_lbl=Label(F3,text="Quantity",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=1,pady=10,sticky="w")
        
        coffe_lbl=Label(F3,text="French Fries-₹100",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F3,width=4,textvariable=self.item7,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=1,pady=10)

        coffe_lbl=Label(F3,text="Cheese Balls-₹100",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F3,width=4,textvariable=self.item8,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=1,pady=10)

        coffe_lbl=Label(F3,text="Nachoes-₹150",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F3,width=4,textvariable=self.item9,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=1,pady=10)

        coffe_lbl=Label(F3,text="Hakka Noddles-₹250",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F3,width=4,textvariable=self.item10,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=1,pady=10)

        coffe_lbl=Label(F3,text="Macroni-₹70",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F3,width=4,textvariable=self.item11,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=1,pady=10)

        coffe_lbl=Label(F3,text="Spring Roll-₹100",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F3,width=4,textvariable=self.item12,font="arial 15",bd=7,relief=SUNKEN).grid(row=6,column=1,padx=1,pady=10)
        #------------------------food---------------------------------------------------
        F4=LabelFrame(self.root,text="Food Items",bd=10,relief=SUNKEN,fg="yellow",bg=bgcolor,font=("times new roman",18,"bold"))
        F4.place(x=565,y=160,width=300,height=440)
        
        coffe_lbl=Label(F4,text="Items",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        coffe_lbl=Label(F4,text="Quantity",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=1,pady=10,sticky="w")
        
        coffe_lbl=Label(F4,text="Biryani-₹50",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F4,width=4,textvariable=self.item13,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=1,pady=10)

        coffe_lbl=Label(F4,text="Kadai Paneer-₹150",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F4,width=4,textvariable=self.item14,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=1,pady=10)

        coffe_lbl=Label(F4,text="Chole Bhature-₹250",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F4,width=4,textvariable=self.item15,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=1,pady=10)

        coffe_lbl=Label(F4,text="Mix Veg-₹200",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F4,width=4,textvariable=self.item16,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=1,pady=10)

        coffe_lbl=Label(F4,text="Dal Makhni-₹150",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F4,width=4,textvariable=self.item17,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=1,pady=10)

        coffe_lbl=Label(F4,text="Kulche-₹50",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F4,width=4,textvariable=self.item18,font="arial 15",bd=7,relief=SUNKEN).grid(row=6,column=1,padx=1,pady=10)
        #--------------------------------Desert--------------------------
        F5=LabelFrame(self.root,text="Desert",bd=10,relief=SUNKEN,fg="yellow",bg=bgcolor,font=("times new roman",18,"bold"))
        F5.place(x=870,y=160,width=290,height=440)
        
        coffe_lbl=Label(F5,text="Items",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        coffe_lbl=Label(F5,text="Quantity",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=0,column=1,padx=1,pady=10,sticky="w")
        
        coffe_lbl=Label(F5,text="Icecream-₹200",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F5,width=4,textvariable=self.item19,font="arial 15",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=1,pady=10)

        coffe_lbl=Label(F5,text="Gulab Jamun-₹150",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F5,width=4,textvariable=self.item20,font="arial 15",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=1,pady=10)

        coffe_lbl=Label(F5,text="Ras Malai-₹100",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F5,width=4,textvariable=self.item21,font="arial 15",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=1,pady=10)

        coffe_lbl=Label(F5,text="Kheer-₹120",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F5,width=4,textvariable=self.item22,font="arial 15",bd=7,relief=SUNKEN).grid(row=4,column=1,padx=1,pady=10)

        coffe_lbl=Label(F5,text="Pastry-₹50",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F5,width=4,textvariable=self.item23,font="arial 15",bd=7,relief=SUNKEN).grid(row=5,column=1,padx=1,pady=10)

        coffe_lbl=Label(F5,text="Brawnie-₹200",fg=textcolor,bg=bgcolor,font=("times new roman",16,"bold")).grid(row=6,column=0,padx=10,pady=10,sticky="w")
        coffe_txt=Entry(F5,width=4,textvariable=self.item24,font="arial 15",bd=7,relief=SUNKEN).grid(row=6,column=1,padx=1,pady=10)
        #------------------Bill Area-----------------------------------------
        F6=Frame(self.root,bd=10,relief=SUNKEN)
        F6.place(x=1170,y=160,width=350,height=420)
        Bill_title=Label(F6,text="Bill Area",bd=7,font=("times new roman",15,"bold"),relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(F6,orient=VERTICAL)
        self.txtarea=Text(F6,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        #-------------------Bill Menu------------------------------------------
        F7=LabelFrame(self.root,text="Bill Menu",bd=10,relief=SUNKEN,fg="yellow",bg=bgcolor,font=("times new roman",18,"bold"))
        F7.place(x=0,y=600,relwidth=1,height=180)

        coffe_lbl=Label(F7,text="Total Drinks Price",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.total_drink,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=2)

        coffe_lbl=Label(F7,text="Total Snacks Price",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.total_snack,font="arial 10",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=2)

        coffe_lbl=Label(F7,text="Total Food Price",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.total_food,font="arial 10",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=2)

        coffe_lbl=Label(F7,text="Total Desert Price",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.total_desert,font="arial 10",bd=7,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=2)
        
        coffe_lbl=Label(F7,text="Drinks Tax",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.tax_drink,font="arial 10",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=2)

        coffe_lbl=Label(F7,text="Snacks Tax",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.tax_snack,font="arial 10",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=2)

        coffe_lbl=Label(F7,text="Food Tax",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.tax_food,font="arial 10",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=2)
        

        coffe_lbl=Label(F7,text="Desert Tax",fg="white",bg=bgcolor,font=("times new roman",14,"bold")).grid(row=3,column=2,padx=20,pady=1,sticky="w")
        coffe_txt=Entry(F7,width=18,textvariable=self.tax_desert,font="arial 10",bd=7,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=2)

        btn_frame=Frame(F7,bd=7,relief=GROOVE,padx=20,pady=20)
        btn_frame.place(x=700,width=800,height=150)

        total_btn=Button(btn_frame,text="Total",command=self.total,bg=bgcolor,fg="white",pady=10,width=12,bd=10,relief=SUNKEN,font="ariel 15 bold").grid(row=0,column=0,padx=10,pady=10)
        total_btn=Button(btn_frame,text="Generate Bill",command=self.bill_area,width=12,bg=bgcolor,fg="white",pady=10,bd=10,relief=SUNKEN,font="ariel 15 bold").grid(row=0,column=1,padx=10,pady=10)
        total_btn=Button(btn_frame,text="Clear",command=self.clear,bg=bgcolor,fg="white",pady=10,width=12,bd=10,relief=SUNKEN,font="ariel 15 bold").grid(row=0,column=2,padx=10,pady=10)
        total_btn=Button(btn_frame,text="Exit",command=self.exit,width=12,bg=bgcolor,fg="white",pady=10,bd=10,relief=SUNKEN,font="ariel 15 bold").grid(row=0,column=3,padx=10,pady=10)

        self.welcome_bill()
    
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\tWelcome")
        self.txtarea.insert(END,f"\nBill Number: {self.c_bill.get()}")
        self.txtarea.insert(END,f"\nCustomer name: {self.c_name.get()}")
        self.txtarea.insert(END,f"\nPhone number: {self.c_phone.get()}")
        self.txtarea.insert(END,f"\nTable number: {self.c_table.get()}")
        self.txtarea.insert(END,"\n======================================")
        self.txtarea.insert(END,"\nProducts\t\tQTY\t\tPrice")
        self.txtarea.insert(END,"\n======================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phone.get()=="" or self.c_table.get()=="":
            messagebox.showerror("Error","Customer Detail are must")
        elif self.dri_tax==0.0 and self.s_tax==0.0 and self.f_tax==0.0 and self.des_tax==0.0:
            messagebox.showerror("Error","No Product Purchase")
        
        self.welcome_bill()
        if self.item1.get()!=0:
            self.txtarea.insert(END,f"\nCoffee\t\t{self.item1.get()}\t\t{self.item1_Price}")
        if self.item2.get()!=0:
            self.txtarea.insert(END,f"\nTea\t\t{self.item2.get()}\t\t{self.item2_Price}")
        if self.item3.get()!=0:
            self.txtarea.insert(END,f"\nJuice\t\t{self.item3.get()}\t\t{self.item3_Price}")
        if self.item4.get()!=0:
            self.txtarea.insert(END,f"\nLimca\t\t{self.item4.get()}\t\t{self.item4_Price}")
        if self.item5.get()!=0:
            self.txtarea.insert(END,f"\nSlice\t\t{self.item5.get()}\t\t{self.item5_Price}")
        if self.item6.get()!=0:
            self.txtarea.insert(END,f"\nCocacola\t\t{self.item6.get()}\t\t{self.item6_Price}")
        
        if self.item7.get()!=0:
            self.txtarea.insert(END,f"\nFrench Fries\t\t{self.item7.get()}\t\t{self.item7_Price}")
        if self.item8.get()!=0:
            self.txtarea.insert(END,f"\nCheese Balls\t\t{self.item8.get()}\t\t{self.item8_Price}")
        if self.item9.get()!=0:
            self.txtarea.insert(END,f"\nNachoes\t\t{self.item9.get()}\t\t{self.item9_Price}")
        if self.item10.get()!=0:
            self.txtarea.insert(END,f"\nHakka Nodels\t\t{self.item10.get()}\t\t{self.item10_Price}")
        if self.item11.get()!=0:
            self.txtarea.insert(END,f"\nMacroni\t\t{self.item11.get()}\t\t{self.item11_Price}")
        if self.item12.get()!=0:
            self.txtarea.insert(END,f"\nSpring Roll\t\t{self.item12.get()}\t\t{self.item12_Price}")
        
        if self.item13.get()!=0:
            self.txtarea.insert(END,f"\nBiryani\t\t{self.item13.get()}\t\t{self.item13_Price}")
        if self.item14.get()!=0:
            self.txtarea.insert(END,f"\nKadai Paneer\t\t{self.item14.get()}\t\t{self.item14_Price}")
        if self.item15.get()!=0:
            self.txtarea.insert(END,f"\nChole Bhature\t\t{self.item15.get()}\t\t{self.item15_Price}")
        if self.item16.get()!=0:
            self.txtarea.insert(END,f"\nMix Veg\t\t{self.item16.get()}\t\t{self.item16_Price}")
        if self.item17.get()!=0:
            self.txtarea.insert(END,f"\nDal Makhni\t\t{self.item17.get()}\t\t{self.item17_Price}")
        if self.item18.get()!=0:
            self.txtarea.insert(END,f"\nKulche\t\t{self.item18.get()}\t\t{self.item18_Price}")
        
        if self.item19.get()!=0:
            self.txtarea.insert(END,f"\nIcecream\t\t{self.item19.get()}\t\t{self.item19_Price}")
        if self.item20.get()!=0:
            self.txtarea.insert(END,f"\nGulab Jamun\t\t{self.item20.get()}\t\t{self.item20_Price}")
        if self.item21.get()!=0:
            self.txtarea.insert(END,f"\nRas Malai\t\t{self.item21.get()}\t\t{self.item21_Price}")
        if self.item22.get()!=0:
            self.txtarea.insert(END,f"\nKheer\t\t{self.item22.get()}\t\t{self.item22_Price}")
        if self.item23.get()!=0:
            self.txtarea.insert(END,f"\nPastry\t\t{self.item23.get()}\t\t{self.item23_Price}")
        if self.item24.get()!=0:
            self.txtarea.insert(END,f"\nBrawnie\t\t{self.item24.get()}\t\t{self.item24_Price}")
        self.txtarea.insert(END,"\n--------------------------------------")
        if self.dri_tax!=0.0:
            self.txtarea.insert(END,f"\nDrink Tax\t\t\t     Rs.{self.dri_tax}")
        if self.s_tax!=0.0:
            self.txtarea.insert(END,f"\nSnacks Tax\t\t\t     Rs.{self.s_tax}")
        if self.f_tax!=0.0:
            self.txtarea.insert(END,f"\nFood Tax\t\t\t     Rs.{self.f_tax}")
        if self.des_tax!=0.0:
            self.txtarea.insert(END,f"\nDesert Tax\t\t\t     Rs.{self.des_tax}") 
        self.txtarea.insert(END,f"\nTotal Bill\t\t\t     Rs.{self.total_bill}")
        self.txtarea.insert(END,"\n--------------------------------------")
        self.save_bill()
    def total(self):
        
        self.item1_Price=self.item1.get()*15
        self.item2_Price=self.item2.get()*20
        self.item3_Price=self.item3.get()*60
        self.item4_Price=self.item4.get()*40
        self.item5_Price=self.item5.get()*50
        self.item6_Price=self.item6.get()*70
        
        self.total_drink_price=int(self.item1_Price+self.item2_Price+self.item3_Price+self.item4_Price+self.item5_Price+self.item6_Price)
        self.total_drink.set("Rs."+str(self.total_drink_price))
        self.dri_tax=round((self.total_drink_price*0.05),2)
        self.tax_drink.set("Rs."+str(round((self.total_drink_price*0.05),2)))
        
        self.item7_Price=self.item7.get()*100
        self.item8_Price=self.item8.get()*100
        self.item9_Price=self.item9.get()*150
        self.item10_Price=self.item10.get()*250
        self.item11_Price=self.item11.get()*70
        self.item12_Price=self.item12.get()*100
        
        self.total_snack_price=int(self.item7_Price+self.item8_Price+self.item9_Price+self.item10_Price+self.item11_Price+self.item12_Price)
        self.total_snack.set("Rs."+str(self.total_snack_price))
        self.s_tax=round((self.total_snack_price*0.05),2)
        self.tax_snack.set("Rs."+str(round((self.total_snack_price*0.05),2)))
        
        self.item13_Price=self.item13.get()*50
        self.item14_Price=self.item14.get()*150
        self.item15_Price=self.item15.get()*250
        self.item16_Price=self.item16.get()*200
        self.item17_Price=self.item17.get()*150
        self.item18_Price=self.item18.get()*50
        
        self.total_food_price=int(self.item13_Price+self.item14_Price+self.item15_Price+self.item16_Price+self.item17_Price+self.item18_Price)
        self.total_food.set("Rs."+str(self.total_food_price))
        self.f_tax=round((self.total_food_price*0.05),2)
        self.tax_food.set("Rs."+str(round((self.total_food_price*0.05),2)))
        
        self.item19_Price=self.item19.get()*200
        self.item20_Price=self.item20.get()*150
        self.item21_Price=self.item21.get()*100
        self.item22_Price=self.item22.get()*120
        self.item23_Price=self.item23.get()*50
        self.item24_Price=self.item24.get()*200
        
        self.total_desert_price=int(self.item19_Price+self.item20_Price+self.item21_Price+self.item22_Price+self.item23_Price+self.item24_Price)
        self.total_desert.set("Rs."+str(self.total_desert_price))
        self.des_tax=round((self.total_desert_price*0.05),2)
        self.tax_desert.set("Rs."+str(round((self.total_desert_price*0.05),2)))
        
        self.total_bill=self.total_drink_price+self.total_snack_price+self.total_food_price+self.total_desert_price+self.dri_tax+self.s_tax+self.f_tax+self.des_tax
        
    def save_bill(self):
        x=messagebox.askyesno("Save Bill","Do you want to save bill?")
        if x==1:
            self.bill_data=self.txtarea.get('1.0',END)
            f=open("bills/"+str(self.c_bill.get())+".txt","w")                                                            
            f.write(self.bill_data)
            f.close()
            messagebox.showinfo("saved","Bill saved sucessfully")
        else:
            return
    def clear(self):
        op=messagebox.askyesno("Clear","Do you really want to Clear?")
        if op>0:
            self.item1.set(0)
            self.item2.set(0)
            self.item3.set(0)
            self.item4.set(0)
            self.item5.set(0)
            self.item6.set(0)

            self.item7.set(0)
            self.item8.set(0)
            self.item9.set(0)
            self.item10.set(0)
            self.item11.set(0)
            self.item12.set(0)

            self.item13.set(0)
            self.item14.set(0)
            self.item15.set(0)
            self.item16.set(0)
            self.item17.set(0)
            self.item18.set(0)

            self.item19.set(0)
            self.item20.set(0)
            self.item21.set(0)
            self.item22.set(0)
            self.item23.set(0)
            self.item24.set(0)
        
            self.c_name.set("")
            self.c_phone.set("")
            self.c_table.set("")
            self.c_bill.set("")
            x=random.randint(1000,9999)
            self.c_bill.set(str(x))
            self.c_search.set("")

            #-----------------------price variables---------------
            self.total_drink.set(0)
            self.total_snack.set(0)
            self.total_food.set(0)
            self.total_desert.set(0)
            self.tax_drink.set(0)
            self.tax_snack.set(0)
            self.tax_food.set(0)
            self.tax_desert.set(0)
            self.welcome_bill()
    def exit(self):
        op=messagebox.askyesno("Exit","Do you really want to exit?")
        if op>0:
            self.root.destroy()
root=Tk()
obj=Bill_App(root)
root.mainloop()
