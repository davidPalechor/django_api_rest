import json

from django.http import HttpResponse
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AdditionalInfo
from .models import BasicInfo


class CreateInfo(View):
    '''
    View for testing POST method
    '''

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        json_response = json.loads(request.body)

        basic_info = BasicInfo.objects.create(
            name=json_response['basicInfo']['name'],
            last_name=json_response['basicInfo']['last_name'],
            tel=json_response['basicInfo']['tel'],
            email=json_response['basicInfo']['email'],
            address=json_response['basicInfo']['address']
        )

        if json_response['additionalInfo']:
            AdditionalInfo.objects.create(
                art=json_response['additionalInfo'].get('art'),
                movies=json_response['additionalInfo'].get('movies'),
                music=json_response['additionalInfo'].get('music'),
                basic_info=basic_info,
            )

        return HttpResponse('success', status=200)


class InfoListView(ListView):
    '''
    View for testing GET method
    '''
    model = BasicInfo

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        queryset = self.get_queryset()
        data = []
        for info in queryset:
            data.append({
                'name': info.name,
                'last_name': info.last_name,
                'telephone': info.tel,
                'email': info.email,
                'address': info.email,
            })

        return JsonResponse({'data': data}, status=200)

    def post(self, request):
        return HttpResponse(
            'Method not allowed, request via GET instead',
            status=405
        )
