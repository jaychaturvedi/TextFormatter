from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def result(request):
    rawtext = request.POST.get('text', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    removeline = request.POST.get('removeline', 'off')
    trim = request.POST.get('trim', 'off')

    if(len(rawtext)==0):
        return render(request, 'home.html',{'error':'Please enter text to format'})
    
    if(uppercase == 'on'):
        testdata = ''
        for i in rawtext:
            testdata += i.upper()
        rawtext = testdata

    if(lowercase=='on'):
        testdata = ''
        for i in rawtext:
            testdata += i.lower()
        rawtext = testdata

    if(removepunc=='on'):
        testdata = ''
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for i in rawtext:
            if i not in punctuations:
                testdata+=i
        rawtext = testdata
            


    if(removeline=='on'):
        testdata = ''
        for i in rawtext:
            if (i != '\n' and i!='\r'):
                testdata+=i
            else:
                testdata+=' '

        rawtext = testdata
                

    if(trim=='on'):
        testdata = ''
        for i,j in enumerate(rawtext):
            if not(rawtext[i]==' ' and rawtext[i+1] == ' ' ):
                testdata+=j

        rawtext = testdata.strip()

    if (uppercase!='on' and lowercase!='on'  and trim!='on'  and removeline!='on'  and removepunc!='on' ):
        return render(request, 'home.html',{'error':'Please select option to format text'})
        

    return render(request, 'result.html',{'data':rawtext})