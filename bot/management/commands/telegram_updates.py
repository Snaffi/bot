import datetime

import telegram
from django.conf import settings
from django.core.management.base import BaseCommand

from bot.models import TelegramMessage, TelegramChat, ChatType, TelegramUser


class Command(BaseCommand):
    def handle(self, *args, **options):
        bot = telegram.Bot(settings.TELEGRAM_BOT_TOKEN)
        list(map(self.process_message, bot.getUpdates()))

    def process_message(self, update_object: telegram.Update) -> TelegramMessage:
        message = update_object.message
        telegram_message = TelegramMessage.objects.filter(
            chat_id=message.chat_id,
            telegram_message_id=message.message_id,
        ).first()

        if telegram_message:
            return telegram_message

        telegram_chat, _ = TelegramChat.objects.update_or_create(
            id=message.chat_id,
            defaults=dict(
                type=message.chat.type,
                title=message.chat.title,
                last_name=message.chat.last_name,
                first_name=message.chat.first_name,
                username=message.chat.username,
            )
        )

        from_user, _ = TelegramUser.objects.update_or_create(
            id=message.from_user.id,
            defaults=dict(
                type=message.from_user.type,
                last_name=message.from_user.last_name,
                first_name=message.from_user.first_name,
                username=message.from_user.username,
            )
        )

        telegram_message = TelegramMessage(
            chat=telegram_chat,
            text=message.text,
            from_user=from_user,
            telegram_message_id=message.message_id,
            date=message.date,
        )
        telegram_message.save()
        return telegram_message
