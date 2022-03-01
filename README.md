# fikrat

Fikrat online download eletron and audio books
___

# pip

```
python3 -m venv venv
source ./venv/bin/activate

python -m pip install -U pip
pip install -r requirements.txt
```

___

# Systemd service [fikrat.service]

```
[Unit]
Description=Systemd service daemon for fikrat.org
Before=nginx.service
After=network.target

[Service]
User=major
Group=major
WorkingDirectory=/home/major/fikrat
ExecStart=/home/major/fikrat/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/major/fikrat/gunicorn.sock project.wsgi:application
Restart=always
SyslogIdentifier=gunicorn

[Install]
WantedBy=multi-user.target
```

___

# Nginx [fikrat_backend]

```
server {
    listen 80;
    server_name fikrat.org www.fikrat.org;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static {
        alias /home/major/fikrat/static;
    }
    
    location /media  {
        alias /home/major/fikrat/media;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/major/fikrat/gunicorn.sock;
    }
}
```