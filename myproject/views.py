# My first Django app
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   # params = {'name':'Sami','place':'Pakistan'}
    return render(request, 'index.html')
#    return HttpResponse('''<h1>Hello world In My First Program</h1> <a href ="https://www.coursera.org/programs/dlsei-phase-2-52jvh?authMode=login&currentTab=CATALOG"> Django with Samiullah </a>
#     <br><a href = "https://www.coursera.org/programs/dlsei-phase-2-52jvh?currentTab=MY_COURSES"> Django With Samiullah</a><br>
#     <a href = "https://www.fiverr.com/inbox/samiullahsal387">Samiullah Is Django Developer</a>''')

def hello(request):
    return HttpResponse('''<h1>Hello Samiullah</h1> <a href = "http://127.0.0.1:8000/remover"> Remover</a>
    <br>
    <h1>home Samiullah</h1> <a href = "http://127.0.0.1:8000/home"> home</a>
    <br>
    <h1>Cutt Samiullah</h1> <a href = "http://127.0.0.1:8000/cutter"> cutter</a>
    <br>
    <h1>space Samiullah</h1> <a href = "http://127.0.0.1:8000/space"> space</a>
    <br>
    ''')

def analyze(request):
    #get the text from frontend
    #check the ckechbox value
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','Off')
    fullcaps = request.POST.get('fullcaps','Off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    Charactedcounter = request.POST.get('Charactedcounter','off')
    print(djtext)
    print(removepunc)
    print(fullcaps)
    print(newlineremover)
    print(extraspaceremover)
    print(Charactedcounter)
    #analyzed = djtext
    #will check wheter checkbox is on the do this
    if (removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
            params = {'purpose': "Removed Punctuation", 'analyzed_text': analyzed}
            # Analyze the text
            djtext = analyzed
            #return render(request, "analyzer.html", params)
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': "Uppered Case", 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed
        #return render(request, "analyzer.html", params)
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != ('\n') and char != ('\r'):
                analyzed = analyzed + char
        params = {'purpose': "Newline Remover", 'analyzed_text': analyzed}
        # Analyze the text
        djtext = analyzed

        #return render(request, "analyzer.html", params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char

        params = {'purpose': "Extraspace Remover", 'analyzed_text': analyzed}
        # Analyze the text
    
    if (removepunc != "on" and extraspaceremover != "on" and newlineremover != "on" and fullcaps != "on" ):
        return HttpResponse("Mzy na khen")
        #return render(request, "analyzer.html", params)
    #if(Charactedcounter == "on"):
     #   analyzed = ("Characters in Your strings are:"  +str(len(djtext)))
     #   params = {'purpose': "Character counter", 'analyzed_text': analyzed}
        # Analyze the text
     #   djtext=analyzed
        #return render(request, "analyzer.html", params)
   # else:
     #   return HttpResponse("Error")
    return render(request, "analyzer.html", params)
    #return  HttpResponse("Here we will analyze your text")
def aboutus(request):
    return render(request,'aboutus.html')
  #  return  HttpResponse("Cutter")
#def space(request):
  #  return  HttpResponse("space")
#def home(request):
  #  return  HttpResponse("home")
##return HttpResponse("Samiullah <a href = '/'>Back</a>")
    #return render( request, 'index.html')


