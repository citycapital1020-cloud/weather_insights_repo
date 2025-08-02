# Use the official Airflow image as the base
FROM apache/airflow:2.10.5

# Switch to root user to install system dependencies
USER root

# Create necessary directories and set permissions first
RUN mkdir -p /var/lib/apt/lists/partial && \
    chmod -R 755 /var/lib/apt/lists && \
    chown _apt:root /var/lib/apt/lists/partial

# Create data directories and set permissions
RUN mkdir -p /opt/airflow/weather_data/{raw,archive}
RUN chmod -R 775 /opt/airflow/weather_data 

# Update and install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        procps \
        openjdk-17-jdk-headless \
        apt-utils && \
    apt-get autoremove -yqq --purge && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set Java environment
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Switch back to airflow user
USER airflow

# Install dependencies separately for debugging
COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
RUN pip install --no-cache-dir jupyter
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir urllib3
RUN python -m ipykernel install --user --name python3 --display-name "Python 3"

# Install psycopg2-binary
RUN pip install psycopg2-binary

# Optional: Install Pillow to address the PIL warning from logs
RUN pip install Pillow