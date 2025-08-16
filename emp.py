from tkinter import *
from requests import * 
from sqlite3 import *
from tkinter.messagebox import * 
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt


def add() : 
	sw.deiconify()
	mw.withdraw()

def back() : 
	mw.deiconify()
	sw.withdraw()

def view() : 
	tw.deiconify()
	mw.withdraw()
	scr_view.delete(1.0 , END)
	con = None
	try : 
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data : 
			info +=  " id: " +   str(d[0])   +   " name: " +    str(d[1])  +   " salary: " +  str(d[2]) +  "\n"
		scr_view.insert(INSERT , info)
	except Exception as e :
		con.rollback()
		showerror("Issue" , e) 
	finally : 
		if con is not None :
			con.close()


def back1() : 
	mw.deiconify()
	tw.withdraw()

def update() : 
	fw.deiconify()
	mw.withdraw()

def back2() : 
	mw.deiconify()
	fw.withdraw()

def delete() : 
	nw.deiconify()
	mw.withdraw()

def back3() : 
	mw.deiconify()
	nw.withdraw()

mw = Tk( )
mw.title("Employee Management System")
mw.geometry("700x700+400+50")
mw.configure(bg = "white")
f = ("Calibri" , 30 , "bold")

btn_add = Button(mw , text = "Add" , font = f , width = 10 , command = add)
btn_add.pack(pady = 10)

btn_view = Button(mw , text = "View" , font = f , width = 10 , command = view)
btn_view.pack(pady = 10)

btn_update = Button(mw , text = "Update" , font = f , width = 10 , command = update )
btn_update.pack(pady = 10)

btn_delete = Button(mw , text = "Delete" , font = f , width = 10 , command = delete)
btn_delete.pack(pady = 10)


sw = Toplevel(mw)
sw.title("Add ")
sw.geometry("700x700+400+50")
f = ("Calibri" , 30 , "bold")

lab_id = Label(sw , text = "Enter id : " , font = f  )
lab_id.pack(pady = 10)

ent_id = Entry(sw , font = f )
ent_id.pack(pady = 10)


lab_name = Label(sw , text = "Enter name : " , font = f  )
lab_name.pack(pady = 10)

ent_name = Entry(sw , font = f )
ent_name.pack(pady = 10)

lab_salary = Label(sw , text = "Enter salary : " , font = f )
lab_salary.pack(pady = 10)

ent_salary = Entry(sw , font = f )
ent_salary.pack(pady = 10)

def save() : 
	con = None
	try : 
		con = connect("employee.db")
		cursor = con.cursor()  
		sql = "insert into emp values('%d' , '%s' , '%f')"
		eid = ent_id.get()
		eid = eid.strip()              
		if (eid == "") or (eid.strip()== "" ) : 
			showerror("Failed ","Id should not be empty")
			ent_id.delete(0 , END)
			ent_id.focus()
			return
		try : 
			id = int(eid) 
		except ValueError : 
			showerror("Error" , "Id must be in integer only")
			ent_id.delete(0 , END)
			ent_id.focus()
			return
		if id < 1 : 
			showerror(" Zero error " ,"Minimum id should be 1")
			ent_id.delete(0 , END)
			ent_id.focus()
			return
		name = ent_name.get()
		if (name == "") or (name.strip() == "") : 
			showerror("Error " ,"Name should not be empty ")
			ent_name.delete(0 , END)
			ent_name.focus()
			return
		if (not name.isalpha()) :
			showerror("Error " ,"Name must be in character text only")
			ent_name.delete(0 , END)
			ent_name.focus()
			return

		esalary = (ent_salary.get())
		if (esalary == "" ) or (esalary.strip() == "") : 
			showerror("Failed " ,"Salary should not be empty")
			ent_salary.delete(0 , END)
			ent_salary.focus()
			return
		try : 
			salary = float(esalary)
		except : 
			showerror("Error " ,"Invalid salary")
			ent_salary.delete(0 , END)
			ent_salary.focus()
			return
		cursor.execute(sql%(id,name,salary))
		con.commit()
		showinfo("Success" , "Records saved ")
		ent_id.delete(0 , END)
		ent_name.delete(0, END)
		ent_salary.delete(0 , END)
		ent_id.focus()
		return

	except Exception as e :
		con.rollback()
		showerror("Failed ", e)
		ent_id.delete(0 , END)
		ent_name.delete(0, END)
		ent_salary.delete(0 , END)
		ent_id.focus()
		return

	finally : 
		if con is not None :
			con.close()		

btn_save = Button(sw , text = "Save " , font = f , width = 10 , command = save)
btn_save.pack(pady = 10)

btn_back = Button(sw , text = "Back " , font = f , width = 10 , command = back )
btn_back.pack(pady = 10) 
sw.withdraw()


tw = Toplevel(mw)
tw.title("View")
tw.geometry("700x700+400+50")
tw.configure(bg = "white")
f = ("Calibri" , 30 , "bold")

scr_view = ScrolledText(tw , font = f , width = 32 , height = 8 )
scr_view.pack(pady = 20)

btn_back1 = Button(tw , text = "Back" , font = f , width = 10 , command = back1)
btn_back1.place(x = 250 , y = 500 )

tw.withdraw()

fw = Toplevel(mw)
fw.title("Update")
fw.geometry("700x700+400+50")
fw.configure(bg = "white")
f = ("Calibri" , 30 , "bold")

uw_lab_id = Label(fw , text = "Enter id : " , font = f  )
uw_lab_id.pack(pady = 10)

uw_ent_id = Entry(fw , font = f )
uw_ent_id.pack(pady = 10)

uw_lab_name = Label(fw , text = "Enter name : " , font = f  )
uw_lab_name.pack(pady = 10)

uw_ent_name = Entry(fw , font = f )
uw_ent_name.pack(pady = 10)

uw_lab_salary = Label(fw , text = "Enter salary : ", font = f )
uw_lab_salary.pack(pady = 10)

uw_ent_salary = Entry(fw , font = f )
uw_ent_salary.pack(pady = 10)

def save2() : 
	con = None
	try  :
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "update emp set name ='%s' , salary='%f' where id = '%d' "
		id = uw_ent_id.get()
		id = id.strip()    
		if (id == "") or (id.strip() == "" ) : 
			showerror("Failed " , "Id should not be empty")
			uw_ent_id.delete(0 , END)
			uw_ent_id.focus()
			return
		try : 
			id = int(id)
		except ValueError : 
			showerror("Failed" , "Id must be in integer only")
			uw_ent_id.delete(0 , END)
			uw_ent_id.focus()
			return

		if (id < 1) : 
			showerror("Failed" , "Minimum id should be 1 ")
			uw_ent_id.delete(0 , END)
			uw_ent_id.focus()
			return

		name = uw_ent_name.get()
		if (name == "") or (name.strip() == "") : 
			showerror("Failed" , "Name should not be empty")
			uw_ent_name.delete(0 , END)
			uw_ent_name.focus()
			return

		if (not name.isalpha()) : 
			showerror("Failed" , "Invalid name")
			uw_ent_name.delete(0 , END)
			uw_ent_name.focus()
			return

		salary = uw_ent_salary.get()
		if (salary == "") or (salary.strip() == "") : 
			showerror("Failed" , "Salary should not be empty")
			uw_ent_salary.delete(0 , END)
			uw_ent_salary.focus()
			return
		try :
			salary = float(salary)
		except ValueError :
			showerror("Failed" , "Invalid salary" )
			uw_ent_salary.delete(0 , END)
			uw_ent_salary.focus()
			return
		cursor.execute(sql%(name,salary,id))
		if cursor.rowcount == 1 : 
			con.commit()
			showinfo("Success" , "Records updated")
			uw_ent_id.delete(0 , END)
			uw_ent_name.delete(0 , END)
			uw_ent_salary.delete(0 , END)
			uw_ent_id.focus()
			return
		else : 
			showerror("Failed" , "Record does not exists ")
			uw_ent_id.delete(0 , END)
			uw_ent_name.delete(0 , END)
			uw_ent_salary.delete(0 , END)
			uw_ent_id.focus()
			return

	except Exception as e : 
		con.rollback()
		showerror("Issue" , e )
		uw_ent_id.delete(0 , END)
		uw_ent_name.delete(0 , END)
		uw_ent_salary.delete(0 , END)
		uw_ent_id.focus()
		return

	finally  :
		if con is not None : 
			con.close()


btn_save2 = Button(fw , text = "Save" , font = f , width = 10 , command = save2)
btn_save2.pack(pady = 10)

btn_back2 = Button(fw , text = "Back" , font = f , width = 10 , command = back2)
btn_back2.pack(pady = 10)

fw.withdraw()

nw = Toplevel(mw)
nw.title("Delete Employee")
nw.geometry("700x700+400+50")
nw.configure(bg = "white")
f = ("Calibri" , 30 , "bold")

dw_lab_id = Label(nw , text = "Enter id : " , font =  f )
dw_lab_id.pack(pady = 10)

dw_ent_id = Entry(nw , font = f )
dw_ent_id.pack(pady = 10)

def save3() : 
	con = None 
	try :
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "delete from emp where id = '%d' "
		id = dw_ent_id.get()
		if (id == "") or (id.strip() == "") : 
			showerror("Failed" , "Id should not be empty") 	
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
		try : 
			id = int(id)
		except : 
			showerror("Failed" , "Id must be integer only") 	
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
		cursor.execute(sql %(id))
		if cursor.rowcount == 1 :
			con.commit()
			showinfo("Success" , "Record deleted")
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
		else :
			showerror("Failed" , "Record does not exists ")
			dw_ent_id.delete(0 , END)
			dw_ent_id.focus()
			return
	except Exception as e :
		con.rollback()
		showerror("Issue" , e)
		dw_ent_id.delete(0 , END)
		dw_ent_id.focus()
		return

	finally : 
		if con is not None :
			con.close()

btn_save3 = Button(nw , text = "Save" , font = f , width = 10 , command = save3 )
btn_save3.pack(pady = 10)

btn_back3 = Button(nw , text = "Back" , font = f , width = 10 , command = back3)
btn_back3.pack(pady = 10)

nw.withdraw()

def chart():
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = '''SELECT name, salary FROM emp ORDER BY salary DESC LIMIT 5'''
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		salary = []
		for i in data:
			name.append(i[0])
			salary.append(i[1])
		plt.figure(figsize=(8,6))
		c = ['green', 'blue', 'black', 'red' , 'orange' ]
		plt.rcParams.update({'text.color': "red", 'axes.labelcolor': "gray"})
		ax = plt.axes()
		ax.set_facecolor("lightblue")  # Setting the background color of the plot using facecolor


		plt.bar(name, salary ,  color= c)
		plt.xlabel("Names of Employee" , fontsize = 15)
		plt.ylabel("Salary of Employee", fontsize = 15)
		plt.title("Top 5 Highest Salaried Employee", fontsize = 15)
		plt.grid()
		plt.show()
	except Exception as e:
        	showerror("issue ", e)
	        con.rollback()
	finally:
		if con is not None:
			con.close()

btn_bar = Button(mw , text = "BarChart" , font = f , width = 10 , command = chart )
btn_bar.pack(pady = 10)

def on_closing():
    if askyesno("Quit", "Do you want to quit?"):
        mw.destroy()

mw.protocol("WM_DELETE_WINDOW", on_closing)
sw.protocol("WM_DELETE_WINDOW", on_closing)
tw.protocol("WM_DELETE_WINDOW", on_closing)
fw.protocol("WM_DELETE_WINDOW", on_closing)
nw.protocol("WM_DELETE_WINDOW", on_closing)

mw.mainloop()
