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

RUN echo "from libraryservice.app.models import Books; Books.objects.create(author='Aditya Chapagain', book_name= 'Database Management System')" | python manage.py shell
RUN echo "from libraryservice.app.models import Books; Books.objects.create(author='Sham Rodes', book_name= 'Strategic Network Design')" | python manage.py shell
RUN echo "from libraryservice.app.models import Books; Books.objects.create(author='Jhon Mann', book_name= 'Service Oriented Software Engineering')" | python manage.py shell


# Expose port 8000 to the outside world
EXPOSE 8001

# Define the command to run on container start
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
