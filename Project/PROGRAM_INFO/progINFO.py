#! C:\Users\patna\AppData\Local\Programs\Python\Python310\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="Rays",passwd="rays123@",database="university_management_system")
x=con.cursor()
f=cgi.FieldStorage()
try:
    u_name = f.getvalue('u_n')
    p_name = f.getvalue('p_n')
    lateral = f.getvalue('lat2')
    min_dur = f.getvalue('dur')
    max_dur = f.getvalue('dur2')
    eligibility = f.getvalue('e')
    session = f.getvalue('sess')
    pro_fees = f.getvalue('pro')
    adm_fees = f.getvalue('adm')
    exam_fees = f.getvalue('exam')
    ser_fees = f.getvalue('ser')
    ref_fees = f.getvalue('ref')
    v=(u_name,p_name,lateral,min_dur,max_dur,eligibility,session,pro_fees,adm_fees,exam_fees,ser_fees,ref_fees)
    print(v)
    x.execute("insert into program_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",v)
    con.commit()
    print("Successfully Inserted!")
except:
    print("Data is not Inserted!") 