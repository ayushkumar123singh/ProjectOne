#! C:\Users\patna\AppData\Local\Programs\Python\Python310\python.exe
print ("Content-Type: text/html\r\n\r\n")
import cgi
import mysql.connector
con=mysql.connector.connect(host="localhost",user="Rays",passwd="rays123@",database="university_management_system")
x=con.cursor()
f=cgi.FieldStorage()
try:
    t2=f.getvalue('a')
    un2=f.getvalue('b')
    cn2=f.getvalue('c')
    mn2=f.getvalue('d')
    if(t2=='delete'):
        lst=[]
        url="select * from program_details where "
        flag=False
        if un2!='ua':
            if flag:
                url=url+"and u_name=%s"
            else:
                url=url+" u_name=%s"
            flag=True
            lst.append(un2)
        if cn2!='ca':
            if flag:
                url=url+' and p_name=%s'
            else:
                url=url+' p_name=%s'
            flag=True
            lst.append(cn2)
        if mn2!='ma':
            if flag:
                url=url+' and mode=%s'
            else:
                url=url+' mode=%s'
            flag=True
            lst.append(mn2)
        if flag:
            lst=tuple(lst)
            x.execute(url,lst)
            res=x.fetchall()
            print("""<table class="t"><tr><td class="t11">University Name</td><td class="t11">Mode</td><td class="t11">Course</td><td class="t11">Lateral</td><td class="t11">Min duration</td><td class="t11">Max duration</td><td class="t11">Eligibility</td><td class="t11">session</td><td class="t11">pro_fees</td><td class="t11">adm_fees</td><td class="t11">exam_fees</td><td class="t11">ser_fees</td><td class="t11">ref_fees</td><td class="t11"></td></tr>""")
            for a in res:
                if a[3]==None:
                    s='0'
                else:
                    s=a[3]
                print("<tr class=t22><td>"+a[0]+"</td><td>"+a[1]+"</td><td>"+a[2]+"</td><td>"+s+"</td><td>"+str(a[4])+"</td><td>"+str(a[5])+"</td><td>"+str(a[6])+"</td><td>"+str(a[7])+"</td><td>"+str(a[8])+"</td><td>"+str(a[9])+"</td><td>"+str(a[10])+"</td><td>"+str(a[11])+"</td><td>"+str(a[12])+"""</td><td><input class="div7" type="button" name="delete" id="del" value="Delete"></td></tr>""")
            print("""</table>""")
        else:
            print("select any one item")
    else:
        x.execute("select distinct u_name from university_info")
        res=x.fetchall()
        print(""" <select class="div1" id="u_n1" name="uni_name"><option value="ua" hidden>Select a University</option>""")
        for a in res:
            print("<option>"+a[0]+"</option>")
        print("</select>,,,")
        ####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        x.execute("select distinct p_name from program_details")
        res=x.fetchall()
        print("""<select class="div2" id="c_n1" name="cou_name"><option value="ca" hidden>Select a Course</option>""")
        for a in res:
            print("<option>"+a[0]+"</option>")
        print("</select>,,,")
        ####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
        x.execute("select distinct mode from university_info")
        res=x.fetchall()
        print(""" <select class="div3" id="m_n1" name="mo_name"><option value="ma" hidden>Select a mode</option>""")
        p=set()
        for a in res:
            a=a[0].split(',')
            for t in a:
                p.add(t)
        for a in p:
            print("<option>"+a+"</option>")
        print("</select>")
except:
    print("unsuccess")
