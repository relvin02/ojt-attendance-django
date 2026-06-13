from django.db import models
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.utils import timezone
from datetime import timedelta

class Program(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'program'
        verbose_name_plural = 'Programs'

    def __str__(self):
        return self.name


class Batch(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'batch'
        verbose_name_plural = 'Batches'

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile', null=True, blank=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='students')
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_students')
    id_number = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True, help_text="Name of the emergency contact person")
    emergency_contact_number = models.CharField(max_length=20, blank=True, null=True, help_text="Emergency contact phone number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='student_profiles/', blank=True, null=True)
    face_encoding = models.JSONField(null=True, blank=True)  # Stores face encoding as JSON
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'student'
        verbose_name_plural = 'Students'
        ordering = ['id_number']

    def __str__(self):
        return f"{self.id_number} - {self.first_name} {self.last_name}"


class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('late', 'Late'),
        ('undertime', 'Undertime'),
        ('absent', 'Absent'),
        ('excused', 'Excused'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='attendances')
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    check_in_latitude = models.FloatField(null=True, blank=True)
    check_in_longitude = models.FloatField(null=True, blank=True)
    check_out_latitude = models.FloatField(null=True, blank=True)
    check_out_longitude = models.FloatField(null=True, blank=True)
    check_in_image = models.ImageField(upload_to='check_in_images/', null=True, blank=True)
    check_out_image = models.ImageField(upload_to='check_out_images/', null=True, blank=True)
    liveness_verified = models.BooleanField(default=False)
    was_late = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present')
    remarks = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'attendance'
        verbose_name_plural = 'Attendances'
        ordering = ['-date', '-check_in_time']
        unique_together = ['student', 'company', 'date']

    def __str__(self):
        return f"{self.student} - {self.date} ({self.status})"

    def get_hours_worked(self):
        """Calculate hours worked based on check-in and check-out times."""
        if self.check_in_time and self.check_out_time:
            start = self.check_in_time
            end = self.check_out_time

            # Total worked seconds
            total_seconds = (end - start).total_seconds()

            # Subtract lunch overlap (12:00 - 13:00) if it intersects the worked period
            lunch_start = start.replace(hour=12, minute=0, second=0, microsecond=0)
            lunch_end = start.replace(hour=13, minute=0, second=0, microsecond=0)

            # If the lunch period spills across days (shouldn't in normal use), adjust to same day
            if lunch_end < lunch_start:
                lunch_end = lunch_start + timedelta(hours=1)

            # Calculate overlap between [start, end] and [lunch_start, lunch_end]
            overlap_start = max(start, lunch_start)
            overlap_end = min(end, lunch_end)
            overlap = 0
            if overlap_end > overlap_start:
                overlap = (overlap_end - overlap_start).total_seconds()

            worked_seconds = max(0, total_seconds - overlap)
            return worked_seconds / 3600


class StudentDocument(models.Model):
    """Files uploaded by students for dean review (monthly reports, etc.)."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=255, help_text="Brief description of the file")
    file = models.FileField(upload_to='student_documents/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student_document'
        verbose_name = 'Student Document'
        verbose_name_plural = 'Student Documents'
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.student} - {self.title} ({self.uploaded_at.date()})"


class DailySchedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='schedules')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='schedules')
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    check_in_time = models.TimeField()
    check_out_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'daily_schedule'
        verbose_name_plural = 'Daily Schedules'
        unique_together = ['batch', 'company', 'day_of_week']

    def __str__(self):
        return f"{self.batch} - {self.company} ({self.day_of_week})"


class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor_profile')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='supervisors')
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='supervisor_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'supervisor'
        verbose_name_plural = 'Supervisors'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.company.name}"


class AcademicStaff(models.Model):
    ROLE_CHOICES = [
        ('dean', 'Dean'),
        ('head', 'Head'),
        ('coordinator', 'Coordinator'),
        ('staff', 'Staff'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='academic_staff')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='academic_staff', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='academic_staff_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'academic_staff'
        verbose_name_plural = 'Academic Staff'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.get_role_display()}"


class LeaveRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    proof_image = models.ImageField(upload_to='leave_proofs/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    approval_date = models.DateTimeField(null=True, blank=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'leave_request'
        verbose_name_plural = 'Leave Requests'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student} - {self.start_date} to {self.end_date}"
