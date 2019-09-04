# Flask_microservice

## Installation
*Use the package manager [PIP3](https://pip.pypa.io/en/stable/).*

*Install docker on 18.04 [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)*

**To run with docker**
```bash
cd src
sudo docker build -t flaskapp:latest .
sudo docker run -it -d -p 5000:5000 flaskapp
```

**To run without docker**
```bash
cd src
pip install -r requirements.txt
export FLASK_APP=app.py
flask run
```

The project will be available at **127.0.0.1:5000**.



