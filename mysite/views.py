from django.http import HttpResponse,JsonResponse


def http_test(request) :
    return HttpResponse('http-test my first try :)')


def json_test(request):
    return JsonResponse({'name':'ali'})