from django.core.management import BaseCommand

from ...models import Client


class Command(BaseCommand):
    help = 'Delete a client.'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')

    def handle(self, *args, **options):
        pk = options.get('pk')
        client = Client.objects.filter(pk=pk).first()
        client.delete()

        self.stdout.write('Client was deleted.')
