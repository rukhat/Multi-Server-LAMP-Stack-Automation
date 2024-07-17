# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.provider :libvirt do |libvirt|
    libvirt.driver = "kvm"
    libvirt.memory = 1024
    libvirt.cpus = 1
  end

  config.vm.define "db" do |db|
    db.vm.box = "generic/ubuntu2004"
    db.vm.hostname = "db-server"
    db.vm.network "private_network", ip: "192.168.56.10"
  end

  config.vm.define "auth" do |auth|
    auth.vm.box = "generic/ubuntu2004"
    auth.vm.hostname = "auth-server"
    auth.vm.network "private_network", ip: "192.168.56.11"
  end

  config.vm.define "app" do |app|
    app.vm.box = "generic/ubuntu2004"
    app.vm.hostname = "app-server"
    app.vm.network "private_network", ip: "192.168.56.12"
  end

  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.groups = {
        "db" => ["db"],
        "auth" => ["auth"],
        "app" => ["app"]
    }
    ansible.raw_ssh_args = ['-o UserKnownHostsFile=/dev/null', '-o StrictHostKeyChecking=no']
    ansible.extra_vars = { ansible_python_interpreter: "/usr/bin/python3" }
  end
end
