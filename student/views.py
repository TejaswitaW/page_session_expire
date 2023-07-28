from django.shortcuts import render,HttpResponse

def setsession(request):
    request.session['name'] = 'Ram'
    return render(request,'student/setsession.html')

def getsession(request):
    if 'name' in request.session:
        name = request.session['name'] 
        # if some modification then reset the session time
        request.session.modified = True
        return render(request,'student/getsession.html',{'name':name})
    else:
        return HttpResponse("Your session is expired!!!")

def delsession(request):
    request.session.flush()
    request.session.clear_expired()
    return render(request,'student/delsession.html')