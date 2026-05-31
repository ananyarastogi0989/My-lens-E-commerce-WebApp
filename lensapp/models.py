from django.db import models

# Create your models here.
class formtbl(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    city=models.CharField(max_length=100)

    class Meta:
        db_table="formtbl"

class tabletbl(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    mobile=models.CharField(max_length=20)

    class Meta:
        db_table="tabletbl"

class signuptbl(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    otp=models.CharField(max_length=100)

    class Meta:
        db_table="signuptbl"


class form3tbl(models.Model):
    name=models.CharField(max_length=500)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=500)

    class Meta:
        db_table="form3tbl"

class form3tbl1(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)

    class Meta:
        db_table="form3tbl1"

class steptbl(models.Model):
    fname=models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address= models.CharField(max_length=500)
    pincode= models.CharField(max_length=20)
    dob= models.CharField(max_length=50)
    email= models.CharField(max_length=100)
    password= models.CharField(max_length=20)

    class Meta:
        db_table="steptbl"

class imgtbl(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=20)
    picture=models.FileField(max_length=500)

    class Meta:
        db_table="imgtbl"

class img1tbl(models.Model):
    picture1=models.FileField(max_length=500)
    picture2=models.FileField(max_length=500)
    picture3=models.FileField(max_length=500)

    class Meta:
        db_table="img1tbl"

class categorytbl(models.Model):
    cname= models.CharField(max_length=20)
    Image= models.FileField(max_length=500)

    class Meta:
        db_table="categorytbl"

class pageonetbl(models.Model):
    image= models.FileField(max_length=500)

    class Meta:
        db_table="pageonetbl"


class addproducttbl(models.Model):
    catid=models.CharField(max_length=5)
    pname=models.CharField(max_length=20)
    pdescription=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    quantity=models.CharField(max_length=100)
    brand=models.CharField(max_length=50)
    image=models.FileField(max_length=500)

    class Meta:
        db_table="addproducttbl"

class addproducttbl3(models.Model):
    catid=models.CharField(max_length=5)
    pname=models.CharField(max_length=20)
    pdescription=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    quantity=models.CharField(max_length=100)
    brand=models.CharField(max_length=50)
    image=models.FileField(max_length=500)

    class Meta:
        db_table="addproducttbl3"

class addproducttbl4(models.Model):
    catid=models.CharField(max_length=5)
    pname=models.CharField(max_length=20)
    pdescription=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    quantity = models.CharField(max_length=100)
    brand=models.CharField(max_length=50)
    image=models.FileField(max_length=500)

    class Meta:
        db_table="addproducttbl4"

class customertbl(models.Model):
    sno=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    class Meta:
        db_table="customertbl"

class imgdatatbl(models.Model):
    text=models.CharField(max_length=100)
    image=models.FileField(max_length=500)

    class Meta:
        db_table="imgdatatbl"

class categorytbl2(models.Model):
    name=models.CharField(max_length=100)
    image=models.FileField(max_length=500)

    class Meta:
        db_table="categorytbl2"

class categorytbl3(models.Model):
    image=models.FileField(max_length=500)

    class Meta:
        db_table="categorytbl3"


class addproducttbl2(models.Model):
    catid=models.CharField(max_length=5)
    pname=models.CharField(max_length=20)
    pdescription=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    size=models.CharField(max_length=50)
    quantity=models.CharField(max_length=100)
    brand=models.CharField(max_length=50)
    image=models.FileField(max_length=500)

    class Meta:
        db_table="addproducttbl2"

class buyproducttbl(models.Model):
    catid = models.CharField(max_length=5)
    image1 = models.FileField(max_length=500)
    image2 = models.FileField(max_length=500)
    image3 = models.FileField(max_length=500)
    image4 = models.FileField(max_length=500)
    image5 = models.FileField(max_length=500)
    image6 = models.FileField(max_length=500)
    image7 = models.FileField(max_length=500)
    image8 = models.FileField(max_length=500)
    image9 = models.FileField(max_length=500)
    image10 = models.FileField(max_length=500)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    mid=models.CharField(max_length=100)
    mno=models.CharField(max_length=100)
    msize=models.CharField(max_length=100)
    mwidth=models.CharField(max_length=100)
    mdimension=models.CharField(max_length=100)
    image11=models.FileField(max_length=500)
    image12 = models.FileField(max_length=500)
    image13 = models.FileField(max_length=500)
    image14 = models.FileField(max_length=500)
    image15 = models.FileField(max_length=500)
    image16 = models.FileField(max_length=500)

    class Meta:
        db_table="buyproducttbl"

class buyproducttbl2(models.Model):
    catid = models.CharField(max_length=5)
    image1=models.FileField(max_length=500)
    image2 = models.FileField(max_length=500)
    image3 = models.FileField(max_length=500)
    image4 = models.FileField(max_length=500)
    image5 = models.FileField(max_length=500)
    image6 = models.FileField(max_length=500)
    image7 = models.FileField(max_length=500)
    image8 = models.FileField(max_length=500)
    image9 = models.FileField(max_length=500)
    image10 = models.FileField(max_length=500)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    mid=models.CharField(max_length=100)
    mno=models.CharField(max_length=100)
    msize=models.CharField(max_length=100)
    mwidth=models.CharField(max_length=100)
    mdimension=models.CharField(max_length=100)
    image11= models.FileField(max_length=500)
    image12= models.FileField(max_length=500)
    image13=models.FileField(max_length=500)
    image14=models.FileField(max_length=500)
    image15=models.FileField(max_length=500)
    image16=models.FileField(max_length=500)

    class Meta:
        db_table="buyproducttbl2"

class buyproducttbl3(models.Model):
    catid = models.CharField(max_length=5)
    image1=models.FileField(max_length=500)
    image2 = models.FileField(max_length=500)
    image3 = models.FileField(max_length=500)
    image4 = models.FileField(max_length=500)
    image5 = models.FileField(max_length=500)
    image6 = models.FileField(max_length=500)
    image7 = models.FileField(max_length=500)
    image8 = models.FileField(max_length=500)
    image9 = models.FileField(max_length=500)
    image10 = models.FileField(max_length=500)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    mid=models.CharField(max_length=100)
    mno=models.CharField(max_length=100)
    msize=models.CharField(max_length=100)
    mwidth=models.CharField(max_length=100)
    mdimension=models.CharField(max_length=100)
    image11= models.FileField(max_length=500)
    image12= models.FileField(max_length=500)
    image13=models.FileField(max_length=500)
    image14=models.FileField(max_length=500)
    image15=models.FileField(max_length=500)
    image16=models.FileField(max_length=500)

    class Meta:
        db_table="buyproducttbl3"

class buyproducttbl4(models.Model):
    catid = models.CharField(max_length=5)
    image1=models.FileField(max_length=500)
    image2 = models.FileField(max_length=500)
    image3 = models.FileField(max_length=500)
    image4 = models.FileField(max_length=500)
    image5 = models.FileField(max_length=500)
    image6 = models.FileField(max_length=500)
    image7 = models.FileField(max_length=500)
    image8 = models.FileField(max_length=500)
    image9 = models.FileField(max_length=500)
    image10 = models.FileField(max_length=500)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    mid=models.CharField(max_length=100)
    mno=models.CharField(max_length=100)
    msize=models.CharField(max_length=100)
    mwidth=models.CharField(max_length=100)
    mdimension=models.CharField(max_length=100)
    image11= models.FileField(max_length=500)
    image12= models.FileField(max_length=500)
    image13=models.FileField(max_length=500)
    image14=models.FileField(max_length=500)
    image15=models.FileField(max_length=500)
    image16=models.FileField(max_length=500)

    class Meta:
        db_table="buyproducttbl4"

# class fronttbl(models.Model):
#     title = models.CharField(max_length=100)
#     image1 = models.FileField(max_length=500)
#     image2 = models.FileField(max_length=500)
#     image3 = models.FileField(max_length=500)
#     image4 = models.FileField(max_length=500)
#     image5 = models.FileField(max_length=500)
#     image6 = models.FileField(max_length=500)
#     image7 = models.FileField(max_length=500)
#     image8 = models.FileField(max_length=500)
#     image9 = models.FileField(max_length=500)
#     image10 = models.FileField(max_length=500)
#     image11 = models.FileField(max_length=500)
#
#     class Meta:
#         db_table="fronttbl"

class registrationtbl(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mobileno = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    otp=models.CharField(max_length=20)

    class Meta:
        db_table="registrationtbl"

class editregistrationtbl(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    mobileno = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "editregistrationtbl"

class carttbl(models.Model):
    pid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    image1 = models.FileField(max_length=500)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    class Meta:
        db_table = "carttbl"

class carttbl1(models.Model):
    pid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    image1 = models.FileField(max_length=500)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    class Meta:
        db_table = "carttbl1"

class carttbl3(models.Model):
    pid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    image1 = models.FileField(max_length=500)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    class Meta:
        db_table = "carttbl3"

class carttbl4(models.Model):
    pid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)
    image1 = models.FileField(max_length=500)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.CharField(max_length=100)

    class Meta:
        db_table = "carttbl4"

class buynowtbl(models.Model):
    pid = models.CharField(max_length=100)
    userid = models.CharField(max_length=100)

    class Meta:
        db_table = "buynowtbl"

class wishlisttbl(models.Model):
    pid =  models.CharField(max_length=100)
    userid =  models.CharField(max_length=100)

    class Meta:
        db_table="wishlisttbl"

class wishlisttbl1(models.Model):
    pid =  models.CharField(max_length=100)
    userid =  models.CharField(max_length=100)

    class Meta:
        db_table="wishlisttbl1"

class wishlisttbl3(models.Model):
    pid =  models.CharField(max_length=100)
    userid =  models.CharField(max_length=100)

    class Meta:
        db_table="wishlisttbl3"

class wishlisttbl4(models.Model):
    pid =  models.CharField(max_length=100)
    userid =  models.CharField(max_length=100)

    class Meta:
        db_table="wishlisttbl4"


class navbartbl(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table="navbartbl"

class reviewratingtbl(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)

    class Meta:
        db_table="reviewratingtbl"

class shippingtbl(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table="shippingtbl"

class ratingtbl(models.Model):
    catid=models.CharField(max_length=5)
    email = models.CharField(max_length=100)
    review = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)

    class Meta:
        db_table="ratingtbl"

class ordertbl(models.Model):
    price=models.CharField(max_length=10)
    cartid = models.CharField(max_length=10)
    userid = models.CharField(max_length=10)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    tracking = models.CharField(max_length=100)

    class Meta:
        db_table = "ordertbl"

class billtbl(models.Model):
    fname=models.CharField(max_length=100)
    number=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)

    class Meta:
        db_table="billtbl"

