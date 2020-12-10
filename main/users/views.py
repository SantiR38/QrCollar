"""Users View"""

# Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



@login_required()
def secret_page(request, *args, **kwargs):
    return HttpResponse('Secret contents!', status=200)