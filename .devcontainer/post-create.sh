. $HOME/.local/bin/env && uv sync

echo >> ~/.zshrc
echo "# devcontainer configuration" >> ~/.zshrc 
echo source $HOME/.local/bin/env >> ~/.zshrc
echo source /workspaces/diu-thi-hieu/.venv/bin/activate >> ~/.zshrc
echo export HISTFILE="/workspaces/diu-thi-hieu/.zsh_history" >> ~/.zshrc
echo export HISTSIZE=1000 >> ~/.zshrc
echo export SAVEHIST=10000 >> ~/.zshrc