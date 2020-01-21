from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Person
from .forms import PersonForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the apiperson index.")


def persons(request):
    
    json_resp = list_persons()

    return JsonResponse(json_resp)

# Lists all persons in the database
def list_persons():
    ret_resp = {}
    person_list = Person.objects.all()
    for person in person_list:
        ret_resp[person.id] = {
            "first_name": person.first_name, 
            "last_name": person.last_name, 
            "email_address": person.email_address
            }
    return ret_resp

# Lists all persons in the database
def get_person(request, person_id):
    ret_resp = {}
    person = Person.objects.get(id=person_id)
    
    ret_resp[person.id] = {
        "first_name": person.first_name, 
        "last_name": person.last_name, 
        "email_address": person.email_address
        }
    return JsonResponse(ret_resp)

# Create a new person
def create_person(request):

    if request.method == 'POST':
        form = PersonForm(request.POST)
        ret_resp = {}
        
        if form.is_valid():
        
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            e_address = form.cleaned_data['email_address']
            new_person = Person(first_name=f_name, last_name=l_name, email_address=e_address)
            new_person.save()

            ret_resp[new_person.id] = {
                "first_name": new_person.first_name, 
                "last_name": new_person.last_name, 
                "email_address": new_person.email_address
                }
            return JsonResponse(ret_resp)

    else:
        form = PersonForm()
    return render(request, 'person_form.html', {'form': form})

   