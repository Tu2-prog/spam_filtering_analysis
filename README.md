# Spam Mail Filtering

This is a personal project to evaluate different machine learning algorithms in their ability to classify if a provided email is a spam mail or not.

### How to install it
To build this container in particular, run this command:

```console
$ docker build -t your_docker_image_name:latest .
```

To execute this contianer, run this command:

```console
$ docker run -p port:port -t your_docker_image_name:latest
```

The other microservices can be built and executed the same way however some times environment variables are needed.

For this one needs to add this flag for building the container with ENV variables:

```console
$ docker build --build-arg ARG=VALUE ....
```

While running the environment variables dependent containers one needs this flag:

```console
$ docker run -e ARG=VALUE ...
```
