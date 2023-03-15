FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y

RUN pip3 install flask pymysql

WORKDIR /opt/source_code

COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]