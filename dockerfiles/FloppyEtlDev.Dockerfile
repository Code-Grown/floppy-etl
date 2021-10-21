FROM python:3.9-slim-bullseye

WORKDIR /app

RUN apt update && apt upgrade -y && apt install -y \
  sudo curl nmap gcc git bash nano tzdata htop net-tools iputils-ping cron systemd rcconf build-essential procps
  #\ mongo-client mysql-client

# Usefull aliases
RUN echo "alias ll='ls -lah'" >> ~/.bashrc

# Install proyect dependencies
ADD ./app/requirements.txt /app
ADD ./app/application.py /app
RUN pip install --upgrade pip && pip install -r requirements.txt 

# Configuring executable global app
RUN chmod +x /app/application.py
RUN ln -s /app/application.py /usr/local/bin/etl

# Adding logs folder and files
RUN mkdir -p /app/storage/logs
RUN touch /app/storage/logs/app.log
RUN touch /app/storage/logs/critical.log
RUN touch /app/storage/logs/danger.log
RUN touch /app/storage/logs/debug.log
RUN touch /app/storage/logs/info.log
RUN touch /app/storage/logs/success.log
RUN touch /app/storage/logs/warning.log
# Adding dumped folders
RUN mkdir -p /app/storage/dumped

# Sending app.log to STDOUT
RUN ln -sf /proc/1/fd/1 /app/storage/logs/app.log

# Adding configured crones
COPY ./dockerfiles/conf.d/etl /etc/cron.d/etl

# Runing added crones
RUN crontab /etc/cron.d/etl

# Adding Entry Point
COPY ./dockerfiles/bin.d/start-cron /usr/local/bin/start-cron
RUN chmod +x /usr/local/bin/start-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Entry point
CMD ["start-cron"]