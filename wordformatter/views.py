from django.shortcuts import render

def home(request):

    rawtext = request.POST.get('text', False)
    print(rawtext)

    return render(request, 'home.html',{'data': rawtext})

def result(request):
    return render(request, 'result.html')