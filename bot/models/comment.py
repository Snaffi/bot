from django.db import models


class TelegramModel(models.Model):
    class Meta:
        abstract = True

    id = models.BigIntegerField(primary_key=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=100, blank=True)

    def to_json(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'type': self.type,
        }


class TelegramUser(TelegramModel):
    pass


class ChatType:
    group = 'group'
    private = 'private'
    channel = 'channel'
    supergroup = 'supergroup'


class TelegramChat(TelegramModel):
    title = models.CharField(max_length=255, blank=True)

    def to_json(self):
        result = super().to_json()
        result['title'] = self.title
        return result


class TelegramMessage(models.Model):
    class Meta:
        unique_together = ('telegram_message_id', 'chat')

    telegram_message_id = models.BigIntegerField()
    chat = models.ForeignKey(TelegramChat)
    to_user = models.ForeignKey(
        TelegramUser,
        null=True,
        blank=True,
        related_name='to_user',
    )
    from_user = models.ForeignKey(TelegramUser, related_name='from_user')
    text = models.TextField(blank=True)
    date = models.DateTimeField()

    def to_json(self):
        return {
            'id': self.id,
            'telegram_message_id': self.telegram_message_id,
            'chat_id': self.chat_id,
            'to_user': self.to_user_id,
            'from_user': self.from_user_id,
            'text': self.text,
            'date': int(self.date.timestamp())
        }
