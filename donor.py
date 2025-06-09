import mysql.connector
from flask import session
from datetime import date


class donor_operation:
    def connection(self):
        con=mysql.connector.connect(host="localhost",port="3306",user="root", password="root",database="donation")
        # con=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="donation")
        return con


    def donor(self,dname,demail,dpan,damt):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into donar(dname,demail,dpan,damt,caseid) values(%s,%s,%s,%s,%s)"

        record=[dname,demail,dpan,damt,session["caseid"]]
        mycursor.execute(sq,record)
        db.commit()
        # retrivee donor id
        sq="select did from donar order by did desc limit 1"
        mycursor.execute(sq)
        row=mycursor.fetchall()
        session['did']=row[0][0]
        mycursor.close()
        db.close()
        return  

    
    def payment(self,payid,ord_id):
        db=self.connection()
        mycursor=db.cursor()
        sq="select damt from donar where did=%s"
        record =[session['did']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        amt=row[0][0]
        payable = amt - (amt * .05)
        sq="insert into payment (caseid,payid,ord_id,amt,donor_id,pay_date,payable) values(%s,%s,%s,%s,%s,%s,%s)"
        
        record=[session["caseid"],payid,ord_id,amt,session['did'],date.today(),payable]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return  
    
    def pay_sum(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select sum(payable) from payment where caseid=%s"
        record =[session['caseid']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        a= row[0][0]
        if (a==None):
            return 0
        else:
            return a

    def receipt(self,payid):
        db=self.connection()
        mycursor=db.cursor()
        sq="select dname,demail,dpan,payid,amt,pay_date from donar d, payment p where d.did=p.donor_id and p.payid=%s"
        record =[payid]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        return row



    