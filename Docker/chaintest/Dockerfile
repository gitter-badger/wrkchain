FROM debian:stretch-slim

RUN apt-get update && \
    apt-get -y install \
        git \
        vim \
        telnet \
        make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev \
        libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev

RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash && \
    /root/.pyenv/bin/pyenv install 3.7.2

WORKDIR "/root"

ARG GO_VERSION

RUN wget https://dl.google.com/go/go1.$GO_VERSION.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf go1.$GO_VERSION.linux-amd64.tar.gz && \
    mkdir ~/.go

ENV GOPATH="/root/.go"
ENV GOROOT="/usr/local/go"
ENV PATH="/usr/local/go/bin:/root/.go/bin:${PATH}"

RUN mkdir /root/.ssh

RUN go get github.com/ethereum/go-ethereum
RUN go install github.com/ethereum/go-ethereum/cmd/geth

ENV PATH="/root/.pyenv/versions/3.7.2/bin:${PATH}"

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV PYTHONPATH /haiku

RUN echo "telnet wrkchain-rpc-validator-1 8101" >> /root/.bash_history && \
    echo "alias ll='ls -la'" >> /root/.bashrc

CMD /bin/sleep 600
