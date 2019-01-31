from celery import shared_task
import time
from django.core.mail import send_mail

@shared_task
def sendverificationemail(email):
  '''print('About to connect with smtp server')
  time.sleep(60) # simulate a long running operation
  print('Email sent to {0}'.format(email))'''

  send_mail('Hi', 'Hey how r u', 'admin@gmail.com', ['mehul@gmail.com','curtly@gmail.com'])