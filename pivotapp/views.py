import datetime as dt

from .forms import *

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django_pandas.io import read_frame
from pivottablejs import pivot_ui
import shutil
import os

class UsersDetailsAPI(APIView):

    @staticmethod
    def get(request, pk):
        user_obj = get_object_or_404(UsersDetails, active=True, id=pk)
        serializer = UsersDetailsSerializers(user_obj).data
        return Response(serializer)

    def post(self, request, pk=None):

            serializer = UsersDetailsSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response("Data added successfully")

def dashboard(request):
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            fdate = form.cleaned_data['fdate']
            tdate = form.cleaned_data['tdate']
            qs = UsersDetails.objects.filter(dob__range=[fdate, tdate])
            df = read_frame(qs)
            pivot_ui(df)
            print (os.path.abspath(os.getcwd())+"/pivottablejs.html")
            print(os.path.abspath(os.getcwd()) + "/pivotapp/templates")
            shutil.copy(os.path.abspath(os.getcwd())+"/pivottablejs.html",
                                  os.path.abspath(os.getcwd()) + "/pivotapp/templates")
            return render(request, 'pivottablejs.html', {})
    else:
        form = DashboardForm()
    return render(request, 'base.html', {'form': form})