from django.shortcuts import render


def run_index(request):
    return render(request, 'cliche/index.html')
