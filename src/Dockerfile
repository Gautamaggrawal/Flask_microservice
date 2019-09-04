from alpine:latest
RUN apk add --no-cache python3-dev \
	&& pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN  pip3 install --no-cache-dir -r requirements.txt
expose 5000
RUN export FLASK_APP=app.py
CMD [ "flask", "run"]



