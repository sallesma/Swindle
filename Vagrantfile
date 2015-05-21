# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.network "forwarded_port", guest: 8000, host: 8080

  config.vm.synced_folder ".", "/home/vagrant/swindle", owner: "vagrant", group: "vagrant"

  config.vm.provision :shell, path: "bootstrap-vagrant.sh"
  config.vm.provision :shell, path: "bootstrap-vagrant-always.sh", run: "always"
end
