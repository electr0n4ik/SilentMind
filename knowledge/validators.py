import re

from rest_framework.serializers import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile('^[a-zA-Z0-9.\-\ ]+$')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Title is not ok')


class UrlYouTubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'https?://(www\.)?youtube\.com/.*')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Url is not ok')
