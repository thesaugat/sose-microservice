# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

RUN echo "from courseservice.app.models import Course; Course.objects.create(title= 'Database Management System',code= 'CSI282', credit=6)" | python manage.py shell
RUN echo "from courseservice.app.models import Course; Course.objects.create(title= 'Strategic Network Design',code= 'CSI285', credit=6)" | python manage.py shell
RUN echo "from courseservice.app.models import Course; Course.objects.create(title= 'Service Oriented Software Engineering',code= 'CSI289',credit= 6)" | python manage.py shell



# Expose port 8000 to the outside world
EXPOSE 8002

# Define the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8002"]
