import mysql.connector
from flask import session
from datetime import date


class admin_operation:
    def connection(self):
        con=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="donation")
        return con




    def admin_login(self,adminid,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select adminid,password from admin where adminid=%s and password=%s"
        record=[adminid,password]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==0):
            return 0
        else:
            session['adminid']=row[0][0]
            session['password']=row[0][1]
            
            return 1
    
    def admin_dashboard(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select pname,gender,cdetails,p.caseid,pa.amt,sum(payable) from payment p, patient pa where p.caseid = pa.caseid group by p.caseid"
        
        mycursor.execute(sq)
        row=mycursor.fetchall()
        return row

    def status_update(self,caseid):
        db=self.connection()
        mycursor=db.cursor()
        sq="update patient set status =0 where caseid=%s"
        record =[caseid]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return