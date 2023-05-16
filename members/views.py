from django.shortcuts import render
from .models import Members


# Create your views here.


# Feching all items from Database
def member_index(request):
    """
    Fetching from database
    """
    members = Members.objects.all()
    context = {"members": members}

    return render(request, "member_index.html", context)


# Getting a Single item from Database
def member_detail(request, pk):
    """
    Geting a single item from database
    """
    member = Members.objects.get(pk=pk)
    context = {"member": member}

    return render(request, "member_detail.html", context)
