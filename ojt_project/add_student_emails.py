#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ojt_project.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from attendance.models import Student

# Get first 5 students to show their current emails
students = Student.objects.all()[:5]
print("Current students in database:")
for s in students:
    print(f"  ID: {s.id_number}, Name: {s.first_name} {s.last_name}, Email: {s.email}")

# Update students to have test emails if they don't have emails
updated_count = 0
for i, student in enumerate(Student.objects.all()):
    if not student.email or student.email.strip() == '':
        test_email = f"student{i+1}@test.com"
        student.email = test_email
        student.save()
        print(f"Updated {student.first_name} with email: {test_email}")
        updated_count += 1

print(f"\nTotal students updated: {updated_count}")
print("All students now have emails registered!")
