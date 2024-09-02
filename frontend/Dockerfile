# Use the Rocky Linux base image
FROM rockylinux:8

# Install dependencies required for Python
RUN yum -y update && \
    yum -y install python39 python39-devel gcc && \
    yum clean all

# Set up a symlink to use python3 as python
RUN ln -s /usr/bin/python3 /usr/bin/python

# Install pip for Python
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire frontend application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]
