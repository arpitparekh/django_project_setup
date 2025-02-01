from django.shortcuts import render
# User Cration form
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def showIntroPage(request):

  fruits = ['apple','banana','orange','grape','mango','strawberry','pineapple','watermelon','peach','pear','plum','pomegranate','raspberry','blackberry','blueberry','cranberry','gooseberry','goji berry','juniper berry','kiwi fruit','kumquat','lemon','lime','lychee','mandarine','mulberry','nectarine','orange','papaya']

  form = UserCreationForm()

  return render(request, 'intro.html',{'name':"Bascom Bridge","fruits":fruits,"form":form})
