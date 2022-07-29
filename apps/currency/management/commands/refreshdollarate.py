from django.core.management.base import BaseCommand, CommandError
from requests import request
from apps.currency.models import DollarRate
from utils.stdout_colors import bcolors
class Command(BaseCommand):
    help = 'Gets dollar rate from cbu.uz and updates dollarrate model'

    def handle(self, *args, **options):
        import requests
        self.stdout.write(bcolors.OKBLUE + "Getting currency info cbu.uz..." + bcolors.ENDC)

        try:
            res = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/")
            # response typeni python data  typega ugiramiz
            data = res.json()

            #lestdan birinchi elementni olamiz, sababi birinchi elementda dollar haqida malumot bor
            dollar = data[0]

            #dollar kursini chiqaramiz
            rate = float(dollar["Rate"])

            obj = DollarRate.objects.last()
            if obj:
                obj.rate = rate
                obj.save()
            else:
                DollarRate.objects.create(rate=rate) 


            self.stdout.write(self.style.SUCCESS("Dollar rate has been updated!"))
        except Exception as e:
              self.stdout.write(bcolors.WARNING + e + bcolors.ENDC)

         