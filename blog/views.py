from django.http import HttpResponse


def index(request):
    return HttpResponse('<h2>Главная</h2>')


def about(request, name, age):
    return HttpResponse(f'''
    <h2>О пользователе</h2>
    <p>Имя: {name}</p>
    <i>Возраст: {age}</i>
    ''')


def contact(request, street : str = 'Undefined', building : str = 'Null'):
    return HttpResponse(f'''
    <h2>Наши контакты</h2>
    <p>Мы находимся на улице : {street}</p>
    <i>Номер строения : {building}</i>
    ''')