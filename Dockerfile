# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /app/src

# Install system dependencies
RUN apt-get update && apt-get install -y \
    pkg-config \
    libhdf5-dev \
    build-essential \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

# Copy the kaggle.json file into the container
COPY kaggle.json /root/.kaggle/kaggle.json

# Set permissions for the kaggle.json file
RUN chmod 600 /root/.kaggle/kaggle.json

# Copy the rest of the application code into the container at /app
COPY . /app

# Expose port 8888 to be able to access Jupyter Notebook
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
