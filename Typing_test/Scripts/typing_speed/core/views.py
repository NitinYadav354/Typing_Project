from django.shortcuts import render

# Create your views here.
def typing_test(request):
    return render(request, 'typing_speed/templates/typing_test.html')