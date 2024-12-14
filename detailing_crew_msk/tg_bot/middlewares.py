# https://docs.djangoproject.com/en/5.1/ref/middleware/

from detailing.models import ClientUser

class RemindersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.is_executed = False

    def __call__(self, request):
        if not self.is_executed:
            # Код, который нужно выполнить только один раз при запуске
            # now = Сегодняшняя дата
            # queryset = ClientUser.objects.filter(next_visit=now)
            # if queryset.exists():
            #     отправить админу напоминания о данных клиентах

            self.is_executed = True
    
        response = self.get_response(request)
        return response