from django.shortcuts import render

def show_main_page(request):
    return render(request, 'main/main_page.html')


def cryptoprojects_page(request):
    return render(request, 'main/test.html')