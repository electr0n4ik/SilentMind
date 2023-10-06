from django.core.management import BaseCommand
from users.models import User
from knowledge.models import Course, Lesson, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        superuser = User.objects.create(
            email='superuser@gmail.com'
        )

        superuser.set_password('superuser')
        superuser.save()

        manager = User.objects.create(
            email='manager@gmail.com',
        )

        manager.set_password('manager')
        manager.save()

        user1 = User.objects.create(
            email='user1@gmail.com',
        )

        user1.set_password('user1')
        user1.save()

        user2 = User.objects.create(
            email='user2@gmail.com',
        )

        user2.set_password('user2')
        user2.save()

        course_list = [
            {'title': 'Python-Dev', 'description': 'SkyPro - лучшие курсы', "preview": ""},
            {'title': 'Python-QA', 'description': 'SkyPro - лучшие тесты', "preview": ""}
        ]

        lesson_list = [
            {'course': 1, 'title': '1 урок Python-Dev', 'description': 'SkyPro - лучшие уроки', "preview": ""},
            {'course': 2, 'title': '1 урок Python-QA', 'description': 'SkyPro - лучшие тестовые уроки', "preview": ""}
        ]

        payment_list = [
            {'user': 1, 'data_pay': '2023-10-05 06:42:28.329296 +00:00', 'lesson': 1, "value_pay": 9999, "method_pay": "cash"},
            {'user': 2, 'data_pay': '2023-09-05 06:42:28.329296 +00:00', 'lesson': 1, "value_pay": 9999, "method_pay": "non_cash"}
        ]

        for element in course_list:
            Course.objects.create(**element)

        for element in lesson_list:
            Lesson.objects.create(**element)

        for element in payment_list:
            Payment.objects.create(**element)
