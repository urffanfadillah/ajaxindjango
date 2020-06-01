from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render

from .models import Person
from .forms import PersonForm

# Create your views here.
def indexView(request):
    form        = PersonForm()
    template    = 'index.html'
    context     = {
         'person': Person.objects.all(),
         'form': form,
    }
    
    return render(request, template, context)

def postPerson(request):
    # request harus ajax dan methodnya harus POST
    if request.is_ajax and request.method    ==  "POST":
        # ambil data form
        form    = PersonForm(request.POST)
        # simpan data dan ambil object dari instance
        if form.is_valid():
            instance    = form.save()
            # sambungkan object person baru di json
            ser_instance    = serializers.serialize('json', [instance, ])
            # kirim ke sisi client
            return JsonResponse({'instance': ser_instance}, status=200)
        else:
            # beberapa pesan form kesalahan ditambahkan
            return JsonResponse({'error': form.errors}, status=400)
    # beberaoa error ditambahkan
    return JsonResponse({'error': ''}, status=400)

def checkNickName(request):
    # requestnya harus ajax dan method nya harus GET
    if request.is_ajax and request.method == 'GET':
        # ambil nickname dari clientside
        nick_name = request.GET.get("nick_name", None)
        # cek nick_name di database
        if Person.objects.filter(nick_name = nick_name).exists():
            # jika nick_name ditemukan
            return JsonResponse({"valid":False}, status=200)
        else:
            return JsonResponse({"valid":True}, status = 200)
    return JsonResponse({}, status = 400)