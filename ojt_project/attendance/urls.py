from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .media_server import serve_media

urlpatterns = [
    # Home
    path('', views.index, name='index'),
    
    # Media serving (for production environments)
    path('media/<path:filepath>', serve_media, name='serve_media'),
    
    # Authentication
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Student URLs
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('student/check-in-out/', views.check_in_out, name='check_in_out'),
    path('student/attendance-history/', views.attendance_history, name='attendance_history'),
    path('student/request-leave/', views.request_leave, name='request_leave'),
    path('student/leave-history/', views.leave_history, name='leave_history'),
    
    # Supervisor URLs
    path('supervisor/dashboard/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('supervisor/manage-attendance/', views.manage_attendance, name='manage_attendance'),
    path('supervisor/approve-leave/', views.approve_leave, name='approve_leave'),
    
    # Admin URLs
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/students/', views.manage_students, name='manage_students'),
    path('admin/companies/', views.manage_companies, name='manage_companies'),
    path('admin/programs/', views.manage_programs, name='manage_programs'),
    path('admin/batches/', views.manage_batches, name='manage_batches'),
    path('admin/reports/', views.reports, name='reports'),
    
    # Academic Staff URLs (Dean/Head)
    path('academic/dashboard/', views.academic_staff_dashboard, name='academic_staff_dashboard'),
    path('academic/students/', views.academic_staff_manage_students, name='academic_staff_manage_students'),
    path('academic/students/add/', views.academic_staff_add_student, name='academic_staff_add_student'),
    path('academic/students/import/', views.academic_staff_import_students, name='academic_staff_import_students'),
    path('academic/students/<int:student_id>/edit/', views.academic_staff_edit_student, name='academic_staff_edit_student'),
    path('academic/students/<int:student_id>/delete/', views.academic_staff_delete_student, name='academic_staff_delete_student'),
    path('academic/attendance/', views.academic_staff_manage_attendance, name='academic_staff_manage_attendance'),
    path('academic/reports/', views.academic_staff_reports, name='academic_staff_reports'),
    path('academic/print-dtr/', views.academic_staff_print_dtr, name='academic_staff_print_dtr'),
    # Document upload/view
    path('student/documents/', views.student_documents, name='student_documents'),
    path('academic/documents/', views.academic_student_documents, name='academic_student_documents'),
]
