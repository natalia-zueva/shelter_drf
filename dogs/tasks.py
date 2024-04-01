import datetime

from celery import shared_task

from dogs.models import Dog


@shared_task
def send_message_about_like(chat_id):
    print(f"Сообщение отправлено в чат {chat_id}")


def send_birthday_mail():
    dog_list = Dog.objects.filter(date_birth=datetime.date.today())
    for dog in dog_list:
        print(f"Отправить письмо для {dog.owner.username}")
