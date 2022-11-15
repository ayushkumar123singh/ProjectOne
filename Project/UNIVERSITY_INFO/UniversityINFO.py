#! C:\Users\patna\AppData\Local\Programs\Python\Python310\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="Rays",passwd="rays123@",database="university_management_system")
x=con.cursor()
f=cgi.FieldStorage()
try:
    u_name = f.getvalue('u_n')
    mode = f.getvalue('m')
    u_reg = f.getvalue('u_r')
    link = f.getvalue('e')
    v=(u_name,mode,u_reg,link)
    print(v)
    x.execute("insert into university_info values(%s,%s,%s,%s)",v)
    con.commit()
    print("Successfully Inserted!")
except:
    print("Data is not Inserted!") 