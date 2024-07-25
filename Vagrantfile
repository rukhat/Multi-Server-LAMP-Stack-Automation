# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Configure the VM provider (in this case, libvirt/KVM)
  
  config.vm.provider :libvirt do |libvirt|
    libvirt.driver = "kvm"
    libvirt.memory = 1024   # Allocate 1GB of RAM
    libvirt.cpus = 1        # Allocate 1 CPU core
  end

  # Define the database server VM
  config.vm.define "db" do |db|
    db.vm.box = "generic/ubuntu2004"    # Use Ubuntu 20.04 as the base image
    db.vm.hostname = "db-server"
    db.vm.network "private_network", ip: "192.168.56.10"    # Assign a static IP
  end

  # Define the authentication server VM
  config.vm.define "auth" do |auth|
    auth.vm.box = "generic/ubuntu2004"
    auth.vm.hostname = "auth-server"
    auth.vm.network "private_network", ip: "192.168.56.11"
  end

  # Define the application server VM
  config.vm.define "app" do |app|
    app.vm.box = "generic/ubuntu2004"
    app.vm.hostname = "app-server"
    app.vm.network "private_network", ip: "192.168.56.12"
  end

  # Provision all VMs using Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.playbook = "playbook.yml"
    ansible.groups = {
        "db" => ["db"],
        "auth" => ["auth"],
        "app" => ["app"]
    }
    # Disable SSH host key checking for easier provisioning
    ansible.raw_ssh_args = ['-o UserKnownHostsFile=/dev/null', '-o StrictHostKeyChecking=no']
    # Specify the Python interpreter to use
    ansible.extra_vars = { ansible_python_interpreter: "/usr/bin/python3" }
  end
end
