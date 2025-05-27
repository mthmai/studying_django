from urllib.parse import urlencode

from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from my_app.abstract_factories import GenericViews
from my_app.generate_qr_code import GenerateQRCode

# Create your views here.

class IndexView(GenericViews):
    def validator(self) -> bool:
        if self.request.path == '/':
            return True
        else:
            return False
        
    def request_page(self):
        if self.request.method == "POST":
            name = self.request.POST.get('name')
            key = self.request.POST.get('key')
            value_pix = self.request.POST.get('value_pix')

            params = urlencode({
                'name': name,
                'key': key,
                'value_pix': value_pix
            })

            return redirect(reverse('return_qr_code') + f"?{params}")
        
        return render(self.request, "index.html")
    

class QRCodeView(GenericViews):
    def validator(self) -> bool:
        if self.request.path == '/return_qr_code/':
            return True
        else:
            return False
        
    def request_page(self):
        name = self.request.GET.get("name")
        key = self.request.GET.get("key")
        value_pix = self.request.GET.get("value_pix")

        instance = GenerateQRCode(name=name, 
                                  key=key, 
                                  value_pix=value_pix
                                  )
        img = instance.generate()

        return render(self.request, "return_qr_code.html", {"img_data": img})
    


def index_view(request):
    view = IndexView(request)
    if view.validator():
        return view.request_page()
    return HttpResponseNotFound("Página não encontrada")


def qr_code_view(request):
    view = QRCodeView(request)
    if view.validator():
        return view.request_page()
    return HttpResponseNotFound("Página não encontrada")