FROM ubuntu:14.04
MAINTAINER Colin Powell "colin.powell@gmail.com"
RUN apt-get -qq update
RUN apt-get install -y python-dev python-setuptools git
RUN easy_install pip
RUN pip install virtualenv
RUN pip install uwsgi
RUN virtualenv --no-site-packages /opt/ve/farmstand
ADD . /opt/apps/farmstand
ADD etc/gunicorn.conf /opt/gunicorn_farmstand.conf
ADD etc/run.sh /usr/local/bin/run_farmstand
RUN (cd /opt/apps/farmstand && git remote rm origin)
RUN (cd /opt/apps/farmstand && git remote add origin https://github.com/powellc/farmstand.git)
RUN (cd /opt/apps/farmstand && python setup.py install)
EXPOSE 30321
CMD ["/bin/sh", "-e", "/usr/local/bin/run_farmstand"]
