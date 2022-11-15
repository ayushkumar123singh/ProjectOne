#! C:\Users\patna\AppData\Local\Programs\Python\Python310\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="Rays",passwd="rays123@",database="university_management_system")
x=con.cursor()
x.execute("select distinct u_name from university_info")
res=x.fetchall()
print(""" <select class="div1" id="u_n" name="uni_name"> <option value="Select a university" hidden>Select a University</option>""")
for a in res: 
    print("<option>"+a[0]+"</option>")
print("</select>,,,")
####################################################################################################################################################
x.execute("select distinct p_name from program_details")
res=x.fetchall()
print("""<select class="div2" id="c_n" name="cou_name"> <option value="Select a Course" hidden>Select a Course</option>""")
for a in res: 
    print("<option>"+a[0]+"</option>")
print("</select>,,,")
####################################################################################################################################################
x.execute("select distinct mode from university_info")
res=x.fetchall()
print("""<select class="div3" id="m_n" name="mo_name"> <option value="Select a mode" hidden>Select a mode</option>""")
p=set()
for a in res:
    a=a[0].split(',')
    for t in a:
        p.add(t)
for a in p:
    print("<option>"+a+"</option>")
print("</select>")
#apple
#ball
