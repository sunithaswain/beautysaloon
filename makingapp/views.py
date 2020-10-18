import requests
import json
# from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render
# from . views import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Customers,Appointments
from .forms import Customersform
from datetime import datetime
from django.contrib.auth.hashers import make_password

# import Checksum
import time
from django.core.validators import validate_email
from django.core.validators import validate_email

# Create your views here.

def homeview(request):
    if request.method=="POST":
        return HttpResponseRedirect('/appointment/')
    else:
        return render(request, "index.html", {})
@csrf_exempt
def appointmentdetails(request):
    success_message = ""
    if request.method == "POST":
        form = Customersform(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            password=request.POST.get("password")
            statedetails=request.POST.get("statelocation")
            citydetails=request.POST.get("citylocation")
            print (statedetails,citydetails,"OOOOOOOOOOOOOOO")
            mobile=request.POST.get("mobile")
            # price=request.POST.get('price')
            # print (price)
            print("==========="*20)
            print(request.POST)
            timedetails=request.POST.get("time")
            print (timedetails)
            # newtime = time.strptime("",timedetails)
            # print (newtime,"{{{{{{{{{{{{"*30)
            dd = datetime.strptime(timedetails, "%H:%M")
            time_slot_time = datetime.strftime(dd, "%H:%M:%S")
            print("time slot is --- >",time_slot_time)

            emailvalid=Customers.objects.filter(email=email)
            #print (emailvalid,"{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{")
            if emailvalid:
                emaildata="Email is already exist"
                print ("data already exist")
                #return HttpResponse("email already exists")
                return render(request,"appointment.html",{'form':form,'email':emaildata})

            else:
                print ("create data")
                now=datetime.now()
                print (name,email,password,mobile,")))))))))))))))))))))))))))))")
                createdata = Customers.objects.create(name=name, email=email,create_time=now.strftime("%H:%M:%S"),category_id_id="1",password=password,mobile=mobile,state_location=statedetails,city_location=citydetails)
                createdata.password = make_password(password=password)
                createdata.save()
                print (createdata.id,"[[[[[[[[[")

                insert_appointment=Appointments.objects.create(customer_id_id=createdata.id,category_id_id="1",employee_id_id="121",timeslot=time_slot_time)
                print("))))))))))))))hello",insert_appointment)

                return render(request,"appointment.html",{"form":form,'email':"user created successfully"})
        else:
            print("not valid test")
            return HttpResponse("not valid data")
    else:
        form = Customersform()
        print(form)
        return render(request, "appointment.html",{'form': form, 'message': success_message})
    return render(request, "appointment.html",{})
@csrf_exempt
def massagedetials(request):
    return render(request,"massage.html",{})
@csrf_exempt
def paymentpagedetials(request):

    # import checksum generation utility
    # You can get this utility from https://developer.paytm.com/docs/checksum/
    from . import Checksum

    # initialize dictionary with request parameters
    paytmParams = {

        # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "MID": "Rujjjt58970680859206",

        # Find your WEBSITE in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "WEBSITE": "WEBSTAGING",

        # Find your INDUSTRY_TYPE_ID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "INDUSTRY_TYPE_ID": "Retail",

        # WEB for website and WAP for Mobile-websites or App
        "CHANNEL_ID": "WEB",

        # Enter your unique order id
        "ORDER_ID": "10201153937",

        # unique id that belongs to your customer
        "CUST_ID": "1",

        # customer's mobile number
        "MOBILE_NO": "9491329685",

        # customer's email
        "EMAIL": "sunithaswain20@gmail.com",

        # Amount in INR that is payble by customer
        # this should be numeric with optionally having two decimal points
        "TXN_AMOUNT": "30",

        # on completion of transaction, we will send you the response on this URL
        "CALLBACK_URL": "http://127.0.0.1:8000/callback/"
    }

    # Generate checksum for parameters we have
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    keydata="71g_8af%cNfk6Qd%"
    checksum = Checksum.generate_checksum(paytmParams, keydata)
    print(checksum,"[[[[[")

    # for Staging
    url = "https://securegw-stage.paytm.in/order/process"

    # for Production
    # url = "https://securegw.paytm.in/order/process"

    # Prepare HTML Form and Submit to Paytm
    print('<html>')
    print('<head>')
    print('<title>Merchant Checkout Page</title>')
    print('</head>')
    print('<body>')
    print('<center><h1>Please do not refresh this page...</h1></center>')
    print('<form method="post" action="' + url + '" name="paytm_form">')
    for name, value in paytmParams.items():
        print('<input type="hidden" name="' + name + '" value="' + value + '">')
    print('<input type="hidden" name="CHECKSUMHASH" value="' + checksum + '">')
    print('</form>')
    print('<script type="text/javascript">')
    print('document.paytm_form.submit();')
    print('</script>')
    print('</body>')
    print('</html>')
    return render(request,"payment.html",{})

@csrf_exempt
def callbackpagedetials(request):
    print ("test")
    # from . import Checksum
    # paytmChecksum = ""
    #
    # # Create a Dictionary from the parameters received in POST
    # # received_data should contains all data received in POST
    # paytmParams = {}
    # for key, value in received_data.items():
    #     if key == 'CHECKSUMHASH':
    #         paytmChecksum = value
    #     else:
    #         paytmParams[key] = value
    #
    # # Verify checksum
    # # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    # isValidChecksum = Checksum.verify_checksum(paytmParams, "YOUR_KEY_HERE", paytmChecksum)
    # if isValidChecksum:
    #     print("Checksum Matched")
    # else:
    #     print("Checksum Mismatched")
    return render(request,"callback.html",{})
@csrf_exempt
def checkout(request):
        return render(request,'check_out.html',{})
@csrf_exempt
def custompagedetials(request):

    merchnant_keys="71g_8af%cNfk6Qd%"
    merchnant_id="Rujjjt58970680859206"
    print (merchnant_id,"TTTTTTTTTTTTTTT")
    print ("::::::::::::::::::::::::")


    # import checksum generation utility
    # You can get this utility from https://developer.paytm.com/docs/checksum/
    from . import Checksum
    #import Checksum

    # initialize a dictionary
    paytmParams = dict()

    # body parameters
    paytmParams["body"] = {

        # for custom checkout value is 'Payment' and for intelligent router is 'UNI_PAY'
        "requestType": "Payment",

        # Find your MID in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "mid": merchnant_id,

        # Find your Website Name in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
        "websiteName": "http://127.0.0.1:8000",

        # Enter your unique order id
        "orderId": "12",

        # on completion of transaction, we will send you the response on this URL
        "callbackUrl": "http://127.0.0.1:8000/callback/",

        # Order Transaction Amount here
        "txnAmount": {

            # Transaction Amount Value
            "value": "30",

            # Transaction Amount Currency
            "currency": "INR",
        },

        # Customer Infomation here
        "userInfo": {

            # unique id that belongs to your customer
            "custId": '000120',#10201153937
        },
    }

    # Generate checksum by parameters we have in body
    # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys
    checksum = Checksum.generate_checksum_by_str(json.dumps(paytmParams["body"]), merchnant_keys)

    print(checksum, "&&&&&&&&&&&&")
    # head parameters
    paytmParams["head"] = {

        # put generated checksum value here
        "signature": checksum
    }

    # prepare JSON string for request
    post_data = json.dumps(paytmParams)

    # for Staging
    url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid={0}&orderId={1}".format(merchnant_id,12)

    # for Production
    # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=YOUR_ORDER_ID"

    response = requests.post(url, data=post_data, headers={"Content-type": "application/json"}).json()
    print (response)
    return HttpResponse("dfgrdg")