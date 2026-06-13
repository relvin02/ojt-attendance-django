#!/bin/bash
# PythonAnywhere Automated Deployment Script
# This script automates the deployment of the OJT Attendance Django project
# Run this script in the PythonAnywhere Bash console after cloning the repository

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}OJT Attendance Django - PythonAnywhere Deployment${NC}"
echo -e "${GREEN}========================================${NC}"

# Check if the project directory exists
if [ ! -d "$HOME/mysite" ]; then
    echo -e "${RED}Error: Project not found at ~/mysite${NC}"
    echo "Please run: git clone https://github.com/relvin02/ojt-attendance-django.git mysite"
    exit 1
fi

cd ~/mysite

# Step 1: Create Virtual Environment
echo -e "${YELLOW}[1/8] Creating virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3.11 -m venv venv
    echo -e "${GREEN}✓ Virtual environment created${NC}"
else
    echo -e "${GREEN}✓ Virtual environment already exists${NC}"
fi

# Step 2: Activate virtual environment and upgrade pip
echo -e "${YELLOW}[2/8] Activating virtual environment and upgrading pip...${NC}"
source venv/bin/activate
pip install --upgrade pip
echo -e "${GREEN}✓ Pip upgraded${NC}"

# Step 3: Install dependencies
echo -e "${YELLOW}[3/8] Installing project dependencies...${NC}"
pip install -r requirements.txt
echo -e "${GREEN}✓ Dependencies installed${NC}"

# Step 4: Create .env file
echo -e "${YELLOW}[4/8] Setting up environment variables...${NC}"
if [ ! -f ".env" ]; then
    echo "Creating .env file. Please edit it with your SECRET_KEY!"
    cp .env.example .env
    # Generate a new SECRET_KEY
    python3 -c "import secrets; print(f'SECRET_KEY={secrets.token_urlsafe(50)}')" >> .env.tmp
    echo "DEBUG=False" >> .env.tmp
    echo "ALLOWED_HOSTS=rgcoder.pythonanywhere.com,www.rgcoder.pythonanywhere.com,localhost,127.0.0.1" >> .env.tmp
    mv .env.tmp .env
    echo -e "${GREEN}✓ .env file created${NC}"
else
    echo -e "${GREEN}✓ .env file already exists${NC}"
fi

# Step 5: Navigate to Django project directory
cd ojt_project

# Step 6: Run migrations
echo -e "${YELLOW}[5/8] Running database migrations...${NC}"
python manage.py migrate
echo -e "${GREEN}✓ Migrations completed${NC}"

# Step 7: Collect static files
echo -e "${YELLOW}[6/8] Collecting static files...${NC}"
python manage.py collectstatic --noinput
echo -e "${GREEN}✓ Static files collected${NC}"

# Step 8: Summary
echo -e "${YELLOW}[7/8] Deployment preparation complete!${NC}"

# Step 9: Instructions
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}Next Steps:${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "1. Go to: https://www.pythonanywhere.com/user/rgcoder/webapps/"
echo -e "2. Click on your web app (rgcoder.pythonanywhere.com)"
echo -e "3. In the 'Code' section, set:"
echo -e "   - Source code: /home/rgcoder/mysite"
echo -e "   - Virtual env: /home/rgcoder/mysite/venv"
echo -e "4. In the 'WSGI configuration file' section, paste the content from pythonanywhere_wsgi.py"
echo -e "5. Click 'Reload' button"
echo -e ""
echo -e "${YELLOW}To create a superuser (optional):${NC}"
echo -e "python manage.py createsuperuser"
echo -e ""
echo -e "${GREEN}Your app should now be live at:${NC}"
echo -e "https://rgcoder.pythonanywhere.com"
echo -e "${GREEN}========================================${NC}"
