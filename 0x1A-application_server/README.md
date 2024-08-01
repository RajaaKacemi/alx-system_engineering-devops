# Application Server Setup

This project involves setting up the development environment to serve the AirBnB clone v2 - Web framework on web-01 for testing and debugging.

## Steps

1. Ensure Task #3 of the SSH Project is completed.
2. Install net-tools:
    ```bash
    sudo apt install -y net-tools
    ```
3. Clone the AirBnB_clone_v2 repository:
    ```bash
    git clone <your-repo-url>
    cd AirBnB_clone_v2
    ```
4. Configure the Flask application:
    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/airbnb-onepage/', strict_slashes=False)
    def hello():
        return "Hello HBNB!"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    ```
5. Run the Flask application:
    ```bash
    python3 -m web_flask.0-hello_route
    ```
6. Test the setup:
    ```bash
    curl 127.0.0.1:5000/airbnb-onepage/
    ```

## Resources

- [Application server vs web server](https://www.digitalocean.com/community/tutorials/application-server-vs-web-server)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-with-gunicorn-and-nginx-on-ubuntu-16-04)
- [Running Gunicorn](https://docs.gunicorn.org/en/stable/run.html)
- [Upstart documentation](http://upstart.ubuntu.com/cookbook/)

