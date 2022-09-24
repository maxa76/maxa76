import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkinter import *
import pymysql

class employee:
    def __init__(self,root):
        self.root = root
        self.root.title(" Maxa Project")
        self.root.geometry("1450x700+0+0") # gore levo
        
        title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("verdana",40,"bold"),bg="blue",fg="white")
        title.pack(side=TOP,fill=X)
        
        self.Eno=StringVar()
        self.Name=StringVar()
        self.Department=StringVar()
        self.Gender=StringVar()
        self.Address=StringVar()
        self.SearchBy=StringVar()
        self.SearchText=StringVar()
        
        #Frame 1 - Left side frame
        Frame1=Frame(self.root,bd="4",bg="blue",relief=RIDGE)  ##3-D effects
        Frame1.place(x=20,y=85,width=450,height=560)
        
        mtitle=Label(Frame1,text="Manage Employees", bg="blue",fg="white",font=("verdana",20,"bold"))
        mtitle.grid(row=0,columnspan=2,padx=10,pady=20, sticky="w")
        
        L_Eno=Label(Frame1,text="EmpNo", bg="blue",fg="white",font=("verdana",12,"bold"))
        L_Eno.grid(row=2,column=0,padx=20,pady=20,sticky="w")
        
        T_Eno = Entry(Frame1,textvariable=self.Eno, font=("verdana",12,"bold"),bd=5,relief=GROOVE)
        T_Eno.grid(row=2,column=1,padx=20,pady=20,sticky="w")
        
        L_Name=Label(Frame1,text="Name", bg="blue",fg="white",font=("verdana",12,"bold"))
        L_Name.grid(row=3,column=0,padx=20,pady=10,sticky="w")
        
        T_Name = Entry(Frame1,textvariable=self.Name, font=("verdana",12,"bold"),bd=5,relief=GROOVE)
        T_Name.grid(row=3,column=1,padx=20,pady=10,sticky="w")
        
        L_Dept=Label(Frame1,text="Department", bg="blue",fg="white",font=("verdana",12,"bold"))
        L_Dept.grid(row=4,column=0,padx=20,pady=10,sticky="w")
        
        T_Dept = Entry(Frame1,textvariable=self.Department, font=("verdana",12,"bold"),bd=5,relief=GROOVE)
        T_Dept.grid(row=4,column=1,padx=20,pady=10,sticky="w")
        
        L_Gender=Label(Frame1,text="Gender", bg="blue",fg="white",font=("verdana",12,"bold"))
        L_Gender.grid(row=5,column=0,padx=20,pady=10,sticky="w")
        
        C_Gender = ttk.Combobox(Frame1,textvariable=self.Gender, font=("verdana",12,"bold"),state="readonly")
        C_Gender['values']=("Male","Female","Others")
        C_Gender.grid(row=5,column=1,padx=20,pady=10)
        
        L_Addr=Label(Frame1,text="Address", bg="blue",fg="white",font=("verdana",12,"bold"))
        L_Addr.grid(row=6,column=0,padx=20,pady=10,sticky="w")
        
        self.Address=Text(Frame1, width=22,height=4,font=("verdana",12,"bold"))
        self.Address.grid(row=6,column=1,padx=20,pady=10,sticky="w")
        
        Frame1in=Frame(Frame1,bd="4",bg="blue",relief=RIDGE)  ## Unutra Frame1
        Frame1in.place(x=15,y=400,width=410,height=60)
        
        B_Add=Button(Frame1in,text="ADD",width=10,command=self.addData).grid(row=0,column=0,padx=10,pady=15)
        B_Update=Button(Frame1in,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=15)
        B_Del=Button(Frame1in,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=15)
        B_Clear=Button(Frame1in,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=15)
        
        Frame2=Frame(self.root,bd="4",bg="blue",relief=RIDGE)  ##3-D effects
        Frame2.place(x=500,y=85,width=920,height=560)
        
        L_Search=Label(Frame2,text="SEARCH BY", bg="blue",fg="white",font=("verdana",12,"bold"))
        L_Search.grid(row=0,column=0,padx=20,pady=10,sticky="w")
        
        C_Search = ttk.Combobox(Frame2,textvariable=self.SearchBy, font=("verdana",12,"bold"),state="readonly")
        C_Search['values']=("EmpNo","Name","Department","Gender","Address")
        C_Search.grid(row=0,column=1,padx=20,pady=10)
        
        T_Search = Entry(Frame2,textvariable=self.SearchText, font=("verdana",12,"bold"),bd=5,relief=GROOVE)
        T_Search.grid(row=0,column=2,padx=20,pady=10,sticky="w")
        
        B_Search=Button(Frame2,text="SEARCH",width=10, command=self.search_data).grid(row=0,column=3,padx=10,pady=15)
        B_Show=Button(Frame2,text="SHOW ALL",width=10,command=self.displayData).grid(row=0,column=4,padx=10,pady=15)
        
        T_Frame=Frame(Frame2,bd="4",bg="blue",relief=RIDGE)  ##3-D effects
        T_Frame.place(x=20,y=70,width=860,height=470)
        
        scroll_x = Scrollbar(T_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(T_Frame,orient=VERTICAL)
        
        self.Emp=ttk.Treeview(T_Frame, columns=("EmpNo","Name","Department","Gender","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Emp.xview) 
        scroll_y.config(command=self.Emp.yview) 
        
        self.Emp.heading("EmpNo",text="EMPNO")
        self.Emp.heading("Name",text="NAME")
        self.Emp.heading("Department",text="DEPARTMENT")
        self.Emp.heading("Gender",text="GENDER")
        self.Emp.heading("Address",text="ADDRESS")
        self.Emp['show']='headings'
        self.Emp.column("EmpNo",width=100)
        self.Emp.column("Name",width=200)
        self.Emp.column("Department",width=150)
        self.Emp.column("Gender",width=100)
        self.Emp.column("Address",width=350)
        
        self.Emp.bind("<ButtonRelease-1>",self.get_data) # OVDE POVEZUJEMO KLIK NA RED U TREEVIEW SA POZIVANJEM FUNKCIJE get_data
        
        self.Emp.pack(fill=BOTH,expand=1)
        
    def displayData(self):
        con = mysql.connector.connect(host='localhost',user='root',password="janjicmarta",database='off')
        cur=con.cursor()
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()
        print(rows)
        if(len(rows)!=0):
            self.Emp.delete(*self.Emp.get_children()) # OVDE PRVO BRIŠEMO POSTOJEĆE ZAPISE 
            for row in rows: # OVDE PUNIMO TREEVIEW
                self.Emp.insert('',END,values=row)
            con.commit()
        con.close()
        
    def addData(self):
        con = mysql.connector.connect(host='localhost',user='root',password="janjicmarta",database='off')
        cur=con.cursor()
        print(self.Eno.get())
        print(self.Name.get())
        print(self.Department.get())
        print(self.Gender.get())
        print(self.Address.get("1.0",END))
        cur.execute("INSERT INTO employee VALUES(%s, %s, %s, %s, %s)",(self.Eno.get(),self.Name.get(),self.Department.get(),self.Gender.get(),self.Address.get("1.0",END)))
        con.commit()
        con.close()
        messagebox.showinfo("Bravo","Uspesno dodavanje reda!!!")
        self.displayData()
        self.clear()
        
    def clear(self):
        self.Eno.set("")
        self.Name.set("")
        self.Department.set("")
        self.Gender.set("")
        self.Address.delete("1.0",END)
        
    def get_data(self,ev): # OVA FUNKCIJA PUNI KOMPONENTE U FREJMU frame1, POTREBNO JE NAVESTI DRUGI ARGUMENT
        cursor_row = self.Emp.focus() # određivanje indeksa vrste na kojoj smo pozicionirani
        contents = self.Emp.item(cursor_row)
        print(contents) # {'text': '', 'image': '', 'values': [3, 'Marko', 'CS', 'Male', 'BG\n'], 'open': 0, 'tags': ''}
        row = contents['values']  # preuzimanje sadržaja (values) iz te vrste 
        self.Eno.set(row[0]) 
        self.Name.set(row[1])
        self.Department.set(row[2])
        self.Gender.set(row[3])
        self.Address.delete("1.0",END) # PRVO BRISANJE
        self.Address.insert(END,row[4]) # PA ONDA PUNJENJE
        
    def update_data(self):
        con = mysql.connector.connect(host='localhost',user='root',password="janjicmarta",database='off')
        cur=con.cursor()
        cur.execute("UPDATE employee SET name=%s, department=%s,gender=%s,address=%s where empno=%s",
        (self.Name.get(),self.Department.get(),self.Gender.get(),self.Address.get("1.0",END),self.Eno.get()))
        con.commit()
        con.close()
        self.displayData()
        self.clear()
    
    def delete_data(self):
        con = pymysql.connect(host='localhost',user='root',password="janjicmarta",database='off')
        cur=con.cursor()
        cur.execute("delete from employee where empno=%s",self.Eno.get())
        con.commit()
        con.close()
        self.displayData()
        self.clear()
        
    def search_data(self): # POVEZATI SA KOMPONENTOM C_Search (textvariable=self.Search), 
        #napraviti promenljivu SearchBy i povezati sa dugmetom B_Search
        #Povezati sa komponentom SearchText
        con = mysql.connector.connect(host='localhost',user='root',password="janjicmarta",database='off')
        cur=con.cursor()
        cur.execute("select * from employee where "+str(self.SearchBy.get())+" like binary '%"+self.SearchText.get()+"%'")
        print("select * from employee where "+str(self.SearchBy.get())+" like binary '%"+self.SearchText.get()+"%'")
        rows = cur.fetchall()
        if(len(rows)!=0):
            self.Emp.delete(*self.Emp.get_children()) # OVDE PRVO BRIŠEMO POSTOJEĆE ZAPISE 
            for row in rows: # OVDE PUNIMO TREEVIEW
                self.Emp.insert('',END,values=row)
                con.commit()
        else:
            self.Emp.delete(*self.Emp.get_children()) # U LSUCAJU POGRESNE PRETRAGE, BRISANJE REDOVA
        con.close()
        
        
root = tk.Tk()
obj = employee(root)
#obj.displayData() # OVDE BI SE INICIJALNO PUNIO TREE_VIEW
root.mainloop()