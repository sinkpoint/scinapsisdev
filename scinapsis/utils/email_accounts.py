from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
import csv
import os

template_file = 'email_template.html'
from_email = 'tomleung@scinapsis.com'
subject = "Your personal Scinapsis login information"
ctx = []

file = 'test.csv'
with open(file, 'rU') as fp:
    reader = csv.DictReader(fp, quoting=csv.QUOTE_NONE)
    for row in reader:
        print row
        ctx.append({
            'to':[row['email']],
            'subject':subject,
            'data':{'firstname':row['first'].title(),'login':row['username'],'password':row['password']}
        })
        ctx.append(row)

from django.template import Template

template_buf = ''
with open(template_file,'rU') as fp:
    template_buf = fp.read()

mtemp = Template(template_buf)
for i in ctx:
    message = mtemp.render(Context(i['data']))
    print message
    msg = EmailMessage(i['subject'], message, to=i['to'], from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()
