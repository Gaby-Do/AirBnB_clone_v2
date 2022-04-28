#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
if ! [ -e /var/run/nginx.pid ]; then
	sudo apt update
	sudo apt -y install nginx
	sudo service nginx restart
fi
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo -e "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sudo sed -i '/error_page 404 \/404.html;/ a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}' /etc/nginx/sites-available/default
sudo service nginx restart
