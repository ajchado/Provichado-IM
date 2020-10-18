from django.http import HttpResponse
from django.http import Http404
from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from .forms import DvdForm, CustomerForm
from .models import DvdRegistration, CustomerRegistration
from django.core.files.storage import FileSystemStorage


# Create your views here.

class MovieHouseIndexView(View):
    def get(self, request):
        # print('get')
        return render(request, 'index.html')
    
    def post(self, request):
        return render(request, 'landing.html')  

class MovieHouseLandingView(View):
    def get(self, request):
        dvds = DvdRegistration.objects.filter(isDeleted = False)

        context = {
            'dvds' : dvds
        }
        return render(request, 'landing.html', context)
    
    def post(self, request):
        if request.method == 'POST':	
            if 'updateview' in request.POST:	
                print('update profile button clicked')
                genres = request.POST.get('genre')
                rd = request.POST.get('releasedate')
                ttl = request.POST.get('title')
                fn = request.POST.get('fname')
                ln = request.POST.get('lname')
                cfn = request.POST.get('cfname')
                cln = request.POST.get('clname')
                prices = request.POST.get('price')
                itemss = request.POST.get('item')
                skus = request.POST.get('ssku')
                #itempic = request.FILES['myFile']
                dvdupdate = DvdRegistration.objects.filter(sku = skus).update( reldate = rd, genre = genres, title = ttl, 
                                                                                dfirstname = fn, dlastname = ln, cfirstname = cfn, clastname = cln,
                                                                                price = prices, items = itemss)
                                                                
                print(dvdupdate)
                print('profile updated')
            elif 'deleteview' in request.POST:	
                print('delete button clicked')
                skus = request.POST.get("ssku")
                dvd = DvdRegistration.objects.filter(sku = skus).update(isDeleted=True)
                print('recorded deleted')
                
            return redirect('moviehouse:landing_view')
                

class MovieHouseDvdRegistrationView(View):
    def get(self, request):
        # print('get')
        return render(request, 'DVDregistration.html')

    def post(self, request):
        form = DvdForm(request.POST)

        if form.is_valid():
            dt = request.POST.get('datetime')
            genres = request.POST.get('genre')
            rd = request.POST.get('releasedate')
            ttl = request.POST.get('title')
            fn = request.POST.get('fname')
            ln = request.POST.get('lname')
            cfn = request.POST.get('cfname')
            cln = request.POST.get('clname')
            prices = request.POST.get('price')
            itemss = request.POST.get('item')
            itempic = request.FILES['myFile']

            # datetime.now().strftime('%Y-%m-%d')

            fs = FileSystemStorage()
            filename = fs.save(itempic.name, itempic)
            file_url = fs.url(filename)
            form = DvdRegistration( dateregistered = dt, reldate = rd, genre = genres, title = ttl, 
                            dfirstname = fn, dlastname = ln, cfirstname = cfn, clastname = cln,
                            price = prices, items = itemss, dvdpic = file_url)

                            # dateregistered = dt, reldate = rd,
            form.save() 
            
        return redirect('moviehouse:landing_view')

class MovieHouseCustomerRegistrationView(View):
        def get(self, request):
        # print('get')
            return render(request, 'CustomerRegistration.html')

#         def post(self, request):
#                 form = CustomerForm(request.POST, request.FILES)

#                 if form.is_valid():
#                     profpic = request.FILES['myFile']
#                     rg = request.POST.get("regdate")
#                     emplid = request.POST.get("empid")
#                     female = request.POST.get("genderf")
#                     male = request.POST.get("genderm")
#                     lgbt = request.POST.get("gendero")
#                     hbd = request.POST.get("bday")
#                     castfn = request.POST.get("castfname")
#                     castmn = request.POST.get("castmname")
#                     castln = request.POST.get("castlname")
#                     st = request.POST.get("street")
#                     brgy = request.POST.get("barangay")
#                     ct = request.POST.get("city")
#                     prov = request.POST.get("province")
#                     zipp = request.POST.get("zip")
#                     countryy = request.POST.get("country")
#                     sngl = request.POST.get("single")
#                     marry = request.POST.get("married")
#                     patay = request.POST.get("widow")
#                     buwag = request.POST.get("divorced")
#                     uyabfn = request.POST.get("sfname")
#                     uyabmn = request.POST.get("smname")
#                     uyabsn = request.POST.get("slname")
#                     trabaho = request.POST.get("occupation")
#                     anak = request.POST.get("children")

#                     form = CustomerRegistration(profilepic = profpic, sku = rg, genre = emplid, title = female, 
#                                                 reldate = male, dfirstname = lgbt, birthday = hbd,
#                                                 firstname = castfn, middlename = castmn, lastname = castln, 
#                                                 street = st, barangay = brgy, city = ct, province = prov, 
#                                                 zipcode = zipp, country = countryy, eldate = sngl, dfirstname = marry, 
#                                                 dlastname = patay, cfirstname = buwag, clastname = uyabfn, price = uyabmn, 
#                                                 items = uyabsn, profilepic = trabaho, profilepic = anak)
#                     form.save() 
                    
#                     return HttpResponse('Success!') 
#                 else:
#                     return HttpResponse('Failed!')