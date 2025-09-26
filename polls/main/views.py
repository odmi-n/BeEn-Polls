from django.shortcuts import render

# Create your views here.
def index(request):
    question_list = [
        "プログラミングは好きですか？",
        "数学は好きですか？",
        "国語は好きですか？",
    ]
    context = {
        "question_list": question_list,
        "is_polled": True,
        "polled_msg": "投票ありがとうございました。",
        "not_polled_msg": "投票をお願いします。",
    }
    return render(request, "main/index.html", context)