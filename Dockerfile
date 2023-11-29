FROM python:3.8-alpine as builder
# RUN adduser -D worker -u 1000

RUN apk add --no-cache git build-base

# Get the python dependencies
COPY requirements.txt /app/
RUN python -m pip install --no-cache-dir -r /app/requirements.txt

# Copy the app itself
COPY backend /app/src
WORKDIR /app/src

# Get the frontend component staticfiles
COPY frontend/public/build /app/frontend/public/build

# Catalog the staticfiles. This is needed in production, but in the dev
#  environment the svelte staticfiles will be drawn from
#  the svelte/public/build directory
RUN python manage.py collectstatic --noinput

# Delete the original staticfiles
RUN rm -rf /app/frontend

# get the runtime instructions
COPY entrypoint.sh /app
RUN chmod +x /app/entrypoint.sh

# set the runtime user
# USER worker
EXPOSE 8080
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
