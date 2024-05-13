# i have created this file- Wali Khan
from django.http import HttpResponse
from django.shortcuts import render
#Code For Video 6
"""
def index(request):
    return HttpResponse('''<h1>Persoanl Navigate </h1><a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django code with harry</a><br></br>
        <a href="https://www.rgpv.ac.in/Login/StudentLogin.aspx">Rgpv webstiel</a><br></br>
        <a href="https://mail.google.com/mail/u/0/#inbox">Gmail website</a> <br></br>
        <a href="https://www.google.com/">google </a> <br></br>
        <a href="https://github.com/">git hub</a>''') 

def about(request):
    return HttpResponse("about wali khan")"""
def index(request):
    #params={'name':'wali','place':'U.P'}
    return render(request,'index.html')

    #return HttpResponse("Home")
def analyze(request):
    djtext=request.POST.get('text','default')
    #check checkbox values
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    NewlineRemover=request.POST.get('NewlineRemover','off')
    ExtraSpaceRemover=request.POST.get('ExtraSpaceRemover','off')
    CharacterCounter=request.POST.get('CharacterCounter','off')
    #print(removepunc)
    #print(djtext)
    # check which checkbox is on
    if removepunc=="on":
        punchutation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punchutation:
                analyzed=analyzed+char
        params={'purpose':'removed punchutation','analyzed_text':analyzed}
        djtext=analyzed
        #Analyze your text
        #return render(request,'Analyze.html',params)
    elif(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'changed to uppercase','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'Analyze.html',params)
    elif (NewlineRemover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n'and char!='\r':
                analyzed=analyzed+char
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'Analyze.html',params)
    elif (ExtraSpaceRemover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed+=char
        params={'purpose':'Removed ExtraSpace','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'Analyze.html',params)
    elif (CharacterCounter=='on'):
        analyzed=len(djtext)
        params={'purpose':'Counter the Character','analyzed_text':"Number of Character in a Text is: "+str(analyzed)}

    if(removepunc!='on' and fullcaps!='on' and NewlineRemover!='on'and ExtraSpaceRemover!='on'and CharacterCounter!='on'):
        return HttpResponse("Error")
    
    return render(request,'Analyze.html',params)
    

'''def removepunc(request):
    # get the text 
    djtext=(request.GET.get('text','default'))
    print(djtext)
    # Analyze the text
    return HttpResponse("Remove Punc <a href='/'>back</a>")
def capitilizeFirst(request):
    return HttpResponse("Capitilize First <a href='/'>back</a>")
def newlineRemove(request):
    return HttpResponse("New Line Remove <a href='/'>back</a>")
'''