#### REST API ####

# Set the baseImage 
FROM python:3.9-slim-buster

# Copy files from source to dest image path
COPY requirements.txt .

# Execute any commands on top of the current image 
RUN python -m pip install --upgrade pip -r requirements.txt

# Copy files from source to dest image path
COPY . .

# The port we will use at runtime
EXPOSE 80

# Provide defaults for an executing container
CMD [ "flask", "run", "--host=0.0.0.0", "--port=80" ]