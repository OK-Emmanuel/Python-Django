from django.shortcuts import render
from django.http import HttpResponse
# Import  models
from .models import Feature


# Create your views here.
def index(request):
   feature1 = Feature()
   feature1.id = 0
   feature1.name = 'Fast'
   feature1.details = 'Our Service is very quick' 

   feature2 = Feature()
   feature2.id = 1
   feature2.name = 'Secure'
   feature2.details = 'Our Service are quick an reliable' 

   feature3 = Feature()
   feature3.id = 2
   feature3.name = 'Professional'
   feature3.details = 'Our Service are professional' 

   #Create a List to Include multiple content
   features = [feature1, feature2, feature3]


   return render(request, 'index.html', {'features': features})

def counter(request):
    text = request.POST['text'] 
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})