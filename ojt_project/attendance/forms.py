from django import forms
from django.contrib.auth.models import User
from .models import Student, Attendance, LeaveRequest, Company, Program, Batch, StudentDocument

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id_number', 'first_name', 'last_name', 'email', 'phone', 'emergency_contact_name', 'emergency_contact_number',
                  'gender', 'date_of_birth', 'address', 'company', 'profile_image']
        widgets = {
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class StudentProfileForm(forms.ModelForm):
    """Student self-service profile form (company assignment is managed by staff)."""

    class Meta:
        model = Student
        fields = [
            'id_number', 'first_name', 'last_name', 'email', 'phone',
            'emergency_contact_name', 'emergency_contact_number',
            'gender', 'date_of_birth', 'address', 'profile_image'
        ]
        widgets = {
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['status', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['start_date', 'end_date', 'reason', 'proof_image']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'rows': 4}),
            'proof_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class LeaveApprovalForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['status', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone', 'email', 'website', 'latitude', 'longitude']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'latitude': forms.NumberInput(attrs={'step': '0.0001'}),
            'longitude': forms.NumberInput(attrs={'step': '0.0001'}),
        }


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['program', 'name', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=False)


class ImportStudentsForm(forms.Form):
    file = forms.FileField(required=True, help_text='Upload .xlsx or .csv file containing student data')


class StudentDocumentForm(forms.ModelForm):
    class Meta:
        model = StudentDocument
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }