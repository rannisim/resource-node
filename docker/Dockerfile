FROM centos:centos7
USER root

ENV PYTHONPATH=/opt/resource-node

EXPOSE 8080

#Install python 3.7
RUN yum groupinstall -y "development tools"
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel wget
WORKDIR /opt
RUN wget https://www.python.org/ftp/python/3.7.5/Python-3.7.5.tgz && tar -xzvf Python-3.7.5.tgz
WORKDIR /opt/Python-3.7.5
RUN ./configure --enable-optimizations && make altinstall
WORKDIR /
RUN rm /opt/Python-3.7.5.tgz


#Setup the application files and requirements
WORKDIR /opt/resource-node/

SHELL ["/bin/bash", "-c"]
RUN pwd
ADD requirements.txt /opt/resource-node/
RUN pip3.7 install -r requirements.txt
ADD app/ /opt/resource-node/app/



CMD ["python3.7","app/main.py"]
