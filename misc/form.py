#! /usr/bin/python
import email.message
import smtplib

message = email.message.Message()

s = smtplib.SMTP(mailmerge_conf.smtp_server)
s.starttls()