from django.core.management import BaseCommand
from users.models import User
from knowledge.models import Course, Lesson, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_list = [
            {'name': 'Фрукты', 'description': 'Обычно сладкие'},
            {'name': 'Овощи', 'description': 'Растут на грядках'},
        ]

        product_list = [
            {'name': 'Апельсин', 'description': 'Сладкий и оранжевый', "photo": "catalog/апельсин.png", "price": 100,
             "category_id": 1},
            {'name': 'Яблоко', 'description': 'Кислый и зеленый', "photo": "catalog/яблоко.jpeg", "price": 200,
             "category_id": 1},
            {'name': 'помидора', 'description': 'Красная', "photo": "catalog/помидора.png", "price": 300,
             "category_id": 2},
        ]

        blog_entry_list = [
            {'title': 'Первая запись', 'slug': 'pervaya-zapis', 'content': 'Содержимое первой записи блога',
             'preview': 'blog/апельсин.png', 'is_published': True, 'view_count': 10},
            {'title': 'Вторая запись', 'slug': 'vtoraya-zapis', 'content': 'Содержимое второй записи блога',
             'preview': 'blog/помидора.png', 'is_published': True, 'view_count': 20},
            {'title': 'Третья запись', 'slug': 'tretaya-zapis', 'content': 'Содержимое третьей записи блога',
             'preview': 'blog/яблоко.jpeg', 'is_published': False, 'view_count': 5},
            {'title': 'Четвертая запись', 'slug': 'chetvertaya-zapis', 'content': 'Содержимое четвертой записи блога',
             'preview': 'blog/4.png', 'is_published': True, 'view_count': 15},
            {'title': 'Пятая запись', 'slug': 'pyataya-zapis', 'content': 'Содержимое пятой записи блога',
             'preview': 'blog/5.png', 'is_published': True, 'view_count': 8},
        ]

        for element in category_list:
            Category.objects.create(**element)

        for element in product_list:
            Product.objects.create(**element)

        for element in blog_entry_list:
            Blog.objects.create(**element)
