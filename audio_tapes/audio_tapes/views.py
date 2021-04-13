from django.http import HttpResponse

def index(request):
    content = "Welcome to Audio Tapes API. Please refer Github Readme page for more information"
    return HttpResponse(content)