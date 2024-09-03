FROM rockylinux:8

RUN dnf -y update && \
    dnf -y install python39 python39-pip python39-devel gcc && \
    dnf clean all

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --upgrade pip && pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
