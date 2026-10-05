FROM ubuntu:26.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y \
        systemd \
        systemd-sysv \
        sudo \
        nano \
        vim \
        wget \
        iproute2 \
        iputils-ping \
        ca-certificates \
        openssh-server \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/bash etudiant && \
    echo "etudiant:password" | chpasswd && \
    usermod -aG sudo etudiant

STOPSIGNAL SIGRTMIN+3

CMD ["/sbin/init"]
