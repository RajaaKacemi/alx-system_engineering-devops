#!/usr/bin/env bash
# This script diagnoses and fixes Nginx to listen on port 80

# Step 1: Check Nginx configuration files
nginx_config="/etc/nginx/nginx.conf"
if [ ! -f "$nginx_config" ]; then
    echo "Nginx configuration file not found at: $nginx_config"
    exit 1
fi

# Step 2: Check if Nginx process is running
if ! pgrep -x "nginx" >/dev/null; then
    echo "Nginx is not running. Starting Nginx..."
    sudo service nginx start
fi

# Step 3: Check if Nginx is listening on port 80
if sudo ss -tln | grep -q ":80 "; then
    echo "Nginx is already listening on port 80"
else
    # Step 4: If not listening, adjust configuration and restart Nginx
    echo "Nginx is not listening on port 80. Adjusting configuration..."
    sudo sed -i 's/^ *listen *80;/listen 80;/g' "$nginx_config"
    sudo service nginx restart
fi

echo "Nginx configured to listen on port 80"
