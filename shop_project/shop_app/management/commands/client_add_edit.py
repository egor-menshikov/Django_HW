from django.core.management import BaseCommand

from ...models import Client


class Command(BaseCommand):
    help = 'Add a new client or edit an existing one, if id is provided.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-pk',
            action='store',
            dest='pk',
            type=int,
            default=None,
            help='Client id.'
        )

        parser.add_argument(
            '-name',
            action='store',
            dest='name',
            type=str,
            default=None,
            help='Client name.'
        )

        parser.add_argument(
            '-email',
            action='store',
            dest='email',
            type=str,
            default=None,
            help='Client email.'
        )

        parser.add_argument(
            '-phone',
            action='store',
            dest='phone',
            type=str,
            default=None,
            help='Client phone.'
        )

        parser.add_argument(
            '-address',
            action='store',
            dest='address',
            type=str,
            default=None,
            help='Client address.'
        )

    def handle(self, *args, **options):
        pk = options.pop('pk', None)

        if not pk:
            client = Client(
                name=options.get('name'),
                email=options.get('email'),
                phone=options.get('phone'),
                address=options.get('address'),
            )
            client.save()
            self.stdout.write('Client saved.')

        else:
            client = Client.objects.filter(pk=pk).first()

            fields = options.keys()
            for field in fields:
                if options.get(field):
                    client.__setattr__(field, options.get(field))
            client.save()

            self.stdout.write(f'Client {client.pk} updated.')
