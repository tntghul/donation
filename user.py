import mysql.connector
from flask import session
from datetime import date



class user_operation:
    def connection(self):
        con=mysql.connector.connect(host="localhost",port="3306",user="root",password="root",database="donation")
        return con


    def contact(self,cname,cemail,csub,cmobile,cdesc):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into contact (cname,cemail,csub,cmobile,cdesc) values (%s,%s,%s,%s,%s)"
        record=[cname,cemail,csub,cmobile,cdesc]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return

    def user_signup(self,name,id,mobile,email,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into user (name,id,mobile,email,password) values (%s,%s,%s,%s,%s)"
        record=[name,id,mobile,email,password]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return

    def user_delete(self,email):
        db=self.connection()
        mycursor=db.cursor()
        sq="delete from user where email=%s"

        record=[email]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return 

    def user_login(self,email,password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select name,email,mobile,password from user where email=%s and password=%s"
        record=[email,password]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==0):
            return 0
        else:
            session['name']=row[0][0]
            session['email']=row[0][1]
            session['mobile']=row[0][2]
            return 1

    def ppic(self,propic):
        db=self.connection()
        mycursor=db.cursor()
        sq="select proid,user_email from profile where user_email=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==0):
            sq="insert into profile (propic,user_email) values(%s,%s)"
            record=[propic,session['email']]
            mycursor.execute(sq,record)
            

        else:
            sq="update profile set propic = %s where user_email=%s"
            record=[propic,session['email']]
            mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return


    def dppic(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select propic,user_email from profile where user_email=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        return row


    def user_profile(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select name,id,email,mobile from user where email=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        return row


    def user_profile_update(self,name,mobile):
        db=self.connection()
        mycursor=db.cursor()
        sq="update user set name=%s,mobile=%s where email=%s"

        record=[name,mobile,session['email']]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        session['name']=name
        session['mobile']=mobile
        return  
    
    def user_password(self,old_password,new_password):
        db=self.connection()
        mycursor=db.cursor()
        sq="select password from user where email=%s and password=%s"
        record=[session['email'],old_password]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        rc=mycursor.rowcount
        if(rc==1):
            sq="update user set password=%s where email=%s"
            record=[new_password,session['email']]
            mycursor.execute(sq,record)
            db.commit()
            mycursor.close()
            db.close()
            return 1
        
        return 0


    def addcase(self, pname, pid, gender, age, hname, haddress, cdetails, paddress, amt, blood, p1, p2, p3):
        try:
            db = self.connection()
            mycursor = db.cursor()
            sq = """
                INSERT INTO patient 
                (pname, pid, gender, age, hname, haddress, cdetails, paddress, amt, blood, p1, p2, p3, user_email) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            record = [pname, pid, gender, age, hname, haddress, cdetails, paddress, amt, blood, p1, p2, p3, session['email']]

            mycursor.execute(sq, record)
            db.commit()
            print("Record inserted successfully")

        except Exception as e:
            print("Error inserting record:", e)
            db.rollback()

        finally:
            mycursor.close()
            db.close()


    
    def photo(self,p1,p2,p3):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into photo (p1,p2,p3) values(%s,%s,%s)"

        record=[p1,p2,p3]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return  
    

    def bank_details(self,bname,pan,bank,account,bmobile):
        db=self.connection()
        mycursor=db.cursor()
        sq="insert into bank_details (bname,pan,bank,account,bmobile) values(%s,%s,%s,%s,%s)"

        record=[bname,pan,bank,account,bmobile]
        mycursor.execute(sq,record)
        db.commit()
        mycursor.close()
        db.close()
        return  
    

    def case_details(self):
        db = self.connection()
        mycursor = db.cursor()
        sq = "SELECT DISTINCT caseid, pname, pid, gender, age, hname, haddress, cdetails, paddress, amt, blood, p1, p2, p3 FROM patient WHERE user_email = %s"
        record = [session['email']]
        mycursor.execute(sq, record)
        row = mycursor.fetchall()

        print("ROWS FETCHED:", row)  # Debug print to check for duplicates

        db.close()
        return row


    def case_detail(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,hname,haddress,cdetails,paddress,amt,blood,p1,p2,p3 from patient where user_email!=%s"
        record=[session['email']]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        return row

    def case(self,caseid):
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,hname,haddress,cdetails,paddress,amt,blood,p1,p2,p3 from patient where caseid=%s"
        record=[caseid]
        mycursor.execute(sq,record)
        row=mycursor.fetchall()
        session['caseid']=row[0][0]  
        return row

    def all_cases(self,caseid):
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,hname,haddress,cdetails,paddress,amt,blood,p1,p2,p3 from patient where status=1"
        
        mycursor.execute(sq)
        row=mycursor.fetchall()
        session['caseid']=row[0][0]
        return row

    def complete(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,hname,haddress,cdetails,paddress,amt,blood,p1,p2,p3 from patient where status=0"
        
        mycursor.execute(sq)
        row=mycursor.fetchall()
        return row

    def complete2(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select caseid,pname,pid,gender,age,hname,haddress,cdetails,paddress,amt,blood,p1,p2,p3 from patient where useremail=%s status=0"
        record=[session[email]]
        mycursor.execute(sq)
        row=mycursor.fetchall()
        return row

    def count(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select count(*),sum(amt) from patient"
       
        mycursor.execute(sq)
        row=mycursor.fetchall()
        return row

    def count2(self):
        db=self.connection()
        mycursor=db.cursor()
        sq="select count(*),sum(payable) from payment"
       
        mycursor.execute(sq)
        row=mycursor.fetchall()
        return row
