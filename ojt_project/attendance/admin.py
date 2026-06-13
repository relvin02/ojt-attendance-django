from django.contrib import admin
from .models import (
    Program, Batch, Student, Company, Attendance,
    DailySchedule, Supervisor, LeaveRequest, AcademicStaff,
    StudentDocument
)


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ['name', 'program', 'start_date', 'end_date']
    list_filter = ['program', 'start_date']
    search_fields = ['name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id_number', 'first_name', 'last_name', 'email', 'batch', 'is_active']
    list_filter = ['batch', 'is_active', 'gender']
    search_fields = ['id_number', 'first_name', 'last_name', 'email']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'company', 'date', 'check_in_time', 'check_out_time', 'status']
    list_filter = ['status', 'date', 'company']
    search_fields = ['student__id_number', 'student__first_name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(DailySchedule)
class DailyScheduleAdmin(admin.ModelAdmin):
    list_display = ['batch', 'company', 'day_of_week', 'check_in_time', 'check_out_time']
    list_filter = ['day_of_week', 'batch']
    search_fields = ['batch__name', 'company__name']


@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ['user', 'company', 'position']
    list_filter = ['company']
    search_fields = ['user__username', 'user__email', 'company__name']


@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ['student', 'start_date', 'end_date', 'status', 'created_at']
    list_filter = ['status', 'start_date']
    search_fields = ['student__id_number', 'student__first_name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AcademicStaff)
class AcademicStaffAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'program']
    list_filter = ['role', 'program']
    search_fields = ['user__username', 'user__email', 'program__name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(StudentDocument)
class StudentDocumentAdmin(admin.ModelAdmin):
    list_display = ['student', 'title', 'uploaded_at']
    list_filter = ['uploaded_at']
    search_fields = ['student__id_number', 'title']
    readonly_fields = ['uploaded_at']
