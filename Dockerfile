# Use the official Python 3.10 slim-buster base image
FROM python:3.10-slim-buster

# Disable cache for pip and set default environment variables
ENV PIP_NO_CACHE_DIR=1 \
    PATH="/home/bot/bin:$PATH"

# Update apt sources for compatibility
RUN sed -i.bak 's/us-west-2\.ec2\.//' /etc/apt/sources.list

# Install system dependencies
RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
    bash \
    bzip2 \
    curl \
    figlet \
    git \
    util-linux \
    libffi-dev \
    libjpeg-dev \
    libwebp-dev \
    musl-dev \
    neofetch \
    php-pgsql \
    postgresql \
    postgresql-client \
    libpq-dev \
    libcurl4-openssl-dev \
    libxml2-dev \
    libxslt1-dev \
    python3-lxml \
    python3-pip \
    python3-requests \
    python3-sqlalchemy \
    python3-tz \
    python3-aiohttp \
    openssl \
    jq \
    wget \
    python3-dev \
    libreadline-dev \
    libyaml-dev \
    gcc \
    sqlite3 \
    libsqlite3-dev \
    zlib1g \
    ffmpeg \
    libssl-dev \
    libopus0 \
    libopus-dev \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Upgrade pip and setuptools
RUN pip3 install --upgrade pip setuptools

# Set working directory
WORKDIR /root/FallenRobot

# Copy Python requirements
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip3 install -U -r requirements.txt

# Copy configuration files and project source
COPY ./FallenRobot/config.py ./FallenRobot/config.py* /root/FallenRobot/FallenRobot/
COPY . .

# Start the bot
CMD ["python3", "-m", "FallenRobot"]
