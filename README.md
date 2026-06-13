# OJT Attendance System - Django

A comprehensive OJT (On-the-Job Training) Attendance System built with Python Django, featuring face recognition and GPS tracking.

## Features

### Student Module
- Check-in/Check-out with Face Recognition
- GPS location verification
- Attendance history and reports
- Leave request submission
- Real-time attendance status

### Supervisor Module
- Manage student attendance
- Approve/reject leave requests
- View attendance reports by date range
- Monitor student attendance statistics

### Admin Module
- Student management
- Company management
- Program and batch management
- Comprehensive attendance reports
- System-wide analytics

### Core Features
- **Face Recognition**: Secure attendance verification using facial recognition
- **GPS Tracking**: Location-based attendance with coordinate verification
- **Leave Management**: Student leave request system with approval workflow
- **Attendance Reports**: Detailed reports and analytics
- **Role-based Access**: Different interfaces for students, supervisors, and admins

## System Requirements

- Python 3.8+
- MySQL Database
- Webcam for face recognition

## Installation

### 1. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

Create a MySQL database:
```sql
CREATE DATABASE ojt_attendance_db;
```

### 4. Configure environment variables

Edit `.env` file with your database credentials:
```
DB_NAME=ojt_attendance_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
```

### 5. Run migrations

```bash
cd ojt_project
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Project Structure

```
ojt_attendance_django/
├── ojt_project/                 # Main project directory
│   ├── settings.py             # Django settings
│   ├── urls.py                 # URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── __init__.py
├── attendance/                 # Main app
│   ├── models.py              # Database models
│   ├── views.py               # View functions
│   ├── forms.py               # Django forms
│   ├── urls.py                # App URLs
│   ├── admin.py               # Admin configuration
│   ├── apps.py                # App configuration
│   ├── templates/
│   │   └── attendance/        # HTML templates
│   ├── static/
│   │   ├── css/               # CSS files
│   │   └── js/                # JavaScript files
│   └── migrations/            # Database migrations
├── media/                      # User uploaded files
├── manage.py                   # Django management script
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables
└── README.md                   # This file
```

## Database Models

### Program
- name
- description
- created_at, updated_at

### Batch
- program (FK)
- name
- start_date, end_date

### Student
- batch (FK)
- id_number, first_name, last_name
- email, phone
- gender, date_of_birth
- address, profile_image
- face_encoding (for face recognition)
- is_active

### Company
- name, address, phone, email
- website, latitude, longitude

### Attendance
- student (FK), company (FK)
- check_in_time, check_out_time
- check_in_latitude, check_in_longitude
- check_out_latitude, check_out_longitude
- check_in_image, check_out_image
- status (present, late, absent, excused)
- date, created_at, updated_at

### DailySchedule
- batch (FK), company (FK)
- day_of_week
- check_in_time, check_out_time

### Supervisor
- user (FK), company (FK)
- phone, position, image

### LeaveRequest
- student (FK)
- start_date, end_date
- reason, status
- approved_by (FK), approval_date

## Usage

### For Students
1. Login with your credentials
2. Go to "Check In/Out" page
3. Select your company
4. Allow camera access for face recognition
5. Click "Check In" when arriving
6. Click "Check Out" when leaving
7. View your attendance history and request leaves

### For Supervisors
1. Login with supervisor credentials
2. View student attendance for your company
3. Manage attendance records
4. Approve or reject student leave requests

### For Admins
1. Login with admin credentials
2. Access Django admin panel at `/admin/`
3. Manage students, companies, programs, and batches
4. View comprehensive attendance reports

## Face Recognition Setup

The system uses OpenCV and face_recognition library for facial recognition. For the first-time setup:

1. Upload a clear profile image of the student
2. The system will extract and store the face encoding
3. On check-in, the system compares the captured face with the stored encoding

## GPS Tracking

Students must enable location services when checking in/out. The system:
- Records GPS coordinates during check-in/out
- Verifies location is within allowed radius (default: 500m from company)
- Stores location data for attendance verification

## API Endpoints

The system provides REST API endpoints for:
- Student attendance submission
- Attendance records retrieval
- Leave requests management

Access API documentation at `/api/docs` (if DRF documentation is enabled)

## Security Considerations

- Passwords are hashed using Django's default authentication
- CSRF protection enabled
- SQL injection prevention through ORM
- XSS protection through template escaping
- Enable HTTPS in production
- Use strong SECRET_KEY in production
- Set DEBUG=False in production

## Maintenance

### Database Backup
```bash
mysqldump -u root -p ojt_attendance_db > backup.sql
```

### Database Restore
```bash
mysql -u root -p ojt_attendance_db < backup.sql
```

## Troubleshooting

### Face Recognition Not Working
- Ensure webcam is connected and permissions are granted
- Check browser console for errors
- Verify face-recognition library is installed

### Database Connection Error
- Verify MySQL is running
- Check database credentials in .env
- Ensure database exists

### Port Already in Use
```bash
python manage.py runserver 8001  # Use different port
```

## Future Enhancements

- SMS/Email notifications for attendance
- Mobile app integration
- Real-time attendance dashboard
- Advanced analytics and reporting
- Multi-language support
- QR code attendance verification
- Biometric integration

## Support

For issues or questions, contact your system administrator or check the application logs.

## License

Copyright © 2026 OJT Attendance System

---

**Created**: February 23, 2026
**Version**: 1.0.0
