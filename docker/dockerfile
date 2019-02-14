FROM fedora:latest

LABEL Author="Landry SERIN"
LABEL email="landry.serin@insa-cvl.fr"

ENV EVAL_PORT 8080
EXPOSE 8080

RUN dnf install python3;\
    dnf clean all;

RUN useradd -d /var/lib/http -M -r -s /sbin/nologin http

USER http

COPY [--chown=http:http] httpserver.py /

ENTRYPOINT [ "/httpserver.py" ]
