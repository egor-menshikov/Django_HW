from django.core.management import BaseCommand

from ...models import Client


class Command(BaseCommand):
    help = 'Read a client\'s data'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()

        self.stdout.write(f'{client}')
