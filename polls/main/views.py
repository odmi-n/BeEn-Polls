from django.shortcuts import render

# Create your views here.
def index(request):  # ビュー関数を定義
    return render(request, "main/index.html")