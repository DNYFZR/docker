# Dockerfile

# Set up slim install of Python
FROM python:3.9-slim

# Set Docker working dir 
WORKDIR /app

# Copy source folder to Docker
COPY app/** /app/

# Install dependencies
RUN pip3 install --upgrade pip -r req.txt

# Execute container 
CMD [ "python", "./main.py" ]