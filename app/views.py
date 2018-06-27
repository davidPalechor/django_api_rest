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


class CreateInfoView(View):
    '''
    View for testing POST method
    '''

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        json_response = json.loads(request.body)

        basic_info = BasicInfo.objects.create(
            name=json_response['name'],
            last_name=json_response['last_name'],
            tel=json_response['tel'],
            email=json_response['email'],
            address=json_response['address']
        )

        if (json_response['art'] or
            json_response['movies'] or
            json_response['music']):

            AdditionalInfo.objects.create(
                art=json_response['art'],
                movies=json_response['movies'],
                music=json_response['music'],
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

        return JsonResponse({'data': data}, status=201)

    def post(self, request):
        return HttpResponse(
            'Method not allowed, request via GET instead',
            status=405
        )


class UpdateInfoView(APIView):
    '''
    View for testing PUT method
    '''

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def put(self, request):
        json_response = json.loads(request.body)

        if BasicInfo.objects.filter(email=json_response['email']).exists():
            info = BasicInfo.objects.get(email=json_response['email'])
            info.name = json_response['name']
            info.last_name = json_response['last_name']
            info.tel = json_response['tel']
            info.address = json_response['address']
            info.save()

            if AdditionalInfo.objects.filter(basic_info=info).exists():
                AdditionalInfo.objects.filter(basic_info=info).update(
                    art=json_response['art'],
                    movies=json_response['movies'],
                    music=json_response['music']
                )

            return HttpResponse('Success', status=200)
        return HttpResponse('Object not found', status=404)


class DeleteInfoView(APIView):
    '''
    View for testing DELETE method
    '''

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request):
        json_response = json.loads(request.body)
        print(json_response)
        if BasicInfo.objects.filter(email=json_response['email']).exists():
            BasicInfo.objects.get(email=json_response['email']).delete()

            return HttpResponse('Success', status=200)
        return HttpResponse('Object not found', status=404)
