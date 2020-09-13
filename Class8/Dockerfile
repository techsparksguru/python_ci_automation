FROM jenkinsci/blueocean
USER root
RUN apk add python3 py3-pip
COPY jobs/ /var/jenkins_home/jobs/
COPY chromedriver /usr/local/bin