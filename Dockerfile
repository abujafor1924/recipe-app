# Use official Python Alpine image
FROM python:3.11-alpine
LABEL maintainer="abujafor"

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED 1

# Copy requirements
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Copy application code
COPY ./app /app
WORKDIR /app

# Expose port
EXPOSE 8000

# Argument to control dev tools installation
ARG DEV=false

# Install Python dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip setuptools wheel && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ "$DEV" = "true" ] ; then /py/bin/pip install -r /tmp/requirements.dev.txt ; fi && \
    rm -rf /tmp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    chown -R django-user:django-user /app

# Add virtualenv bin to PATH
ENV PATH="/py/bin:$PATH"

# Use non-root user
USER django-user
