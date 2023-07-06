link(){
    mkdir -p src
    ln -srf ../../ansible src/
}


new(){
    ver=ubuntu2204
    #vagrant init generic/$ver
    vagrant up --provider=libvirt
    vagrant ssh
}

link