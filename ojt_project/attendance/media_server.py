"""Media file serving for production environments."""
import os
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings


def serve_media(request, filepath):
    """Serve media files safely from the media directory."""
    # Security: Prevent directory traversal attacks
    filepath = filepath.lstrip('/')
    if '..' in filepath or filepath.startswith('/'):
        return HttpResponseForbidden("Access denied")
    
    full_path = os.path.join(settings.MEDIA_ROOT, filepath)
    
    # Ensure the file is within MEDIA_ROOT
    if not os.path.abspath(full_path).startswith(os.path.abspath(settings.MEDIA_ROOT)):
        return HttpResponseForbidden("Access denied")
    
    # Check if file exists
    if not os.path.exists(full_path):
        return HttpResponse("File not found", status=404)
    
    # Serve the file
    try:
        with open(full_path, 'rb') as f:
            content = f.read()
            
            # Determine content type based on file extension
            ext = os.path.splitext(full_path)[1].lower()
            content_types = {
                '.jpg': 'image/jpeg',
                '.jpeg': 'image/jpeg',
                '.png': 'image/png',
                '.gif': 'image/gif',
                '.pdf': 'application/pdf',
                '.txt': 'text/plain',
            }
            content_type = content_types.get(ext, 'application/octet-stream')
            
            response = HttpResponse(content, content_type=content_type)
            response['Content-Disposition'] = f'inline; filename="{os.path.basename(full_path)}"'
            return response
    except IOError:
        return HttpResponse("Error reading file", status=500)
