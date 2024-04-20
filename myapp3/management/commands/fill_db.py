from random import choices
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from myapp3.models import Author, Post

LOREM = 'Работа кода шаблона заключается в том, что он перебирает элементы списка или'\
'словаря с помощью тега for и выводит их на страницу с помощью переменных,'\
'которые обернуты в двойные фигурные скобки. Код представления передает'\
'данные в контекст шаблона, которые затем используются в шаблоне для вывода на'\
'страницу.'


class Command(BaseCommand):
    help = 'Generate fake authors and posts'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Count of user')


    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count+1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count+1):
                post = Post(
                    title = f'Title-{j}',
                    content = ' '.join(choices(text, k=12)),
                    author = author
                )
                post.save()