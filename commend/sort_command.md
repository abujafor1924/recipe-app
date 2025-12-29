Here's a cleaned and organized list of useful commands for a backend developer, grouped by functionality:

## **Environment & Virtual Environment**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
. venv/bin/activate

# Deactivate virtual environment
deactivate

# Install requirements
pip install -r requirements.txt
pip freeze > requirements.txt
```

## **Django Development**
```bash
# Run development server
python3 manage.py runserver
python3 manage.py runserver 8800
python3 manage.py runserver 0.0.0.0:5002 --noreload

# Database migrations
python3 manage.py makemigrations
python3 manage.py makemigrations app_name  # Specific app
python3 manage.py migrate

# Create superuser
python3 manage.py createsuperuser

# Collect static files
python3 manage.py collectstatic

# Django checks
python3 manage.py check
python3 manage.py check --deploy
```

## **Git Commands**
```bash
# Basic git workflow
git add .
git commit -m "commit message"
git push
git push origin branch_name

# Branch management
git branch
git checkout -b feature_branch
git checkout main
git branch -M main

# Remote repository management
git remote rename origin old-origin
git remote add origin git@gitlab.example.com:user/repo.git
git push --set-upstream origin --all
git remote -v

# Clone repositories
git clone git@github.com:user/repo.git
git clone https://github.com/user/repo.git
```

## **Package Management**
```bash
# Install Python packages
pip install package_name
pip install django requests python-decouple djangorestframework
pip install Pillow django-cors-headers pyngrok django-debug-toolbar

# Upgrade pip
pip install --upgrade pip
```

## **Database (PostgreSQL)**
```bash
# PostgreSQL service management
sudo systemctl status postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql

# PostgreSQL CLI
sudo -u postgres psql
CREATE DATABASE database_name;
```

## **Docker Commands**
```bash
# Docker Compose
sudo docker-compose up
sudo docker-compose up --build
sudo docker-compose down

# Docker container management
docker ps
sudo docker ps -a
sudo docker rm -f container_name
sudo docker inspect --format '{{.State.Pid}}' container_name

# Docker system
sudo systemctl restart docker
sudo systemctl status docker
```

## **System & Maintenance**
```bash
# Update system packages
sudo apt update
sudo apt install package_name -y

# Clean system cache
sudo rm -rf ~/.cache/*
sudo apt clean

# Check disk usage
sudo du -h /var/log | sort -h
sudo du -sh /var/log/*.gz
journalctl --disk-usage

# Clean logs
sudo rm -f /var/log/*.gz
sudo journalctl --vacuum-size=20000M
```

## **SSH & Security**
```bash
# Generate SSH keys
ssh-keygen -t ed25519 -C "email@example.com"
ssh-keygen -t rsa -b 4096 -C "email@example.com"

# View SSH keys
cat ~/.ssh/id_rsa.pub
```

## **Process Management**
```bash
# Kill process by PID
sudo kill -9 PID_number

# Check running services
sudo systemctl status service_name
```

## **API Testing**
```bash
# Curl commands for API testing
curl https://api.example.com/endpoint
curl https://api.example.com/endpoint?param=value

# Postman (if installed as snap)
snap run postman
sudo snap install postman
sudo snap remove postman
```

## **Python Script Execution**
```bash
# Run Python scripts
python script.py
python3 script.py
/home/user/venv/bin/python /path/to/script.py
```

## **Project Structure**
```bash
# Navigate directories
cd /path/to/project
cd ..
ls
ls -la

# Create directories
mkdir -p ~/tmp
mkdir directory_name

# Start new Django project
django-admin startproject project_name
python3 manage.py startapp app_name
```

## **Miscellaneous Tools**
```bash
# Ngrok for tunneling
ngrok http 8800
ngrok config add-authtoken your_token

# Clear terminal
clear

# View command history
history

# Check Python version
python --version
python3 --version
```

## **Debugging & Monitoring**
```bash
# Check system logs
sudo journalctl -f
sudo tail -f /var/log/syslog

# Memory and process monitoring
top
htop
free -h
```

This organized list covers essential commands for backend development including Django, Git, Docker, database management, and system operations.