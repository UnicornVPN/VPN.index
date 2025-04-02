server=free-unlimited.hideservers.net

install(){
  sudo apt install curl
  curl -L https://hide.me/download/linux-amd64 | tar -xz && sudo ./install.sh
}

enable(){
  systemctl enable $server
}

start(){
  systemctl start $server
}
