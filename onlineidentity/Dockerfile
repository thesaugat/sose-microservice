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

RUN echo "from onlineidentity.app.models import User; User.objects.create_superuser('admin@uow.com', 'SOE Admin', 'Test123')" | python manage.py shell
RUN echo "from onlineidentity.app.models import User, StudentProfile; u=User.objects.create_user('student@uow.com',  'Stud123', name='Test Student') ; StudentProfile.objects.create(user=u, year=2023) "  | python manage.py shell


# Expose port 8000 to the outside world
EXPOSE 8000

# Define the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
