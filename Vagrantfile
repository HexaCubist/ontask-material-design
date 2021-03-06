# -*- mode: ruby -*-
# vi: set ft=ruby :

# This is a Vagrantfile for OnTask Development
# Configuration of a basic development environment is done automatically
# Usage:
#  - Use 'vagrant up' to bring up the vagrant VM on your provider
#  - Use 'vagrant ssh' to load a shell interface with the VM
#  - Use 'vagrant halt' to bring down the vagrant VM
#  - Use 'vagrant destroy' to destroy the VM (but leave the files)
# For more information on how to use and configure Vagrant,
# see https://www.vagrantup.com/

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "geerlingguy/centos7"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  # NOTE: This will enable public access to the opened port
  config.vm.network "forwarded_port", guest: 8080, host: 8000, auto_correct: true

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  # config.vm.network "forwarded_port", guest: 80, host: 8080, host_ip: "127.0.0.1"

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"
  config.vm.synced_folder "./", "/srv/ontask"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    sudo yum update
    sudo yum install epel-release -y
    sudo yum update -y
    sudo yum install screen -y

    echo "Installing Redis..."
    sudo yum install redis -y
    sudo systemctl start redis.service
    sudo systemctl enable redis

    echo "Installing Postgresql..."
    sudo yum install -y https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
    sudo yum install -y postgresql96 postgresql96-server
    sudo systemctl enable postgresql-9.6
    sudo /usr/pgsql-9.6/bin/postgresql96-setup initdb
    sudo systemctl start postgresql-9.6
    sudo -u postgres psql -c "create role ontask with login password 'DEVTESTPASS';"
    sudo -u postgres psql -c "create database ontask OWNER ontask template template0 encoding 'UTF8' lc_collate 'en_US.UTF-8' lc_ctype 'en_US.UTF-8';"
    # update postgresql setup to allow connection to local database
    # "local" is for Unix domain socket connections only
    sudo echo "local   all             all                                     peer" > /var/lib/pgsql/9.6/data/pg_hba.conf
    # IPv4 local connections:
    sudo echo "host    all             all             127.0.0.1/32            md5" >> /var/lib/pgsql/9.6/data/pg_hba.conf
    # IPv6 local connections:
    sudo echo "host    all             all             ::1/128                 md5" >> /var/lib/pgsql/9.6/data/pg_hba.conf
    sudo service postgresql-9.6 restart

    echo "Python should already be installed. Installing pip..."
    sudo yum -y install python-pip
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools

    echo "Installing OnTask (located in /srv/ontask)..."
    cd /srv/ontask/
    sudo pip install -r requirements/development.txt

    echo "OnTask Configuration..."
    sudo mkdir logs
    cd src
    echo " - Configure ENV"
    sudo echo "DEBUG=True" > ontask/settings/local.env
    sudo echo "TIME_ZONE=UTC" >> ontask/settings/local.env
    sudo echo "BASE_URL=''" >> ontask/settings/local.env
    sudo echo "DOMAIN_NAME=127.0.0.1" >> ontask/settings/local.env
    sudo echo "SHOW_HOME_FOOTER_IMAGE=True" >> ontask/settings/local.env
    sudo echo "# syntax: DATABASE_URL=postgres://username:password@127.0.0.1:5432/database" >> ontask/settings/local.env
    sudo echo "DATABASE_URL=postgres://ontask:DEVTESTPASS@127.0.0.1:5432/ontask" >> ontask/settings/local.env
    sudo echo "REDIS_URL=redis://127.0.0.1:6379/1" >> ontask/settings/local.env
    sudo echo -n "SECRET_KEY=" >> ontask/settings/local.env
    sudo python -c 'import random; import string; print("".join([random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))' >> ontask/settings/local.env
    
    python manage.py makemigrations profiles accounts workflow dataops
    python manage.py makemigrations table action logs scheduler table
    python manage.py migrate
    python manage.py runscript -v1 --traceback initial_data

    echo "from django.contrib.auth import get_user_model; User = get_user_model(); u = User.objects.create_user(email='admin@example.com',password='admin'); u.is_superuser = True; u.is_staff = True; u.save()" | python manage.py shell
    cd ../src/
    python manage.py collectstatic --noinput

    echo "Running Server... Should become live at http://127.0.0.1:8000 with username admin email admin@localhost and password admin"
    # python manage.py runserver_plus 0.0.0.0:8080
  SHELL

  config.trigger.after :up do |trigger|
    trigger.run_remote = {inline: "cd /srv/ontask/src && screen -dmS OnTask python manage.py runserver_plus 0.0.0.0:8080 --settings=ontask.settings.development"}
  end

end
