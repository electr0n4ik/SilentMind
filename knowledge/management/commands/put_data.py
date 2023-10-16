from django.core.management import BaseCommand
from django.utils import timezone

from users.models import User
from knowledge.models import Course, Lesson, Payment


class Command(BaseCommand):

    def handle(self, *args, **options):
        superuser, _ = User.objects.get_or_create(
            email='superuser@gmail.com',
            defaults={'is_superuser': True, 'is_staff': True}
        )
        superuser.set_password('superuser')
        superuser.save()

        manager, _ = User.objects.get_or_create(
            email='manager@gmail.com',
            defaults={'is_staff': True}
        )
        manager.set_password('manager')
        manager.save()

        user1, _ = User.objects.get_or_create(
            email='user1@gmail.com'
        )
        user1.set_password('user1')
        user1.save()

        user2, _ = User.objects.get_or_create(
            email='user2@gmail.com'
        )
        user2.set_password('user2')
        user2.save()

        user3, _ = User.objects.get_or_create(
            email='andreyshka3@gmail.com'
        )
        user3.set_password('user3')
        user3.save()

        course_list = [
            {'title': 'Python-Dev', 'description': 'SkyPro - лучшие курсы', "preview": ""},
            {'title': 'Python-QA', 'description': 'SkyPro - лучшие тесты', "preview": ""}
        ]
        for element in course_list:
            Course.objects.create(**element)

        lesson_list = [
            {'course': Course.objects.get(id=1), 'title': '1 урок Python-Dev', 'description': 'SkyPro - лучшие уроки',
             "preview": ""},
            {'course': Course.objects.get(id=2), 'title': '2 урок Python-QA',
             'description': 'SkyPro - лучшие тестовые уроки', "preview": ""}
        ]

        for element in lesson_list:
            Lesson.objects.create(**element)

        payment_list = [
            {'user': User.objects.get(id=1), 'data_pay': timezone.now(),
             'lesson': Lesson.objects.get(id=1),
             "value_pay": 9999,
             "method_pay": "cash"},
            {'user': User.objects.get(id=1), 'data_pay': timezone.now() - timezone.timedelta(days=2),
             'course': Course.objects.get(id=1),
             "value_pay": 9999,
             "method_pay": "cash"},
            {'user': User.objects.get(id=2), 'data_pay': timezone.now() - timezone.timedelta(days=1),
             'lesson': Lesson.objects.get(id=2),
             "value_pay": 9999,
             "method_pay": "non_cash"}
        ]

        for element in payment_list:
            Payment.objects.create(**element)
