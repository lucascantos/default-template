FROM python:3.8-alpine
# Install OS dependencies
RUN apk update \
    && apk add gcc libc-dev bash git npm 

# Make folder and copy files to it
RUN mkdir -p /home/deploy/.ssh/ /home/deploy/app/
COPY . /home/deploy/app/
WORKDIR /home/deploy/app/

# Install python packages
RUN pip install --upgrade pip
RUN pip install pre-commit pyyaml
RUN pip install -r requirements-lint.txt 
RUN pip install -r requirements-test.txt 
RUN npm install -g serverless serverless-offline

# Expose Port 3000 for serverless
EXPOSE 3000
# Run serverless offline
ENTRYPOINT [ "sls", "offline" ]