#userdifened file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'textutil-2.html')

def analyzer(request):
    inputtext = request.POST.get('text','default')
    removepunctuations = request.POST.get('removepunctuations','off')
    capitalize = request.POST.get('capitalize','off')
    spaceremover = request.POST.get('spaceremover','off')

    if removepunctuations == "on":
        punctuations='''!@#$%^&*()_+-={}[];:><,.?/'"'''
        analyzed = ""
        for char in inputtext:
            if char not in punctuations:
                analyzed = analyzed+char
        user_text = {'Task': 'Removed Puncuations', 'analyzed_text': analyzed}
        inputtext=analyzed

    if capitalize == "on":
        analyzed = ""
        for char in inputtext:
                analyzed = analyzed+char.upper()
        user_text = {'Task': 'Capatalized', 'analyzed_text': analyzed}
        inputtext=analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(inputtext):
            if not (inputtext[index] == " " and inputtext[index + 1]== " "):
                analyzed = analyzed + char
        user_text = {'Task': 'Space removed', 'analyzed_text': analyzed}
        inputtext=analyzed

    if(removepunctuations != "on" and capitalize != "on" and spaceremover != "on"):
        return HttpResponse("You have not selected any operations !!")

    return render(request, 'analyzed.html', user_text)

def about(request):
    return HttpResponse("About Us")
def home(request):
    return HttpResponse("Welcome to the home page of this website")