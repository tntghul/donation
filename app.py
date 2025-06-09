from flask import Flask,render_template,request,redirect,url_for,flash,session,send_file
from user import user_operation
from encryption import Encryption
from myrandom import randomnumber
from myemail import Email
from validate import myvalidate
from datetime import datetime
from donor import donor_operation
from admin import admin_operation
import razorpay

app=Flask(__name__)
app.secret_key='hdjdkeloejel45625'

client = razorpay.Client(auth=("rzp_test_PkxyeF1OLcy3d8", "anNC61WKeRqubB3e5oQIbDbK"))


m = Email(app)   # activate Email object


@app.route('/')
def index():
    if('email' in session):
        session.clear()
        return render_template("index.html")
    else:
        caseid= request.args.get('caseid')
        ob= user_operation()
        data=ob.complete()
        record=ob.all_cases(caseid)

        return render_template("index.html",record=record)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/about2')
def about2():
    return render_template("about2.html")

   
@app.route('/contact',methods=['GET','POST'])
def contact():
    if(request.method=='GET'):
        return render_template("contact.html")
    elif(request.method=='POST'):
        cname=request.form['cname']
        cemail=request.form['cemail']
        csub=request.form['csub']
        cmobile=request.form['cmobile']
        cdesc=request.form['cdesc']

        ob = user_operation()
        ob.contact(cname,cemail,csub,cmobile,cdesc)
        flash("Message sent successfully!!")
        return redirect(url_for('user_dashboard'))            
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_dashboard')) 


@app.route('/contact2',methods=['GET','POST'])
def contact2():
    if(request.method=='GET'):
        return render_template("contact2.html")
    elif(request.method=='POST'):
        cname=request.form['cname']
        cemail=request.form['cemail']
        csub=request.form['csub']
        cmobile=request.form['cmobile']
        cdesc=request.form['cdesc']

        ob = user_operation()
        ob.contact(cname,cemail,csub,cmobile,cdesc)
        flash("Message sent successfully!!")
        return redirect(url_for('user_dashboard'))            
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_dashboard')) 
    

@app.route('/user_signup',methods=['GET','POST'])
def user_signup():
    if(request.method=='GET'):
        return render_template("user_signup.html")
    elif(request.method=='POST'):
        name=request.form['name']
        id=request.form['id']
        mobile=request.form['mobile']
        email=request.form['email']
        password=request.form['password']

        e = Encryption()
        password = e.convert(password)
        #---insertion-------------------
        ob = user_operation() # object create
        ob.user_signup(name,id,mobile,email,password)
        #------ email otp send-----------------
        # global otp
        # otp = randomnumber()
        # subject="verification code"
        # message="hi "+name+"\nYour OTP is: "+ str(otp)+"\n Thank You"
        # m.compose_mail(subject,email,message)  # calling
        # return render_template("user_email_verify.html",email=email)
        return render_template ("user_login.html")
    else:
        return "error"

@app.route('/user_email_verify',methods=['GET','POST'])
def user_email_verify():
    if(request.method=='POST'):
        if(str(otp)==request.form['otp']):
            flash("Your Email is Verified... You can Login Now!!")
            return render_template('user_login.html')
        else:
            email=request.form['email']
            ob = user_operation()
            ob.user_delete(email)
            flash("Invalid OTP...Your Email is not verified.. Try Again to Register!!")
            return redirect(url_for('user_signup'))
    else:
        return "page can not be access!!"        

@app.route('/user_login',methods=['GET','POST'])
def user_login():
    
    if(request.method=='GET'):
        return render_template("user_login.html")
    elif(request.method=='POST'):
        email = request.form['email']
        password = request.form['password']
        #-- validatation ---------------
        v = myvalidate()
        frm=[email,password]
        if(not v.required(frm)):
            flash("field can not be empty!!")
            return redirect(url_for('user_login'))

        #-- password encryption---------
        e = Encryption()
        password = e.convert(password)

        ob = user_operation()
        rc=ob.user_login(email,password)
        if(rc==0):
            flash("invalid email or password!!")
            return redirect(url_for('user_login'))
        else:
            return redirect(url_for('user_dashboard'))
            # return session['name']
    else:
        return "error"


@app.route('/user_logout',methods=['GET','POST'])
def user_logout():
    if('email' in session):
        if(request.method=='GET'):
            session.clear()
            return redirect(url_for('index'))
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))


@app.route('/user_dashboard',methods=['GET','POST'])
def user_dashboard():
    if('email' in session):
        if(request.method=='GET'):
            
            ob = user_operation()
            record=ob.case_detail()
            
            
            return render_template("user_dashboard.html",record=record)
            
        else:
            flash("you are not authorized to access this page.. please login first")
            return redirect(url_for('user_login'))


@app.route('/ppic',methods=['GET','POST'])
def ppic():
    if('email' in session):
        if(request.method=='POST'):
            upic=request.files['upic']
            propic=upic.filename
            upic.save("static/dp/"+propic)
            ob = user_operation()
            ob.ppic(propic)
            
            return redirect(url_for("user_profile"))
        else:
            
            flash("your profile pic successfully uploaded!!")
            return "error"
    
    


@app.route('/user_profile',methods=['GET','POST'])
def user_profile():
    if('email' in session):
        if(request.method=='GET'):
            ob = user_operation()
            record = ob.user_profile()
            r= ob.dppic()
            return render_template("user_profile.html",record=record,r=r)
        else:
            name = request.form['name']
            mobile = request.form['mobile']
            ob = user_operation()
            ob.user_profile_update(name,mobile)
            flash("your profile is updated successfully!!")
            return redirect(url_for('user_profile'))
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))


@app.route('/user_password',methods=['GET','POST'])
def user_password():
    if('email' in session):
        if(request.method=='GET'):
            return render_template("user_password.html")
        else:
            old_password = request.form['old_password']
            new_password = request.form['new_password']
            
            #-- password encryption---------
            e = Encryption()
            old_password = e.convert(old_password)
            new_password = e.convert(new_password)

            ob = user_operation()
            r=ob.user_password(old_password,new_password)
            if(r==1):
                session.clear()
                flash("your password is updated successfully!!")
                return redirect(url_for('user_login'))
            else:
                flash("your old password is invalid...")
                return redirect(url_for('user_password'))
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))



@app.route('/addcase',methods=['GET','POST'])
def addcase():
    if(request.method=='GET'):
        return render_template("addcase.html")
    elif(request.method=='POST'):
        pname=request.form['pname']
        pid=request.form['pid']
        gender=request.form['gender']
        age=request.form['age']
        hname=request.form['hname']
        haddress=request.form['haddress']
        cdetails=request.form['cdetails']
        paddress=request.form['paddress']
        amt=request.form['amt']
        blood=request.form['blood']
        p1=request.files['p1']
        p2=request.files['p2']
        p3=request.files['p3']

        P1 = p1.filename  # retrieve photo name with extension
        P2 = p2.filename
        P3 = p3.filename
        d = datetime.now() 
        t = int(round(d.timestamp()))
        # path1 = str(t)+'.'+P1.split('.')[-1]
        # path2 = str(t)+'.'+P2.split('.')[-2]
        # path3 = str(t)+'.'+P3.split('.')[-3]

        p1.save("static/images/" + P1)
        p2.save("static/images/" + P2)
        p3.save("static/images/" + P3)
        # email=request.form['email']
        
        #---insertion-------------------
        ob = user_operation() # object create
        ob.addcase(pname,pid,gender,age,hname,haddress,cdetails,paddress,amt,blood,P1,P2,P3)
        
        return render_template("bank_details.html")
    else:
        return "error"

@app.route('/photo',methods=['GET','POST'])
def photo():
    # if(request.method=='GET'):
    #     return render_template("photo.html")
    # elif(request.method=='POST'):
    #     p1=request.files['p1']
    #     p2=request.files['p2']
    #     p3=request.files['p3']

    #     P1 = p1.filename  # retrieve photo name with extension
    #     P2 = p2.filename
    #     P3 = p3.filename
    #     d = datetime.now() 
    #     t = int(round(d.timestamp()))
    #     path1 = str(t)+'.'+P1.split('.')[-1]
    #     path2 = str(t)+'.'+P2.split('.')[-2]
    #     path3 = str(t)+'.'+P3.split('.')[-3]

    #     p1.save("static/images/" + path1)
    #     p2.save("static/images/" + path2)
    #     p3.save("static/images/" + path3)
           
    #     ob = user_operation()
    #     ob.photo(path1,path2,path3)
    #     flash("photo is uploaded successfully!!")
    #     return redirect(url_for('bank_details'))            
    # else:
    #     flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login')) 
   


@app.route('/bank_details',methods=['GET','POST'])
def bank_details():
    if('email' in session):
        if(request.method=='GET'):
            return render_template("bank_details.html")
        elif(request.method=='POST'):
            bname=request.form['bname']
            pan=request.form['pan']
            bank=request.form['bank']
            account=request.form['account']
            bmobile=request.form['bmobile']

            ob = user_operation()
            ob.bank_details(bname,pan,bank,account,bmobile)
            flash("Bank details is uploaded successfully!!")
            return redirect(url_for('user_dashboard'))            
        else:
            flash("you are not authorized to access this page.. please login first")
            return redirect(url_for('user_login')) 

@app.route('/donation_amt',methods=['GET','POST'])
def donation_amt():

    if('caseid'in session):
        if(request.method=='GET'):
            
            return render_template("donation_amt.html")
        elif(request.method=='POST'):
            amt= request.form['damt']
            return render_template("donor.html",damt=amt)
    else:
        return "error"

@app.route('/donation_amt2',methods=['GET','POST'])
def donation_amt2():

    if('caseid'in session):
        if(request.method=='GET'):
            
            return render_template("donation_amt2.html")
        elif(request.method=='POST'):
            amt= request.form['damt']
            return render_template("donor.html",damt=amt)
    else:
        return "error"


@app.route('/donor',methods=['POST'])
def donor():
    if('caseid' in session):
            
           
        if(request.method=='POST'):
            dname=request.form['dname']
            demail=request.form['demail']
            dpan=request.form['dpan']  
            damt=int(request.form['damt'])

            ob = donor_operation()
            ob.donor(dname,demail,dpan,damt)
            
            data = { "amount": damt*100, "currency": "INR", "receipt": "order_rcptid_11" }
            payment = client.order.create(data=data)
            pdata=[damt*100, payment["id"]]
            return render_template("payment.html", pdata=pdata)
    else:
        return "error"


@app.route('/case_details',methods=['GET','POST'])
def case_details():
    if('email' in session):
        if(request.method=='GET'):
            ob = user_operation()
            record=ob.case_details()
            print("✅ Passed to Template:", record) 
            return render_template("case_details.html",record=record)
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))

@app.route('/case_detail',methods=['GET','POST'])
def case_detail():
    if('email' in session):
        if(request.method=='GET'):
            ob = user_operation()
            record=ob.case_detail()
            return render_template("case_detail.html",record=record)
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))

@app.route('/case',methods=['GET','POST'])
def case():
    if("email" in session):
        if(request.method=='GET'):
            caseid=request.args.get('caseid')
            ob = user_operation()
            record=ob.case(caseid)
            amount=int(record[0][-5])
            obj=donor_operation()
            d=obj.pay_sum()
            
            a=(d*100/amount)
            
            return render_template("case.html",record=record,data=a)
        elif(request.method=='POST'):
            caseid=request.args.get('caseid')
            ob = user_operation()
            record=ob.case(caseid)
            return render_template("donation_amt.html",record=record)
        else:
            flash("you are not authorized to access this page.. please login first")
            return redirect(url_for('donation_amt'))

@app.route('/case2',methods=['GET','POST'])
def case2():
    
        if(request.method=='GET'):
            caseid=request.args.get('caseid')
            ob = user_operation()
            record=ob.case(caseid)
            amount=int(record[0][-5])
            obj=donor_operation()
            d=obj.pay_sum()
            a=(d*100/amount)
            c=int(a)
            return render_template("case2.html",record=record,data=c)
        else:
            flash("you are not authorized to access this page.. please login first")
            return redirect(url_for('donation_amt'))



@app.route('/all_cases',methods=['GET','POST'])
def all_cases():
    if(request.method=='GET'):
            caseid=request.args.get('caseid')
            ob = user_operation()
            record=ob.all_cases(caseid)
            return render_template("all_cases.html",record=record)
    



@app.route('/success', methods=["POST"])
def success():
    if('email' in session):
        if(request.method=='POST'):
            payid=request.form.get("razorpay_payment_id")
            ord_id=request.form.get("razorpay_order_id")
            sign=request.form.get("razorpay_signature")
            # created_at=request.form.get("razorpay_created_at")
            params={
            'razorpay_order_id': ord_id,
            'razorpay_payment_id': payid,
            'razorpay_signature': sign
            }
            final=client.utility.verify_payment_signature(params)
            if final == True:
                ob = donor_operation()
                ob.payment(payid,ord_id)
                r=ob.receipt(payid)
                
                
                return render_template("receipt2.html",record=r)
            return "Something Went Wrong Please Try Again"

    
    elif('caseid' in session):
        if(request.method=='POST'):
            payid=request.form.get("razorpay_payment_id")
            ord_id=request.form.get("razorpay_order_id")
            sign=request.form.get("razorpay_signature")
            # created_at=request.form.get("razorpay_created_at")
            params={
            'razorpay_order_id': ord_id,
            'razorpay_payment_id': payid,
            'razorpay_signature': sign
            }
            final=client.utility.verify_payment_signature(params)
            if final == True:
                ob = donor_operation()
                ob.payment(payid,ord_id)
                r= ob.receipt(payid)
                
                
                return render_template("receipt.html",record=r)
            return "Something Went Wrong Please Try Again"

    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_login'))   
    

@app.route('/admin_login',methods=['GET','POST'])
def admin_login():
    
    if(request.method=='GET'):
        return render_template("admin_login.html")
    elif(request.method=='POST'):
        adminid = request.form['adminid']
        password = request.form['password']
        

        ob = admin_operation()
        rc=ob.admin_login(adminid,password)
        if(rc==0):
            flash("invalid adwinid or password!!")
            return redirect(url_for('admin_login'))
        else:
            return redirect(url_for('admin_dashboard'))
            # return session['name']
    else:
        return "error"

@app.route('/admin_logout',methods=['GET','POST'])
def admin_logout():
    if('adminid' in session):
        if(request.method=='GET'):
            session.clear()
            return redirect(url_for('index'))
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('admin_login'))




@app.route('/admin_dashboard',methods=['GET','POST'])
def admin_dashboard():
    if('adminid in session'):
        if(request.method=='GET'):
            
            ob=admin_operation()
            record = ob.admin_dashboard()
            
            return render_template("admin_dashboard.html",record=record)
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('admin_login'))




@app.route('/status',methods=['POST'])
def status_update():
    if(request.method=="POST"):
        ob=admin_operation()
        record=ob.admin_dashboard()
        caseid=request.args.get("caseid")
        ob.status_update(caseid)

        return render_template("admin_dashboard.html",record=record)

@app.route('/complete',methods=['GET','POST'])
def complete():
    
    if(request.method=='GET'):
        ob = user_operation()
        record=ob.complete()
        return render_template("complete.html",record=record)
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('/'))

@app.route('/complete2',methods=['GET','POST'])
def complete2():
    if('email' in session):
        if(request.method=='GET'):
            ob = user_operation()
            record=ob.complete()
            return render_template("complete2.html",record=record)
    else:
        flash("you are not authorized to access this page.. please login first")
        return redirect(url_for('user_dashboard'))



if __name__=='__main__':
    app.run(debug=True)      #server activate