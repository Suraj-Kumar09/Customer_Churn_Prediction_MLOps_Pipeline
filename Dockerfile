FROM python:3.10-slim-bookworm

WORKDIR /app

# System dependencies (AWS CLI ke liye)
RUN apt update -y && apt install -y awscli

# Pura code copy karein (taaki setup.py aur requirements.txt dono mil jayein)
COPY . .

# Dependencies install karein
RUN pip install --no-cache-dir -r requirements.txt

# Port
EXPOSE 5000

# Run command
CMD ["python", "app.py"]