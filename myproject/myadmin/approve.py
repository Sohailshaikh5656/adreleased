




from django.core.mail import send_mail
import uuid
from django.conf import settings


def send_mail_to_user(email,fname,lname):

	
	subject = 'Your Order has been Approved'
	message = f'Hi,{fname} {lname}\nYour order has been approved and send to agency, \nThanks and regardss'
	email_form = settings.EMAIL_HOST_USER
	recipient_list = [email]
	send_mail(subject, message, email_form, recipient_list)
	return True