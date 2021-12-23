host = "127.0.0.1"
user = "postgres"
password = "qwerty"
db_name = "course_work"
port = 5432



import pandas as pd
import pandas.io.sql as psql
import psycopg2
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from tkinter import Text

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth',None)
pd.set_option('display.width', 0)



# Будем выбирать таблицу из которой надо выгрузить данные
def data():
	reqest = tabel_name_.get()
	if not (reqest == 'children' or reqest == 'parents' or reqest == 'money' or reqest == 'contract' or reqest == 'registration'):
		error1()
		return

	with connection.cursor() as cursor:
		cursor.execute(

			

			"SELECT * FROM " + reqest


					
			)
		res = list(cursor)
	
	info = psql.read_sql("SELECT * FROM " + reqest, connection)


	with open(reqest, "w+") as f:
		for i in res:
			f.write(' '.join(str(res) for res in i) + '\n')
			
		
	data_text = tk.Text(tab2, height = 40, width = 150)
	data_text.place(x = 50, y = 100)		
			
	#file_name = filedialog.askopenfile()				
	#data = file_name.read()	
	data_text.insert(INSERT, info)
	

	



def add_data():
	name = name_.get()
	last_name = last_name_.get()
	otchestvo = otchestvo_.get()
	group = group_.get()
	gender = gender_.get()
	skips = skips_.get()
	if not (name and otchestvo and last_name and group and gender and skips):
		error()
		return
	else:
		good()

		
	
	val = "("  +  "'" + name + "'" + ", " +  "'" + last_name +  "'" + ", "  +  "'" + otchestvo +  "'" + ", "  +  "'"  + group  +  "'"  + ", "  + "'" + gender +  "'"  + ", " + skips + ")" + ";"


	with connection.cursor() as cursor:
		cursor.execute(

			

			"INSERT INTO children (first_name, last_name, otchestvo, grroup, gender, skips) VALUES " + val
		
			)
	print("Ребёнок успешно добавлен в список!")	




def remove_data():
	id_child = delete_child_.get()	
	id_child = str(id_child)
	
	with connection.cursor() as cursor:
		cursor.execute(

			

			"DELETE FROM children WHERE id_child = " + id_child
		
			)



def dolg():
#	change = tk.Label(tab2, text = "Номер контракта для изменения данных")
#	change.place(x = 770, y = 50)
	

	info = psql.read_sql("SELECT * FROM money WHERE operation = 'False'", connection)
	data_text = tk.Text(tab2, height = 40, width = 150)
	data_text.place(x = 50, y = 100)
	data_text.insert(INSERT, info)

#	_change = tk.Entry(tab2, width = 20)
#	_change.place(x = 1070, y = 50)

	
	


def change_dolg():
	change = _change.get()
	change = str(change)
	if not (change):
		error()
		return
	with connection.cursor() as cursor:
		cursor.execute(

			"UPDATE money SET operation = 'true' WHERE fk_number_contract = " + change 
		
			)	
	good1()
	


	

	


def error():
	tk.messagebox.showerror('Error!', 'Не все данные заполнены!') 

def good():
	tk.messagebox.showinfo('Операция выполнена!', 'Ребёнок добавлен успешно!')

def error1():
	tk.messagebox.showerror('Error!', 'Таблицы с таким именем не существует!')
def good1():
	tk.messagebox.showinfo('Операция выполнена!', 'Статус успешно ищменён!')











try:
	# Firstly we have to connect to our DB
	connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )

	connection.autocommit = True

	window = Tk()  
	window.title("Детский сад Ромашка") 
	window.geometry('1300x900')   
	window.resizable(False, False)
	
	
	tab_control = ttk.Notebook(window)  
	tab1 = ttk.Frame(tab_control)  
	tab2 = ttk.Frame(tab_control)
	tab3 = ttk.Frame(tab_control)  
	tab_control.add(tab1, text='Добавить ребёнка')  
	tab_control.add(tab2, text='Узнать информацию из таблицы')
	tab_control.add(tab3, text='Удалить ребёнка из списка')  
	tab_control.pack(expand=1, fill='both')
	





	_name = tk.Label(tab1, text = "Введите имя")
	_name.place(x = 150, y = 200)
	name_ = tk.Entry(tab1, width = 20)
	name_.place(x = 350, y = 200)

	_last_name = tk.Label(tab1, text = "Введите фамилию")
	_last_name.place(x = 150, y = 250)
	last_name_ = tk.Entry(tab1, width = 20)
	last_name_.place(x = 350, y = 250)

	_otchestvo = tk.Label(tab1, text = "Введите отчество")
	_otchestvo.place(x = 150, y = 300)
	otchestvo_ = tk.Entry(tab1, width = 20)
	otchestvo_.place(x = 350, y = 300)

	_group = tk.Label(tab1, text = "Введите группу")
	_group.place(x = 150, y = 350)
	group_ = tk.Entry(tab1, width = 20)
	group_.place(x = 350, y = 350)

	_gender = tk.Label(tab1, text = "Введите пол")
	_gender.place(x = 150, y = 400)
	gender_ = tk.Entry(tab1, width = 20)
	gender_.place(x = 350, y = 400)

	_skips = tk.Label(tab1, text = "Введите кол-во пропусков")
	_skips.place(x = 150, y = 450)
	skips_ = tk.Entry(tab1, width = 20)
	skips_.place(x = 350, y = 450)



	tabel_name = tk.Label(tab2, text = "Введите название таблицы, из которой хотите получить данные")
	tabel_name.place(x = 50, y = 50)
	tabel_name_ = tk.Entry(tab2, width = 20)
	tabel_name_.place(x = 520, y = 50)



	delete_child = tk.Label(tab3, text = "Введите номер (id_child) ребёнка в списке")
	delete_child.place(x = 100, y = 50)
	delete_child_ = tk.Entry(tab3, width = 20)
	delete_child_.place(x = 410, y = 50)




	change = tk.Label(tab2, text = "Номер контракта для изменения данных")
	change.place(x = 770, y = 50)
	_change = tk.Entry(tab2, width = 20)
	_change.place(x = 1070, y = 50)




	btn = tk.Button(tab1, text = 'Добавить ребёнка', command = add_data).place(x = 100, y = 800)
	btn1 = tk.Button(tab2, text = 'Узнать информацию из таблицы', command = data).place(x = 100, y = 800)
	btn2 = tk.Button(tab3, text = 'Удалить ребёнка', command = remove_data).place(x = 100, y = 800)
	btn3 = tk.Button(tab2, text = 'Показать список должников', command = dolg).place(x = 500, y = 800)
	btn4 = tk.Button(tab2, text = 'Изменить статус оплаты', command = change_dolg).place(x = 900, y = 800)
	
	




	window.mainloop()
	







except Exception as _ex:
	print('Ошибка, что-то пошло не так!', _ex)

finally:
	if connection:
		connection.close()
#		print("Операция выполнена успешно!!")