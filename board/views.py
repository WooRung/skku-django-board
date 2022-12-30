from django.http import HttpResponse


def index(request):
    # print(request)
    # print(type(request))
    print(dir(request))



    return HttpResponse("Hello World, I am Younsoo!")
