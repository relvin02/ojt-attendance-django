#!/usr/bin/env python
"""Test script to verify Gmail SMTP email sending"""
import os
import sys
import django
from django.core.mail import EmailMessage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ojt_project.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from attendance.models import Student
from django.conf import settings

print("=" * 60)
print("TESTING GMAIL SMTP EMAIL SENDING")
print("=" * 60)
print(f"\nEmail Backend: {settings.EMAIL_BACKEND}")
print(f"Email Host: {settings.EMAIL_HOST}")
print(f"Email Port: {settings.EMAIL_PORT}")
print(f"Use TLS: {settings.EMAIL_USE_TLS}")
print(f"From Email: {settings.DEFAULT_FROM_EMAIL}")

# Get the first student with email
student = Student.objects.filter(email__isnull=False).first()
if not student:
    print("\n❌ No students with email addresses found!")
    sys.exit(1)

print(f"\n📧 Sending test email to: {student.email}")
print(f"Student: {student.first_name} {student.last_name}")

try:
    # Create and send test email
    email = EmailMessage(
        subject="OJT Attendance System - Test Email",
        body="Hello! This is a test email from the OJT Attendance System. If you received this, Gmail SMTP is working correctly!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[student.email]
    )
    result = email.send()
    
    if result == 1:
        print("✅ Email sent successfully!")
    else:
        print("❌ Email sending failed (returned 0)")
except Exception as e:
    print(f"❌ Error sending email: {str(e)}")
    sys.exit(1)

print("\n" + "=" * 60)
