from django.shortcuts import render
def get_app(request):
    return render(request, 'app.html')
