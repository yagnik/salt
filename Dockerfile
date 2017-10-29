from saltstack/centos-7-minimal

WORKDIR "."
RUN yum install -y gcc gcc-c++ python-devel python-pip
COPY requirements /tmp/requirements

RUN pip install -r /tmp/requirements/dev_python27.txt
CMD tail -f /dev/null
