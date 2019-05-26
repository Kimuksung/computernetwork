from django.shortcuts import render

# Create your views here.
def addid(request):
    return render(request, 'network/ID.html', {})
