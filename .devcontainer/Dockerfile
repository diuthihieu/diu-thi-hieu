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

# oh-my-zsh
RUN sh -c "$(wget https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"
RUN git clone --depth=1 \
    https://github.com/romkatv/powerlevel10k.git \
    ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k

# meslo font for powerlevel10k
ARG MESLO_URL="https://github.com/romkatv/powerlevel10k-media/raw/master"
ARG MESLO_DIR="/usr/share/fonts/truetype/meslo"
RUN sudo mkdir -p ${MESLO_DIR}
RUN sudo wget ${MESLO_URL}/MesloLGS%20NF%20Regular.ttf -O ${MESLO_DIR}/MesloLGSNFRegular.ttf
RUN sudo wget ${MESLO_URL}/MesloLGS%20NF%20Bold.ttf -O ${MESLO_DIR}/MesloLGSNFBold.ttf
RUN sudo wget ${MESLO_URL}/MesloLGS%20NF%20Italic.ttf -O ${MESLO_DIR}/MesloLGSNFItalic.ttf
RUN sudo wget ${MESLO_URL}/MesloLGS%20NF%20Bold%20Italic.ttf -O ${MESLO_DIR}/MesloLGSNFBoldItalic.ttf

# uv for python
RUN curl --proto '=https' --tlsv1.2 -LsSf https://astral.sh/uv/install.sh | sh -s --
RUN . $HOME/.local/bin/env && uv python install 3.12
