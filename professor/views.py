from django.shortcuts import render

def professor_page(request):
    return render(request, 'index_professor.html')