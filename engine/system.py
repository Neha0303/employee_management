import sys,os, PyQt5 as pqt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from tabulate import tabulate
import engine.base as base

''' This creates the main window of the application '''

def window():
    ''' This creates the window '''

    app = QApplication(sys.argv)
    win = QWidget()
    path = os.getcwd()

    # Stylizing Window
    win.setStyleSheet("background-color:white")
    win.setGeometry(500, 70, 0, 0)
    win.setFixedSize(700, 700)
    win.setWindowTitle("Management")

    style = "font-size:24px; border: 2px solid black;"
    #Adding buttons
    def create_button(title,x,y,xp,yp):
        buttonx = QPushButton(title,win)
        buttonx.resize(x,y)
        buttonx.move(xp,yp)
        buttonx.setStyleSheet(style)
        return buttonx

    show = create_button("Show Employee",300,100,200,20)
    add = create_button("Add Employee",300,100,200,140)
    remove = create_button("Remove Employee",300,100,200,260)
    showAll = create_button("Show all",300,100,200,380)
    removeAll = create_button("Remove all",300,100,200,500)

    #Creating popups
    def showEmployee():
        xdialog = QDialog(win)
        xdialog.setWindowTitle("Add employee")
        dbInput = QLineEdit(xdialog)
        dbInput.setPlaceholderText("Employee ID")
        dbInput.setGeometry(100,10,300,100)
        dbInput.setStyleSheet("font-size:24px;")
        Buttonx = QPushButton(xdialog)
        Buttonx.setText("Show employee")
        Buttonx.setGeometry(100,150,300,100)
        Buttonx.setStyleSheet(style)

        def showDatax():
            values = base.select_specific_from_table(dbInput.text())
            data = tabulate(values,headers = ["ID","Name","Age","Salary","Title"],tablefmt='psql')
            print(data)
            xdialog.close()
        
        Buttonx.clicked.connect(showDatax)
        xdialog.setFixedSize(500, 400)
        xdialog.exec_()
    
    def fshowAll():
        values = base.select_all_from_table()
        data = tabulate(values,headers = ["ID","Name","Age","Salary","Title"],tablefmt='psql')
        print(data)
        
    
    def removeOne():
        xdialog = QDialog(win)
        xdialog.setWindowTitle("Remove employee")
        dbInput = QLineEdit(xdialog)
        dbInput.setPlaceholderText("Employee ID")
        dbInput.setGeometry(100,10,300,100)
        dbInput.setStyleSheet("font-size:24px;")
        Buttonx = QPushButton(xdialog)
        Buttonx.setText("Remove employee")
        Buttonx.setGeometry(100,150,300,100)
        Buttonx.setStyleSheet(style)

        def showDatax():
            base.drop_employee(dbInput.text())
            print(f"Deleted Employee with ID {dbInput.text()}")
            xdialog.close()
        
        Buttonx.clicked.connect(showDatax)
        xdialog.setFixedSize(500, 400)
        xdialog.exec_()

    def addOne():
        vdialog = QDialog(win)
        vdialog.setWindowTitle("Add employee")

        def create_inputs(title,xp,yp):
            dbInput = QLineEdit(vdialog)
            dbInput.setPlaceholderText(title)
            dbInput.setGeometry(xp,yp,300,100)
            dbInput.setStyleSheet("font-size:24px;")
            return dbInput
        
        empid = create_inputs("Employee Id",200,90)
        name = create_inputs("Employee Name",200,200)
        age = create_inputs("Employee Age",200,310)
        salary = create_inputs("Employee Salary",200,420)
        title = create_inputs("Employee Title",200,530)

        def showData():
            inputs = [empid,name,age,salary,title]
            values = []
            for item in inputs:
                values.append(item.text())
            base.insert_values(values)
            vdialog.close()
        
        Buttonx = QPushButton(vdialog)
        Buttonx.setText("Add employee")
        Buttonx.setGeometry(200,650,300,100)
        Buttonx.setStyleSheet(style)
        Buttonx.clicked.connect(showData)

        vdialog.setFixedSize(700, 800)
        vdialog.exec_()
    
    def fremoveAll():
        base.drop_table()
        print("Deleted all employees")
    

    functions = [showEmployee,fshowAll,removeOne,addOne,fremoveAll]
    buttons = [show,showAll,remove,add,removeAll]

    def assign_click(button,func):
        button.clicked.connect(func)    
    
    # Assigning button clicks
    for item in range(len(functions)):
        assign_click(buttons[item],functions[item])
    
    # starting Activities
    win.show()
    sys.exit(app.exec())
