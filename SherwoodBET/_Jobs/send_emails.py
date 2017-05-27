from django.contrib.auth.models import User
from django.core.email import send_email

class ConfirmationEmailCreator:
    def __init__(self):
        self.title = '%(username), Please confirm your account'
        self.template = '''
            Welcome to SherwoodBET,\n
            You have registered with this email.
            Please, follow this link, to confirm your account:
            %(link)\n
            Or use the following code:
            %(code)\n
            Regards,
            Team SherwoodBET
        '''

    def create(self, user):
        username = user.username
        confirmation_code = user.profile.confirmation_code
        link = "http://localhost:8000/profile/api/confirm"
        link = link + "#username=" + username + "&confirmation_code=" + confirmation_code
        return self.title % {'username': username}, self.template % {'link': link, 'code': confirmation_code}

class EmailSender:
    def __init__(self):
        self.client = "confirm@sherwoodbet.com"
        self.creator = ConfirmationEmailCreator()
        self.users = []

    def get_bulk(self, size):
        self.users = User.objects.filter(profile__email_attempted=False)[:size]

    def set_attempted(self):
        for user in self.users:
            user.profile.email_attempted = True
            user.profile.save()

    def send(self, title, message, user):
        send_mail(title, message, self.client, [user.email], fail_silently=False)
        user.profile.email_sent = True
        user.profile.save()

    def report_fail(self):
        pass

    def attempt_send(self, user):
        title, message = self.creator.create(user)
        try:
            self.send(title, message, user)
        except:
            self.report_fail()

    def bulk_send(self):
        for user in self.users:
            self.attempt_send(user)

def send_emails():
    s = EmailSender()
    s.get_bulk(50)
    s.set_attempted()
    s.bulk_send()
