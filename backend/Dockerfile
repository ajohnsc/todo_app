# Use the Rocky Linux base image
FROM rockylinux:8

# Install dependencies required for Python, compilation, and MySQL client
RUN yum -y update && \
    yum -y install python39 python39-devel gcc mysql-devel && \
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

# Copy the entire backend application code
COPY . .

# Expose the FastAPI port
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
