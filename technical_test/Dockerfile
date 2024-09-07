# 1. Specify the base image
FROM python:3.12.2

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the current directory contents into the container
COPY . /app

# 4. Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Install necessary dependencies for Chrome
RUN apt-get update && apt-get install -y \
    bash \
    curl \
    chromium \
    fonts-liberation \
    libappindicator3-1 \
    libnss3 \
    libx11-6 \
    libxrender1 \
    libxi6 \
    libgconf-2-4 \
    udev \
    dbus-x11 \
    && rm -rf /var/lib/apt/lists/*

# Install specific ChromeDriver version
RUN CHROME_DRIVER_VERSION=128.0.6613.119 && \
    curl -sSLO "https://storage.googleapis.com/chrome-for-testing-public/128.0.6613.119/linux64/chromedriver-linux64.zip" && \
    unzip chromedriver-linux64.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver-linux64 && \
    rm chromedriver-linux64.zip

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/local/bin/chromedriver \
    DISPLAY=:99

# 6. Set environment variable PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app"

# 7. Specify the command to run your app
CMD ["pytest", "-m", "positive_login", "./Tests"]
