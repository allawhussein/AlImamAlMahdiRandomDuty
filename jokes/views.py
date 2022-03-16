from email.quoprimime import quote
from django.shortcuts import render
import pyjokes
import random
# Create your views here.
def index(request):
    jokes=pyjokes.get_joke()
    list_of_quotes = ["صلاة على محمد وآل محمد",
    "قراءة سورة يس",
    "زيارة يس",
    "زيارة عاشوراء"]
    quote = random.choice(list_of_quotes)
    return render(request,'index.html',{'jokes':quote})