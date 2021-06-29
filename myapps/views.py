from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from .models import Devis, DevisDemande
from .forms import DevisForm,DevisDemandeForm


def index(request):
    festival_list = ["Birthday", 'Holi', 'Diwali']
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request=request))


def tarifs(request):
    name = "kamel"
    if request.method == "POST" and "submit1" in request.POST:
        form = DevisForm(request.POST)
        if form.is_valid():
    
            firstname = request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            statut = request.POST.get('statut')
            phone = request.POST.get("phone")
            website = request.POST.get("website")
            description = request.POST.get("description")

            if Devis.objects.filter(email=email).exists():
                messages.info(request,'email est déjà pris,veuillez changer')
                template = loader.get_template('home.html')
                return HttpResponse(template.render(request=request))
            elif Devis.objects.filter(phone=phone).exists():
                messages.info(request,'ce numero de tel est déjà pris,veuillez changer')
                template = loader.get_template('home.html')
                return HttpResponse(template.render(request=request))
            else:
                devis= Devis(firstname=firstname,lastname=lastname,email=email,statut=statut,
                         phone=phone, website=website,description=description)
                devis.save()
                messages.success(request, "votre message a bien éte envoyé ")
                template = loader.get_template('home.html')
                return HttpResponse(template.render(request=request))
    else:
        #messages.success(request, "Your message has been successfully sent")
        #template = loader.get_template('home.html')
        #return HttpResponse(template.render(request=request))
        messages.success(request, "Votre message n'a pas été envoyé veuillez completer le formulaire")
        form = DevisForm()
        return render(request, 'home.html', {'form': form})
        

    if request.method == "POST" and "submit" in request.POST:
        form1 = DevisDemandeForm(request.POST)
        if form1.is_valid():
                       
            firstname= request.POST.get("firstname")
            lastname = request.POST.get("lastname")
            email = request.POST.get("email")
            phone= request.POST.get("phone")
            statut= request.POST.get("statut")
            pack_choice = request.POST.get("pack_choice")
            description = request.POST.get("description")
            if DevisDemande.objects.filter(email=email1).exists():
                messages.info(request,'email est déjà pris,veuillez changer')
                template = loader.get_template('home.html')
                return HttpResponse(template.render(request=request))
            elif DevisDemande.objects.filter(phone=phone).exists():
                messages.info(request,'ce numero de tel est déjà pris,veuillez changer')
                template = loader.get_template('home.html')
                return HttpResponse(template.render(request=request))
            else:
                devisdemande = DevisDemande (firstname=firstname, lastname=lastname, email=email,
                                             phone=phone, statut=statut, pack_choice=pack_choice,description=description)
                messages.success(request, "votre message a bien éte envoyé ")
                devis.save()
                template = loader.get_template('home.html')
                return HttpResponse(template.render(request=request))
                


        else:
            messages.success(request, "Votre message n'a pas été envoyé ")
            template = loader.get_template('home.html')
            return HttpResponse(template.render(request=request))
    else:
        #messages.success(request, "Your message has been successfully sent")
        #template = loader.get_template('home.html')
        #return HttpResponse(template.render(request=request))
        messages.success(request, "Votre message n'a pas été envoyé veuillez completer le formulaire")
        form = DevisDemandeForm()
        return render(request, 'home.html', {'form': form})
   

        # return HttpResponseRedirect(self.request.path_info)
        # return render(request, 'home.html')
        # return redirect('settings:tarifs')
        # return HttpResponseRedirect(self.get_success_url())
