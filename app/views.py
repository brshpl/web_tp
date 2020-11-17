from django.core.paginator import Paginator
from django.shortcuts import render


tags = [
    {
        'id': idx,
        'name': f'name {idx}',
    } for idx in range(45)
]


questions = [
    {
        'id': idx,
        'title': f'title {idx}',
        'text': 'text text',
        'answ_number': idx,
        'tags': {
            'a': 'a' * idx,
            'b': 'b' * idx,
        },
        'rating': idx,
    } for idx in range(45)
]

answers = [
    {
        'id': idx,
        'text': 'text text',
        'rating': idx,
    } for idx in range(10)
]


def paginate(request, per_page):
    objects_list = questions
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    ques = paginator.get_page(page)
    return ques


def index(request):
    questions_for_page = paginate(request, 10)
    return render(request, 'index.html', {
        'questions': questions_for_page,
    })


def new_question_page(request):
    return render(request, 'ask.html', {})


def login_page(request):
    return render(request, 'login.html', {})


def question_page(request, pk):
    question = questions[pk]
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
    })


def signup_page(request):
    return render(request, 'registration.html', {})


def settings_page(request):
    return render(request, 'settings.html', {})


def tag_page(request, tag_name):
    questions_for_tag = [questions[0], questions[1], questions[2]]
    questions_for_page = questions_for_tag
    return render(request, 'tag.html', {
        'tag_name': tag_name,
        'questions': questions_for_page,
    })


def hot_questions_page(request):
    questions_for_page = paginate(request, 10)
    return render(request, 'hot_questions.html', {
        'questions': questions_for_page,
    })
