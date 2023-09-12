from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'James Zefanya Tumbelaka',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
