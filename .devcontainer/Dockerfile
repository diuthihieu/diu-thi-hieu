FROM ubuntu:22.04

RUN apt update && apt upgrade -y && apt install \
    software-properties-common \
    sudo zsh wget curl git vim zip \
    bpytop cloc \
    -y

# user
ARG USER_NAME=hieudt
RUN groupadd ${USER_NAME}
RUN adduser --shell /usr/bin/zsh --gecos '' --ingroup ${USER_NAME} --disabled-password ${USER_NAME}
RUN usermod -aG sudo ${USER_NAME}
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ${USER_NAME}

# python tools
# RUN pip3 install ipykernel pylance nbconvert

# uv for python
RUN curl --proto '=https' --tlsv1.2 -LsSf https://astral.sh/uv/install.sh | sh -s --
RUN . $HOME/.local/bin/env && uv python install 3.12

# oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

