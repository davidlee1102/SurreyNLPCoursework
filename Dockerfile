# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENVIRONMENT production

# Set the working directory to the directory containing manage.py
WORKDIR /SurreyCourseworkNLPProject

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the container
COPY . .

# Collect the static files
# RUN python manage.py collectstatic --noinput

# Expose the port that the app will run on
EXPOSE 8000

# Run the command to start the app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.wsgi"]

#Test