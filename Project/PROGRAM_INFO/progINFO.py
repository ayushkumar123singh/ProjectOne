#! C:\Users\patna\AppData\Local\Programs\Python\Python310\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="Rays",passwd="rays123@",database="university_management_system")
x=con.cursor()
f=cgi.FieldStorage()
try:
    t=f.getvalue('x')
    if(t=='edit'):
        u_name = f.getvalue('u_n')
        mode = f.getvalue('m_n')
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
        v=(u_name,mode,p_name,lateral,min_dur,max_dur,eligibility,session,pro_fees,adm_fees,exam_fees,ser_fees,ref_fees)
        print(v)
        x.execute("insert into program_details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",v)
        con.commit()
        print("Successfully Inserted!")
    else:
        x.execute("select distinct u_name from university_info")
        res=x.fetchall()
        print("""<select id="u_n" class="t1" name="uni_name" onfocusin="cleardata('u_n','U_N')"> <option value="Select a University" hidden>Select a University</option>""")
        for a in res:
            print("<option>"+a[0]+"</option>")
        print("<select>,,,")
        #########################################################################################################################################################
        x.execute("select distinct mode from university_info")
        res=x.fetchall()
        print("""<select class="t1a" id="m_n" name="mo_name" onfocusin="cleardata('m_n','M_N')"> <option value="ma" hidden>Select a mode</option>""")
        p=set()
        for a in res:
            a=a[0].split(',')
            for t in a:
                p.add(t)
        for a in p:
            print("<option>"+a+"</option>")
        print("</select>")
except:
    print("Data is not Inserted!") 