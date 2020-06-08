from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # return HttpResponse('Hello')
    return render(request,'home.html')
def eggs(request):
    return HttpResponse('<h1>EGGS</h1>')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    dic = {}
    for word in wordlist:
        if word in dic:
            dic[word] += 1
        else:
            dic[word] = 1
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddic':dic})
def about(request):
    import datetime
    week = datetime.datetime.today().isocalendar()[1]
    return render(request,'about.html',{'week':week})
