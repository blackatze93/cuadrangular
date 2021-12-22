FROM python:3

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# By copying over requirements first, we make sure that Docker will cache
# our installed requirements rather than reinstall them on every build
COPY requirements.txt /app/requirements.txt
#COPY package.json /app/package.json
#COPY package-lock.json /app/package-lock.json
#COPY entrypoint.sh /app/entrypoint.sh

#RUN curl -fsSL https://deb.nodesource.com/setup_17.x | bash -
#RUN apt-get install -y nodejs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN npm install
#RUN chmod +x /app/entrypoint.sh

# Now copy in our code
COPY . /app