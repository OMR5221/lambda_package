FROM amazonlinux:latest

RUN yum update -y

WORKDIR /var/task
ENV WORKDIR /var/task

RUN yum -y install git \
    python36 \
    python36-pip \
    zip \
    && yum clean all

RUN python3 -m pip install --upgrade pip \
    # boto3 is available to lambda processes by default,
    # but it's not in the amazonlinux image
    && python3 -m pip install requests -t packages/ \
    && python3 -m pip install bs4 -t packages/

# Copy initial source codes into container.
COPY lambda_function.py "$WORKDIR/lambda_function.py"

# Compress all source codes.
RUN zip -r9 $WORKDIR/lambda.zip packages/ lambda_function.py

CMD ["/bin/bash"]

# --- Other commands to run to get lambda.zip
# 1.  cd esbi_pull_lambda/
# 2.  sudo docker build -t mylambda .
# 3.  sudo docker run mylambda
# 4.  sudo docker ps -a
# 5.  sudo docker cp <container_id>:/var/task/lambda.zip .
