from django.db import models


class Comment(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.TextField('Текст')
    views_count = models.IntegerField('Количество просмотров', default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.user.username, self.text)

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user_id,
            'text': self.text,
            'created': int(self.created.timestamp()),
        }
