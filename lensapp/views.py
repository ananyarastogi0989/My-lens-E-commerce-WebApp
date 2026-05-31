import random
from django.core.mail import  send_mail
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from lensapp.models import formtbl, tabletbl, signuptbl, form3tbl, form3tbl1, steptbl, imgtbl, img1tbl, registrationtbl, \
    categorytbl, addproducttbl, customertbl, imgdatatbl, categorytbl2, addproducttbl2, buyproducttbl, buyproducttbl2, \
    editregistrationtbl, carttbl, wishlisttbl, navbartbl, reviewratingtbl, shippingtbl, pageonetbl, addproducttbl3, \
    wishlisttbl1, carttbl1, buyproducttbl3, wishlisttbl3, carttbl3, categorytbl3, addproducttbl4, buyproducttbl4, \
    wishlisttbl4, carttbl4, ratingtbl, ordertbl


# Create your views here.
def mytest(request):
    return render(request,"test.html")

def demopage(request):
    return render(request,"demo.html")

def premium(request):
    return render(request,"2_premium.html")

def form(request):
    return render(request,"form.html")

def formcode(request):
    a=request.POST['name']
    b=request.POST['mob']
    c=request.POST['city']
    ins=formtbl(name=a,mobile=b,city=c)
    ins.save()
    return render(request,"form.html")

def show(request):
    result=formtbl.objects.all()
    return render(request,"show.html",{"results":result})

def delete(request,id):
    delid=formtbl.objects.get(id=id)
    delid.delete()
    return redirect("../show")

def abc(request):
    return render(request,"abc.html")

def abccode(request):
    a=request.POST['name']
    b=request.POST['pass']
    c=request.POST['num']
    ins=tabletbl(name=a,password=b,mobile=c)
    ins.save()
    return render(request,"abc.html")

def show2(request):
    result=tabletbl.objects.all()
    return render(request,"show2.html",{"results":result})

def delete(request,id):
    delid=tabletbl.objects.get(id=id)
    delid.delete()
    return redirect("../show2")
def edit(request,id):
    editid=formtbl.objects.get(id=id)
    return render(request,"edit.html",{"editids":editid})

def update(request):
    a=request.POST['id']
    b=request.POST['name']
    c=request.POST['mob']
    d=request.POST['city']
    up=formtbl(id=a,name=b,mobile=c,city=d)
    up.save()
    return redirect("../show/")

def signup(request):
    return render(request,"signup.html")

def signupcode(request):
    a=request.POST['name']
    b=request.POST['email']
    c=request.POST['pass']
    ins=signuptbl(name=a,email=b,password=c)
    ins.save()
    return redirect('../login/')

def login(request):
    return render(request,"login.html")

def logincode(request):
    a=request.POST['email']
    b=request.POST['pass']
    if signuptbl.objects.filter(email=a).exists():
        if signuptbl.objects.filter(password=b).exists():
            request.session['user']=a
            return redirect('../dashboard/')
        else:
            return render(request,"login.html")
    else:
        return render(request,"login.html")

def dashboard(request):
    return render(request,"dashboard.html")

def changepassword(request):
    return render(request,"changepassword.html")

def changepasscode(request):
    a = request.POST['opass']
    b = request.POST['npass']
    c = request.POST['cpass']
    sesid=request.session['user']
    signuptbl.objects.filter(email=sesid).update(password=b)
    return render(request,"login.html")

def logout(request):
    return render(request,"login.html")

def form3(request):
    return render(request,"form3.html")


def form3code(request):
    a=request.POST['name']
    b=request.POST['mob']
    c=request.POST['add']
    d=request.POST['email']
    e=request.POST['pass']
    ins=form3tbl(name=a,mobile=b,address=c)
    ins.save()
    ins1=form3tbl1(email=d,password=e)
    ins1.save()
    return render(request,"form3.html")

def step1(request):
    return render(request,"step1.html")

def step2(request):
    return render(request,"step2.html")

def step3(request):
    return render(request,"step3.html")

def step1code(request):
    a=request.POST['fname']
    b= request.POST['lname']
    c= request.POST['fathername']
    ins=steptbl(fname=a,lname=b,fathername=c)
    ins.save()
    res=steptbl.objects.latest('id','fname','lname','fathername','mobile','address','pincode')
    return render (request,"step2.html",{'res':res})


def step2code(request):
    a=request.POST['id']
    b = request.POST['fname']
    c = request.POST['lname']
    d = request.POST['fathername']
    e=request.POST['mobile']
    f= request.POST['address']
    g= request.POST['pincode']
    ins=steptbl(id=a,fname=b,lname=c,fathername=d,mobile=e,address=f,pincode=g)
    ins.save()
    res = steptbl.objects.latest('id', 'fname', 'lname', 'fathername', 'mobile', 'address', 'pincode','dob','email','password')
    return render(request, "step3.html", {'res': res})

def step3code(request):
    a = request.POST['id']
    b = request.POST['fname']
    c = request.POST['lname']
    d = request.POST['fathername']
    e = request.POST['mobile']
    f = request.POST['address']
    g = request.POST['pincode']
    h = request.POST['dob']
    i = request.POST['email']
    j = request.POST['password']
    ins=steptbl(id=a,fname=b,lname=c,fathername=d,mobile=e,address=f,pincode=g,dob=h,email=i,password=j)
    ins.save()
    return render(request, "step1.html")

def img(request):
    return render(request,"img.html")

def imgcode(request):
    a=request.POST['name']
    b=request.POST['email']
    c=request.POST['pass']
    d=request.FILES['files']
    ins=imgtbl(name=a,email=b,password=c,picture=d)
    ins.save()
    return render(request,"img.html")

def imgshow(request):
    res=imgtbl.objects.all()
    return render(request,"imgshow.html",{'result':res})

def img1(request):
    return render(request,"img1.html")
def img1code(request):
    a = request.FILES['files1']
    b = request.FILES['files2']
    c = request.FILES['files']
    ins = img1tbl(picture1=a,picture2=b,picture3=c)
    ins.save()
    return render(request, "img1.html")

def img1show(request):
    res=img1tbl.objects.all()
    return render(request,"img1show.html",{'result':res})

def delete(request,id):
    dell=img1tbl.objects.get(id=id)
    dell.delete()
    return redirect("../img1show/")

def forgetpass(request):
    return render(request,"forgetpass.html")

def forgetpasscode(request):
    a=request.POST['email']
    sesid=registrationtbl.objects.get(email=a)
    b=str(random.randint(1000,9999))
    send_mail(
        'OTP',
        'Verify your OTP'+b,
        'ananyarastogi908@gmail.com',
        [a],
        fail_silently=False
    )
    if a=='':
        return render(request,"forgetpass.html")
    else:
        if registrationtbl.objects.filter(email=a).update(otp=b):
            return render(request,"otppage.html",{'sesid':sesid})
        else:
            return render(request,"forgetpass.html")

def otppage(request):
    return render(request,"otppage.html")

def otpcode(request):
    email=request.POST['email']
    a=request.POST['otp']
    sesid=registrationtbl.objects.get(email=email)
    if a=='':
        return render(request,"otppage.html")
    else:
        if registrationtbl.objects.filter(otp=a).exists():
            return render(request,"resetpass.html",{'sesid':sesid})
        else:
            return render(request,"otppage.html")

def resetpass(request):
    return render(request,"resetpass.html")

def resetpasscode(request):
    email=request.POST['email']
    a=request.POST['npass']
    b=request.POST['cpass']
    if a=='' or b=='':
        return render(request,"resetpass.html")
    else:
        if a==b:
            if registrationtbl.objects.filter(email=email).update(password=a):
                return render(request,"index.html")
            else:
                return render(request,"resetpass.html")
        else:
            return render(request,"resetpass.html")


def head2(request):
    # result_table1 = categorytbl.objects.all()
    # result_table2 = categorytbl2.objects.all()
    # result_table3 = pageonetbl.objects.all()
    # result_table4 = navbartbl.objects.all()
    # result_table5 = categorytbl3.objects.all()

    return render(request, "index.html", {
        # "results_table1": result_table1,
        # "results_table2": result_table2,
        # "results_table3": result_table3,
        # "results_table4": result_table4,
        # "results_table5": result_table5,
    })




def head2code(request):
    a=request.POST['fname']
    b=request.POST['lname']
    c=request.POST['mobileno']
    d=request.POST['email']
    e=request.POST['password']
    ins=registrationtbl(fname=a,lname=b,mobileno=c,email=d,password=e)
    ins.save()
    return redirect('../')


def signincode(request):
    d=request.POST['email']
    e=request.POST['password']
    if registrationtbl.objects.filter(email=d).exists():
        user=registrationtbl.objects.get(email=d)
        if user.password==e:
            request.session['user']=d
            return redirect(f'../account_info/{user.id}')
        else:
            return redirect("../")
    else:
        return redirect("../")



def trackcode(request):
    d = request.POST['email']
    e = request.POST['password']
    if registrationtbl.objects.filter(email=d).exists():
        if registrationtbl.objects.filter(password=e).exists():
            request.session['user'] = d
            return redirect('../dashboard/')
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")

def do_more_be_more2(request):
    return render(request,"do_more_be_more2.html")

def john_jacobs_nav(request):
    return render(request,"john_jacobs_nav.html")

def aqua_lens(request):
    return render(request,"aqua_lens.html")

def singapore2(request):
    return render(request,"singapore2.html")

def nav_eyeglass(request,id):
    idd=categorytbl.objects.get(id=id)
    result=addproducttbl.objects.filter(catid=idd.id)
    return render(request,"nav_eyeglass.html",{"results":result})

def nav_computer(request):
    return render(request,"nav_computer.html")

def nav_kids(request):
    return render(request,"nav_kids.html")

def nav_contact(request):
    return render(request,"nav_contact.html")

def blu_button(request):
    return render(request,"blu_button.html")

def progressive_lens(request):
    return render(request,"progressive_lens.html")

def cat_eye(request,id):
    idd=pageonetbl.objects.get(id=id)
    result=addproducttbl3.objects.filter(catid=idd.id)
    return render(request,"cat_eye.html",{"results":result})

def nav_sunglass(request,id):
    idd=categorytbl3.objects.get(id=id)
    result=addproducttbl4.objects.filter(catid=idd.id)
    return render(request,"nav_sunglass.html",{"results":result})

def john_jacobs(request):
    return render(request,"john_jacobs.html")

def vinchent_chase(request):
    return render(request,"vinchent_chase.html")

def rounds(request,id):
    idd = categorytbl2.objects.get(id=id)
    result = addproducttbl2.objects.filter(catid=idd.id)
    return render(request, "rounds.html", {"results": result})

def transparent(request):
    return render(request,"transparent.html")

def mouni_roy(request):
    return render(request,"mouni_roy.html")

def karan_johar(request):
    return render(request,"karan_johar.html")

def buying_guide(request):
    return render(request,"buying_guide.html")

def size_guide(request):
    return render(request,"size_guide.html")

def FAQs(request):
    return render(request,"FAQs.html")

def contact_nine(request):
    return render(request,"contact_nine.html")

def John_Jacobs_Card1(request,id):
    idd = addproducttbl3.objects.get(id=id)
    result =buyproducttbl3.objects.filter(catid=idd.id)
    return render(request,"John_Jacobs_Card1.html",{"results":result, 'idd':idd})

def nav_sunglass_card1(request,id):
    idd = addproducttbl4.objects.get(id=id)
    result =buyproducttbl4.objects.filter(catid=idd.id)
    return render(request,"nav_sunglass_card1.html",{"results":result})

def John_jacobs_Card2(request):
    return render(request,"John_jacobs_Card2.html")

def John_Jacobs_Card3(request):
    return render(request,"John_Jacobs_Card3.html")

def John_jacobs_card4(request):
    return render(request,"John_jacobs_card4.html")

def John_Jacobs_Card5(request):
    return render(request,"John_Jacobs_Card5.html")

def John_Jacobs_Card6(request):
    return render(request,"John_Jacobs_Card6.html")

def buy_step2(request,id):
    result=carttbl.objects.get(pid=id)
    return render(request,"buy_step2.html", {'result':result})

def buy_step2_part2(request,id):
    result=carttbl3.objects.get(pid=id)
    return render(request,"buy_step2_part2.html", {'result':result})

def buy_step2_part3(request,id):
    result=carttbl1.objects.get(pid=id)
    return render(request,"buy_step2_part3.html", {'result':result})

def buy_step2_part6(request,id):
    result=carttbl4.objects.get(pid=id)
    return render(request,"buy_step2_part6.html", {'result':result})

def review_rating(request):
    result = reviewratingtbl.objects.all()
    return render(request, "review_rating.html", {"results": result})

def buy_step_3(request):
    return render(request,"buy_step_3.html")

def buy_step_3part1(request):
    return render(request,"buy_step_3part1.html")

def buy_step_4(request,id):
    result=carttbl.objects.get(id=id)
    return render(request,"buy_step_4.html", {'result':result})

def buy_step_5(request):
    return render(request,"buy_step_5.html")

def summary(request):
    return render(request,"summary.html")

def full_rim(request):
    return render(request,"full_rim.html")

def Buy_step1(request,id):
    idd = addproducttbl.objects.get(id=id)
    result = buyproducttbl.objects.filter(catid=idd.id)
    return render(request, "Buy_step1.html", {"results": result, 'idd':idd})

def round_card1(request,id):
    idd = addproducttbl2.objects.get(id=id)
    print(idd)
    result = buyproducttbl2.objects.filter(catid=idd.id)
    print(result)
    return render(request, "round_card1.html", {"results": result, 'idd':idd})

def card2_Buy(request):
    return render(request,"card2_Buy.html")

def card3_Buy_step_1(request):
    return render(request,"card3_Buy_step_1.html")

def card4_Buy_step_1(request):
    return render(request,"card4_Buy_step_1.html")

def card5_Buy_step_1(request):
    return render(request,"card5_Buy_step_1.html")

def card6_Buy_step_1(request):
    return render(request,"card6_Buy_step_1.html")


def nav_sunglass_card2(request):
    return render(request,"nav_sunglass_card2.html")

def nav_sunglass_card3(request):
    return render(request,"nav_sunglass_card3.html")

def nav_sunglass_card4(request):
    return render(request,"nav_sunglass_card4.html")

def nav_sunglass_card5(request):
    return render(request,"nav_sunglass_card5.html")

def nav_sunglass_card6(request):
    return render(request,"nav_sunglass_card6.html")

def nav_contact_card1(request):
    return render(request,"nav_contact_card1.html")

def nav_contact_card2(request):
    return render(request,"nav_contact_card2.html")

def nav_contact_card3(request):
    return render(request,"nav_contact_card3.html")
def nav_contact_card4(request):
    return render(request,"nav_contact_card4.html")

def nav_contact_card5(request):
    return render(request,"nav_contact_card5.html")

def nav_contact_card6(request):
    return render(request,"nav_contact_card6.html")

def comp_card1(request):
    return render(request,"comp_card1.html")

def comp_card2(request):
    return render(request,"comp_card2.html")

def comp_card3(request):
    return render(request,"comp_card3.html")

def comp_card4(request):
    return render(request,"comp_card4.html")

def comp_card5(request):
    return render(request,"comp_card5.html")

def comp_card6(request):
    return render(request,"comp_card6.html")

def nav_contact_card1(request):
    return render(request,"nav_contact_card1.html")

def nav_contact_card2(request):
    return render(request,"nav_contact_card2.html")

def nav_contact_card3(request):
    return render(request,"nav_contact_card3.html")

def nav_contact_card4(request):
    return render(request,"nav_contact_card4.html")

def nav_contact_card5(request):
    return render(request,"nav_contact_card5.html")

def nav_contact_card6(request):
    return render(request,"nav_contact_card6.html")

def Vincent_Chase_card1(request):
    return render(request,"Vincent_Chase_card1.html")

def Vncent_Chase_Card2(request):
    return render(request,"Vncent_Chase_Card2.html")

def Vincent_Chase_card3(request):
    return render(request,"Vincent_Chase_card3.html")

def Vincent_Chase_Card4(request):
    return render(request,"Vincent_Chase_Card4.html")

def Vincent_Chase_Card5(request):
    return render(request,"Vincent_Chase_Card5.html")

def Vincent_Chase_Card6(request):
    return render(request,"Vincent_Chase_Card6.html")

def karan_johar_card1(request):
    return render(request,"karan_johar_card1.html")

def karan_johar_card2(request):
    return render(request,"karan_johar_card2.html")

def karan_johar_card3(request):
    return render(request,"karan_johar_card3.html")

def karan_johar_card4(request):
    return render(request,"karan_johar_card4.html")

def karan_johar_card5(request):
    return render(request,"karan_johar_card5.html")

def karan_johar_card6(request):
    return render(request,"karan_johar_card6.html")

def cat_eye_card1(request):
    return render(request,"cat_eye_card1.html")

def cat_eye_card2(request):
    return render(request,"cat_eye_card2.html")

def cat_eye_card3(request):
    return render(request,"cat_eye_card3.html")

def cat_Eye_card4(request):
    return render(request,"cat_Eye_card4.html")

def cat_eye_card5(request):
    return render(request,"cat_eye_card5.html")

def cat_Eye_card6(request):
    return render(request,"cat_Eye_card6.html")

def mouni_roy_card1(request):
    return render(request,"mouni_roy_card1.html")

def mouni_roy_card2(request):
    return render(request,"mouni_roy_card2.html")

def mouni_roy_card3(request):
    return render(request,"mouni_roy_card3.html")

def mouni_roy_card4(request):
    return render(request,"mouni_roy_card4.html")

def mouni_roy_card5(request):
    return render(request,"mouni_roy_card5.html")

def mouni_roy_card6(request):
    return render(request,"mouni_roy_card6.html")

def kids_card1(request):
    return render(request,"kids_card1.html")

def kids_card2(request):
    return render(request,"kids_card2.html")

def kids_card3(request):
    return render(request,"kids_card3.html")

def kids_card4(request):
    return render(request,"kids_card4.html")

def kids_card5(request):
    return render(request,"kids_card5.html")

def kids_card6(request):
    return render(request,"kids_card6.html")

def round_card1(request,id):
    idd = addproducttbl2.objects.get(id=id)
    result = buyproducttbl2.objects.filter(catid=idd.id)
    # result = buyproducttbl.objects.all()
    return render(request, "round_card1.html", {"results": result, 'idd':idd})

def round_card2(request):
    return render(request,"round_card2.html")

def round_card3(request):
    return render(request,"round_card3.html")

def round_card4(request):
    return render(request,"round_card4.html")

def round_card5(request):
    return render(request,"round_card5.html")

def round_card6(request):
    return render(request,"round_card6.html")

def transparent_card1(request):
    return render(request,"transparent_card1.html")

def transparent_card2(request):
    return render(request,"transparent_card2.html")

def transparent_card3(request):
    return render(request,"transparent_card3.html")

def transparent_card4(request):
    return render(request,"transparent_card4.html")

def transparent_card5(request):
    return render(request,"transparent_card5.html")

def transparent_card6(request):
    return render(request,"transparent_card6.html")

def nine_nine_card1(request):
    return render(request,"nine_nine_card1.html")

def nine_nine_card2(request):
    return render(request,"nine_nine_card2.html")

def nine_nine_card3(request):
    return render(request,"nine_nine_card3.html")

def nine_nine_card4(request):
    return render(request,"nine_nine_card4.html")

def nine_nine_card5(request):
    return render(request,"nine_nine_card5.html")

def nine_nine_card6(request):
    return render(request,"nine_nine_card6.html")


def signin_page3(request,id):
    sesid=registrationtbl.objects.get(id=id)
    result_table4 = navbartbl.objects.all()
    result = categorytbl.objects.all()
    result_table3 = pageonetbl.objects.all()
    result_table2 = categorytbl2.objects.all()
    result_table5 = categorytbl3.objects.all()
    if request.method=='GET':
        st=request.GET.get('searchdata')
        if st!=None:
            result=categorytbl.objects.filter(cname__icontains=st)
            # result_table3 |= categorytbl.objects.filter(cname__icontains=st)
    return render(request, "signin_page3.html", {"results": result, "navbar_results": result_table4,"pageone_results":result_table3,"category_results":result_table2,"table_results":result_table5, 'sesid':sesid})

def my_order(request):
    return render(request,"my_order.html")

def Prescription(request):
    return render(request,"Prescription.html")

def account_info(request,id):
    result = registrationtbl.objects.get(id=id)
    return render(request, "account_info.html", {"results": result})


def admin(request):
    return render(request,"Admin_Panel/admin.html")

def ecommerce_orders(request):
    return render(request,"Admin_Panel/ecommerce_orders.html")

def delete_product(request):
    return render(request,"Admin_Panel/delete_product.html")

def auth_logout(request):
    return render(request,"auth_logout.html")

def add_category(request):
    return render(request,"Admin_Panel/add_category.html")


def add_category3(request):
    return render(request,"Admin_Panel/add_category3.html")


def add_pageone(request):
    return render(request,"Admin_Panel/add_pageone.html")

def categorycode(request):
    a=request.POST['customername']
    b=request.FILES['image']
    ins=categorytbl(Image=b,cname=a)
    ins.save()
    return redirect('../add_category/')

def pageonecode(request):
    a=request.FILES['image']
    ins=pageonetbl(image=a)
    ins.save()
    return redirect('../add_pageone/')

def addcategory3(request):
    a=request.FILES['image']
    ins=categorytbl3(image=a)
    ins.save()
    return redirect('../add_category3/')

def ecommerce_add_product(request):
    return render(request,"Admin_Panel/ecommerce_add_product.html")

def add_product_pageone(request):
    page=pageonetbl.objects.all()
    return render(request,"Admin_Panel/add_product_pageone.html",{'page':page})

def addproductcode(request):
    g=request.POST['category']
    a=request.POST['productname']
    b=request.POST['productdescription']
    c=request.POST['productprice']
    d=request.POST['productsize']
    h=request.POST['quantity']
    e=request.POST['manufacturerbrand']
    f=request.FILES['image']
    ins=addproducttbl(catid=g,pname=a,pdescription=b,price=c,size=d,quantity=h,brand=e,image=f)
    ins.save()
    return redirect('../ecommerce_add_product/')

def addproductpageonecode(request):
    g=request.POST['category']
    a=request.POST['productname']
    b=request.POST['productdescription']
    c=request.POST['productprice']
    d=request.POST['productsize']
    h=request.POST['quantity']
    e=request.POST['manufacturerbrand']
    f=request.FILES['image']
    ins=addproducttbl3(catid=g,pname=a,pdescription=b,price=c,size=d,quantity=h,brand=e,image=f)
    ins.save()
    return redirect('../add_product_pageone/')

def addproductcode3(request):
    g=request.POST['category']
    a=request.POST['productname']
    b=request.POST['productdescription']
    c=request.POST['productprice']
    d=request.POST['productsize']
    h=request.POST['quantity']
    e=request.POST['manufacturerbrand']
    f=request.FILES['image']
    ins=addproducttbl4(catid=g,pname=a,pdescription=b,price=c,size=d,quantity=h,brand=e,image=f)
    ins.save()
    return redirect('../add_product3/')

def ecommerce_customers(request):
    return render(request,"Admin_Panel/ecommerce_customers.html")

def cartt(request):
    return render(request,"cartt.html")

def navbar(request):
    return render(request,"Admin_Panel/navbar.html")

def customercode(request):
    a=request.POST['num']
    b=request.POST['name']
    c=request.POST['email']
    d=request.POST['address']
    ins=customertbl(sno=a,name=b,email=c,address=d)
    ins.save()
    return redirect('../ecommerce_customers/')

def show_category(request):
    result=categorytbl.objects.all()
    return render(request,"Admin_Panel/show_category.html",{"results":result})


def rating(request):
    result=ratingtbl.objects.all()
    return render(request,"Admin_Panel/rating.html",{"results":result})

def order_status(request):
    result=ordertbl.objects.all()
    return render(request,"Admin_Panel/order_status.html",{"results":result})

def show_pageone(request):
    result=pageonetbl.objects.all()
    return render(request,"Admin_Panel/show_pageone.html",{"results":result})

def show_category3(request):
    result=categorytbl3.objects.all()
    return render(request,"Admin_Panel/show_category3.html",{"results":result})

def delete_product(request):
    result=addproducttbl.objects.all()
    return render(request,"Admin_Panel/delete_product.html",{"results":result})


def show_product_pageone(request):
    result=addproducttbl3.objects.all()
    return render(request,"Admin_Panel/show_product_pageone.html",{"results":result})

def show_product3(request):
    result=addproducttbl4.objects.all()
    return render(request,"Admin_Panel/show_product3.html",{"results":result})





def ecommerce_add_product(request):
    result=categorytbl.objects.all()
    return render(request,"Admin_Panel/ecommerce_add_product.html",{"results":result})

def page_banners(request):
    return render(request,"Admin_Panel/page_banners.html")

def imagecode(request):
    a=request.POST['data']
    b=request.FILES['image']
    ins=imgdatatbl(text=a,image=b)
    ins.save()
    return redirect('../page_banners/')

def add_category2(request):
    return render(request,"Admin_Panel/add_category2.html")

def show_category2(request):
    result = categorytbl2.objects.all()
    return render(request, "Admin_Panel/show_category2.html", {"results": result})

def categorycode2(request):
    a=request.POST['categoryname']
    b=request.FILES['image']
    ins=categorytbl2(name=a,image=b)
    ins.save()
    return redirect('../add_category2/')

def add_product2(request):
    result = categorytbl2.objects.all()
    return render(request, "Admin_Panel/add_product2.html", {"results": result})

def add_product3(request):
    result = categorytbl3.objects.all()
    return render(request, "Admin_Panel/add_product3.html", {"results": result})


def addproductcode2(request):
    g=request.POST['category']
    a=request.POST['productname']
    b=request.POST['productdescription']
    c=request.POST['productprice']
    d=request.POST['productsize']
    h=request.POST['quantity']
    e=request.POST['manufacturerbrand']
    f=request.FILES['image']
    ins=addproducttbl2(catid=g,pname=a,pdescription=b,price=c,size=d,quantity=h,brand=e,image=f)
    ins.save()
    return redirect('../add_product2/')

def show_product2(request):
    result = addproducttbl2.objects.all()
    return render(request, "Admin_Panel/show_product2.html", {"results": result})

def buy_product(request):
    result = addproducttbl.objects.all()
    return render(request, "Admin_Panel/buy_product.html", {"results": result})


def show_step1(request):
    result = buyproducttbl.objects.all()
    return render(request, "Admin_Panel/show_step1.html", {"results": result})

def buyproductcode(request):
    catery = request.POST['category']
    a = request.FILES['image1']
    b = request.FILES['image2']
    c = request.FILES['image3']
    d = request.FILES['image4']
    e = request.FILES['image5']
    f = request.FILES['image6']
    g = request.FILES['image7']
    h = request.FILES['image8']
    i = request.FILES['image9']
    j = request.FILES['image10']
    k = request.POST['productname']
    l = request.POST['productdescription']
    m = request.POST['productsize']
    n = request.POST['productprice']
    o = request.POST['productid']
    p = request.POST['modelno']
    q = request.POST['framesize']
    r = request.POST['framewidth']
    s = request.POST['framedimension']
    t =  request.FILES['image11']
    u =  request.FILES['image12']
    v =  request.FILES['image13']
    w =  request.FILES['image14']
    x =  request.FILES['image15']
    y =  request.FILES['image16']
    z =  request.POST['review']
    ins=buyproducttbl(catid=catery,image1=a,image2=b,image3=c,image4=d,image5=e,image6=f,image7=g,image8=h,image9=i,image10=j,name=k,description=l,size=m,price=n,mid=o,mno=p,msize=q,mwidth=r,mdimension=s,image11=t,image12=u,image13=v,image14=w,image15=x,image16=y,review=z)
    ins.save()
    return redirect('../buy_product/')

def buy_product2(request):
    result = addproducttbl2.objects.all()
    return render(request, "Admin_Panel/buy_product2.html", {"results": result})


def buy_product3(request):
    result = addproducttbl3.objects.all()
    return render(request, "Admin_Panel/buy_product3.html", {"results": result})

def buy_product4(request):
    result = addproducttbl4.objects.all()
    return render(request, "Admin_Panel/buy_product4.html", {"results": result})

def show_step2(request):
    result = buyproducttbl2.objects.all()
    return render(request, "Admin_Panel/show_step2.html", {"results": result})


def show_step3(request):
    result = buyproducttbl3.objects.all()
    return render(request, "Admin_Panel/show_step3.html", {"results": result})

def show_step4(request):
    result = buyproducttbl4.objects.all()
    return render(request, "Admin_Panel/show_step4.html", {"results": result})

def buyproductcode2(request):
    catery = request.POST['category']
    a = request.FILES['image1']
    b = request.FILES['image2']
    c = request.FILES['image3']
    d = request.FILES['image4']
    e = request.FILES['image5']
    f = request.FILES['image6']
    g = request.FILES['image7']
    h = request.FILES['image8']
    i = request.FILES['image9']
    j = request.FILES['image10']
    k = request.POST['productname']
    l = request.POST['productdescription']
    m = request.POST['productsize']
    n = request.POST['productprice']
    o = request.POST['productid']
    p = request.POST['modelno']
    q = request.POST['framesize']
    r = request.POST['framewidth']
    s = request.POST['framedimension']
    t = request.FILES['image11']
    u = request.FILES['image12']
    v = request.FILES['image13']
    w = request.FILES['image14']
    x = request.FILES['image15']
    y = request.FILES['image16']
    ins=buyproducttbl2(catid=catery,image1=a,image2=b,image3=c,image4=d,image5=e,image6=f,image7=g,image8=h,image9=i,image10=j,name=k,description=l,size=m,price=n,mid=o,mno=p,msize=q,mwidth=r,mdimension=s,image11=t,image12=u,image13=v,image14=w,image15=x,image16=y)
    ins.save()
    return redirect('../buy_product2/')

def buyproductcode3(request):
    catery = request.POST['category']
    a = request.FILES['image1']
    b = request.FILES['image2']
    c = request.FILES['image3']
    d = request.FILES['image4']
    e = request.FILES['image5']
    f = request.FILES['image6']
    g = request.FILES['image7']
    h = request.FILES['image8']
    i = request.FILES['image9']
    j = request.FILES['image10']
    k = request.POST['productname']
    l = request.POST['productdescription']
    m = request.POST['productsize']
    n = request.POST['productprice']
    o = request.POST['productid']
    p = request.POST['modelno']
    q = request.POST['framesize']
    r = request.POST['framewidth']
    s = request.POST['framedimension']
    t = request.FILES['image11']
    u = request.FILES['image12']
    v = request.FILES['image13']
    w = request.FILES['image14']
    x = request.FILES['image15']
    y = request.FILES['image16']
    ins=buyproducttbl3(catid=catery,image1=a,image2=b,image3=c,image4=d,image5=e,image6=f,image7=g,image8=h,image9=i,image10=j,name=k,description=l,size=m,price=n,mid=o,mno=p,msize=q,mwidth=r,mdimension=s,image11=t,image12=u,image13=v,image14=w,image15=x,image16=y)
    ins.save()
    return redirect('../buy_product3/')

def buyproductcode4(request):
    catery = request.POST['category']
    a = request.FILES['image1']
    b = request.FILES['image2']
    c = request.FILES['image3']
    d = request.FILES['image4']
    e = request.FILES['image5']
    f = request.FILES['image6']
    g = request.FILES['image7']
    h = request.FILES['image8']
    i = request.FILES['image9']
    j = request.FILES['image10']
    k = request.POST['productname']
    l = request.POST['productdescription']
    m = request.POST['productsize']
    n = request.POST['productprice']
    o = request.POST['productid']
    p = request.POST['modelno']
    q = request.POST['framesize']
    r = request.POST['framewidth']
    s = request.POST['framedimension']
    t = request.FILES['image11']
    u = request.FILES['image12']
    v = request.FILES['image13']
    w = request.FILES['image14']
    x = request.FILES['image15']
    y = request.FILES['image16']
    ins=buyproducttbl4(catid=catery,image1=a,image2=b,image3=c,image4=d,image5=e,image6=f,image7=g,image8=h,image9=i,image10=j,name=k,description=l,size=m,price=n,mid=o,mno=p,msize=q,mwidth=r,mdimension=s,image11=t,image12=u,image13=v,image14=w,image15=x,image16=y)
    ins.save()
    return redirect('../buy_product4/')

def front(request):
    return render(request,"Admin_Panel/front.html")

def frontshow(request):
    result = fronttbl.objects.all()
    return render(request, "Admin_Panel/frontshow.html", {"results": result})

def frontcode(request):
    a=request.POST['title']
    b = request.FILES['image1']
    c = request.FILES['image2']
    d = request.FILES['image3']
    e = request.FILES['image4']
    f = request.FILES['image5']
    g = request.FILES['image6']
    h = request.FILES['image7']
    i = request.FILES['image8']
    j = request.FILES['image9']
    k = request.FILES['image10']
    l = request.FILES['image11']
    ins=fronttbl(title=a,image1=b,image2=c,image3=d,image4=e,image5=f,image6=g,image7=h,image8=i,image9=j,image10=k,image11=l)
    ins.save()
    return redirect('../front/')

def accountcode(request):
    a = request.POST['firstname']
    b = request.POST['lastname']
    c = request.POST['mobileno']
    e = request.POST['email']
    d = request.POST['password']
    ins = editregistrationtbl(fname=a, lname=b, email=e, mobileno=c, password=d)
    ins.save()
    return redirect('../account_info/')

def ratingcode(request):
    catid1=request.POST['catid']
    a = request.POST['email']
    b = request.POST['review']
    c = request.POST['rating']
    ins = ratingtbl(catid=catid1,email=a,review=b,rating=c)
    ins.save()
    return redirect(f'../Buy_step1/{catid1}')

def ratingcode1(request):
    catid1=request.POST['catid']
    a = request.POST['email']
    b = request.POST['review']
    ins = ratingtbl(catid=catid1,email=a,review=b)
    ins.save()
    return redirect(f'../John_Jacobs_Card1/{catid1}')

def ratingcode2(request):
    catid1=request.POST['catid']
    a = request.POST['email']
    b = request.POST['review']
    ins = ratingtbl(catid=catid1,email=a,review=b)
    ins.save()
    return redirect(f'../round_card1/{catid1}')

def add_registration(request):
    return render(request,"Admin_Panel/add_registration.html")

def registrationcode(request):
    a=request.POST['firstname']
    b=request.POST['lastname']
    c=request.POST['mobileno']
    d=request.POST['emaill']
    e=request.POST['password']
    ins=registrationtbl(fname=a,lname=b,mobileno=c,email=d,password=e)
    ins.save()
    return redirect('../add_registration/')

def registration_show(request):
    result=registrationtbl.objects.all()
    return render(request,"Admin_Panel/registration_show.html",{"results":result})

def edit_registration(request):
    result = registrationtbl.objects.all()
    return render(request, "Admin_Panel/edit_registration.html", {"results": result})

def show_edit_registration(request):
    result = editregistrationtbl.objects.all()
    return render(request, "Admin_Panel/show_edit_registration.html", {"results": result})

def editcode(request):
    result = registrationtbl.objects.all()
    print(result)
    return render(request, "account_info.html", {"results": result})


def wishlist(request,id):
    product= addproducttbl.objects.get(id=id)
    pid=product.id
    ins = wishlisttbl(pid=pid,userid=0)
    ins.save()
    return redirect(f'../nav_eyeglass/{product.catid}')

def wishlist1(request,id):
    product= addproducttbl2.objects.get(id=id)
    pid=product.id
    ins = wishlisttbl1(pid=pid,userid=0)
    ins.save()
    return redirect(f'../rounds/{product.catid}')

def wishlist3(request,id):
    product= addproducttbl3.objects.get(id=id)
    pid=product.id
    ins = wishlisttbl3(pid=pid,userid=0)
    ins.save()
    return redirect(f'../cat_eye/{product.catid}')

def wishlist4(request,id):
    product= addproducttbl4.objects.get(id=id)
    pid=product.id
    ins = wishlisttbl4(pid=pid,userid=0)
    ins.save()
    return redirect(f'../nav_sunglass/{product.catid}')


def wishlist_show(request):
    results = wishlisttbl.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid

        # Assuming there's a ForeignKey relationship between wishlisttbl and addproducttbl
        matching_addproduct_data = addproducttbl.objects.filter(id=result_id)

        result_data.append({"wishlist_item": result, "matching_addproduct_data": matching_addproduct_data})

    return render(request, "wishlist_show.html", {"result_datas": result_data})

def wishlist3_show(request):
    results = wishlisttbl3.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid

        # Assuming there's a ForeignKey relationship between wishlisttbl and addproducttbl
        matching_addproduct_data = addproducttbl3.objects.filter(id=result_id)

        result_data.append({"wishlist_item": result, "matching_addproduct_data": matching_addproduct_data})

    return render(request, "wishlist3_show.html", {"result_datas": result_data})

def wishlist4_show(request):
    results = wishlisttbl4.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid

        # Assuming there's a ForeignKey relationship between wishlisttbl and addproducttbl
        matching_addproduct_data = addproducttbl4.objects.filter(id=result_id)

        result_data.append({"wishlist_item": result, "matching_addproduct_data": matching_addproduct_data})

    return render(request, "wishlist4_show.html", {"result_datas": result_data})

def wishlist1_show(request):
    results = wishlisttbl1.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid

        # Assuming there's a ForeignKey relationship between wishlisttbl and addproducttbl
        matching_addproduct_data = addproducttbl2.objects.filter(id=result_id)

        result_data.append({"wishlist_item": result, "matching_addproduct_data": matching_addproduct_data})

    return render(request, "wishlist1_show.html", {"result_datas": result_data})


def cart(request,id):
    product= buyproducttbl.objects.get(id=id)
    pid=product.id
    image=product.image1
    title=product.name
    des=product.description
    price=product.price
    ins = carttbl(pid=pid,userid=0,image1=image,name=title,description=des,price=price)
    ins.save()
    return redirect(f'../Buy_step1/{product.catid}')

def cart1(request,id):
    product= buyproducttbl2.objects.get(id=id)
    pid=product.id
    image=product.image1
    title=product.name
    des=product.description
    price=product.price
    ins = carttbl1(pid=pid,userid=0,image1=image,name=title,description=des,price=price)
    ins.save()
    return redirect(f'../round_card1/{product.catid}')

def cart3(request,id):
    product= buyproducttbl3.objects.get(id=id)
    pid=product.id
    image=product.image1
    title=product.name
    des=product.description
    price=product.price
    ins = carttbl3(pid=pid,userid=0,image1=image,name=title,description=des,price=price)
    ins.save()
    return redirect(f'../John_Jacobs_Card1/{product.catid}')

def cart4(request,id):
    product= buyproducttbl4.objects.get(id=id)
    pid=product.id
    image=product.image1
    title=product.name
    des=product.description
    price=product.price
    ins = carttbl4(pid=pid,userid=0,image1=image,name=title,description=des,price=price)
    ins.save()
    return redirect(f'../nav_sunglass_card1/{product.catid}')
def cart_show(request):
    results=carttbl.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid
        matching_buyproduct_data = buyproducttbl.objects.filter(id=result_id)
        result_data.append({"cart_item":result,"matching_buyproduct_data": matching_buyproduct_data})
    return render(request,"cart_show.html",{"result_datas":result_data})

def cart1_show(request):
    results=carttbl1.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid
        matching_buyproduct_data = buyproducttbl2.objects.filter(id=result_id)
        result_data.append({"cart_item":result,"matching_buyproduct_data": matching_buyproduct_data})
    return render(request,"cart1_show.html",{"result_datas":result_data})

def cart3_show(request):
    results=carttbl3.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid
        matching_buyproduct_data = buyproducttbl3.objects.filter(id=result_id)
        result_data.append({"cart_item":result,"matching_buyproduct_data": matching_buyproduct_data})
    return render(request,"cart3_show.html",{"result_datas":result_data})



def cart4_show(request):
    results=carttbl4.objects.all()
    result_data = []

    for result in results:
        result_id = result.pid
        matching_buyproduct_data = buyproducttbl4.objects.filter(id=result_id)
        result_data.append({"cart_item":result,"matching_buyproduct_data": matching_buyproduct_data})
    return render(request,"cart4_show.html",{"result_datas":result_data})
def deletecode(request,pid):
    wishid = wishlisttbl.objects.get(pid=pid)
    wishid.delete()
    return redirect("../wishlist_show/")

def deletecode1(request,pid):
    wishid = wishlisttbl1.objects.get(pid=pid)
    wishid.delete()
    return redirect("../wishlist1_show/")

def deletecode3(request,pid):
    wishid = wishlisttbl3.objects.get(pid=pid)
    wishid.delete()
    return redirect("../wishlist3_show/")

def deletecode4(request,pid):
    wishid = wishlisttbl4.objects.get(pid=pid)
    wishid.delete()
    return redirect("../wishlist4_show/")

def navbarcode(request):
    a=request.POST['navbarname']
    ins=navbartbl(name=a)
    ins.save()
    return redirect('../navbar/')

def navbar_show(request):
    result=navbartbl.objects.all()
    return render(request,"Admin_Panel/navbar_show.html",{"results":result})

def deletecodee(request,pid):
    cartid = carttbl.objects.get(pid=pid)
    cartid.delete()
    return redirect("../cart_show/")

def deletecodee1(request,pid):
    cartid = carttbl1.objects.get(pid=pid)
    cartid.delete()
    return redirect("../cart1_show/")

def deletecodee5(request,pid):
    cartid = carttbl3.objects.get(pid=pid)
    cartid.delete()
    return redirect("../cart3_show/")

def deletecodee6(request,pid):
    cartid = carttbl4.objects.get(pid=pid)
    cartid.delete()
    return redirect("../cart4_show/")

def reviewcode(request):
    a=request.POST['name']
    b=request.POST['email']
    c=request.POST['comment']
    d=request.POST['rating']
    ins = reviewratingtbl(name=a,email=b,comment=c,rating=d)
    ins.save()
    return redirect('../')


def shippingcode(request):
    b=request.POST['price']
    a=request.POST['cartid']
    d = request.POST['firstname']
    e = request.POST['lastname']
    f = request.POST['number']
    g = request.POST['email']
    h = request.POST['address']
    i = request.POST['pincode']
    j = request.POST['city']
    k = request.POST['state']
    l = request.POST['country']
    ins = ordertbl(cartid=a,price=b,fname=d,lname=e,number=f,email=g,address=h,pincode=i,city=j,state=k,country=l)
    ins.save()
    return redirect(f'../buy_step_4/{a}',{"result":b})


def index1(request,id):
    res1 = carttbl.objects.get(id=id)
    print(res1)
    return render(request,"Razorpay/index1.html",{'res1':res1})

def shipping_data(request):
    result=ordertbl.objects.all()
    return render(request,"Admin_Panel/shipping_data.html",{"results":result})

def invoice_bill(request,id):
    res=ordertbl.objects.get(id=id)
    return render(request,"Admin_Panel/invoice_bill.html",{"res":res})

def order_tracking(request,id):
    return render(request,"order_tracking.html")

def shipping1(request,id):
    res=ordertbl.objects.get(id=id)
    if request.method=='POST':
        action=request.POST.get('action')
    return render(request,"Admin_Panel/shipping1.html",{'res':res,'action':action})

def updateshipdata(request):
    id=request.POST['id']
    a=request.POST['price']
    b=request.POST['firstname']
    c=request.POST['lastname']
    d=request.POST['number']
    e = request.POST['email']
    f = request.POST['address']
    g = request.POST['pincode']
    h = request.POST['city']
    i = request.POST['state']
    j = request.POST['country']
    k = request.POST['status']
    ins = ordertbl(id=id, price=a,fname=b,lname=c,number=d,email=e,address=f,pincode=g,city=h,state=i,country=j,tracking=k)
    ins.save()
    return redirect('../shipping_data/')



def track_order(request,id):
    res=ordertbl.objects.get(id=id)
    return render(request,"track_order.html",{'res':res})

# Search functionality.
# def search(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#
#     items = categorytbl.objects.filter(
#         Q(name__icontains=q)
#     )
#     subcategory_results = addproducttbl.objects.filter(name__icontains=q)
#
#     # Append subcategory_results to items list
#     items = list(items) + list(subcategory_results)
#
#     context = {'items': items }
#     return render(request, 'search.html', context)


def tryon(request):
    return render(request,"tryon.html")

def order_data_show(request):
    orderdata = ordertbl.objects.all()
    return render(request,"order_data_show.html",{'orderdata':orderdata})


# def services(request):
#     ServiceData = addproducttbl.objects.all()
#     if request.method=="GET":
#         st=request.GET.get('servicename')
#         if st!=None:
#            ServiceData = addproducttbl.objects.filter(service_titile__icontains=st)
#     data={
#         'servicesData':ServiceData
#     }
#     return render(request,"index.html",data)


def categorydelete(request,id):
    dell=navbartbl.objects.get(id=id)
    dell.delete()
    return redirect("../navbar_show/")

def ratingdelete(request,id):
    dell=ratingtbl.objects.get(id=id)
    dell.delete()
    return redirect("../rating/")

def category_edit(request,id):
    editdata=navbartbl.objects.get(id=id)
    return render(request,"category_edit.html",{'editdata':editdata})

def cateditcode(request):
    id=request.POST['id']
    a=request.POST['navbarname']
    ins=navbartbl(id=id,name=a)
    ins.save()
    return render(request, "category_edit.html")





