# AirBnB Clone Deployment Tasks

## Task 0: Set up development with Python

### Requirements:
- Ensure that task #3 of your SSH project is completed for web-01.
- Install the net-tools package on your server: `sudo apt install -y net-tools`.
- Git clone your AirBnB_clone_v2 on your web-01 server.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
- Your Flask application object must be named `app`.

## Task 1: Set up production with Gunicorn

### Requirements:
- Install Gunicorn and any other libraries required by your application.
- The Flask application object should be called `app`.
- Serve the same content from the same route as in Task 0.
- Bind a Gunicorn instance to localhost listening on port 5000 with your application object as the entry point.

## Task 2: Serve a page with Nginx

### Requirements:
- Configure Nginx to serve your page from the route /airbnb-onepage/.
- Nginx must serve this page both locally and on its public IP on port 80.
- Nginx should proxy requests to the process listening on port 5000.

## Task 3: Add a route with query parameters

### Requirements:
- Configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.
- Nginx must serve this page both locally and on its public IP on port 80.

## Task 4: Serve AirBnB Clone v3 - RESTful API

### Requirements:
- Git clone your AirBnB_clone_v3.
- Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002.
- Nginx must serve this page both locally and on its public IP on port 80.
- Bind Gunicorn to api/v1/app.py.
- Import your data and environment variables from this project.

## Task 5: Serve your AirBnB clone - Web dynamic

### Requirements:
- Git clone your AirBnB_clone_v4.
- Your Gunicorn instance should serve content from web_dynamic/2-hbnb.py on port 5003.
- Setup Nginx so that the route / points to your Gunicorn instance.
- Setup Nginx to serve the static assets found in web_dynamic/static/.
- Reconfigure web_dynamic/static/scripts/2-hbnb.js to the correct IP.
- Nginx must serve this page both locally and on its public IP on port 5003.

**Note**: Don't forget to upload your Nginx configuration files for each task.

For detailed information on each task, refer to the [GitHub repository](https://github.com/alx-system_engineering-devops) in the respective directories and files mentioned.

