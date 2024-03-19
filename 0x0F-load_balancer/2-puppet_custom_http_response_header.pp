# Puppet script to install Nginx server

exec { 'update system':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

exec { 'HTTP header':
  command  => 'sed -i "51i \\\tadd_header X-Served-By: $HOSTNAME;" /etc/nginx/sites-enabled/default && service nginx restart',
  provider => 'shell',
  path     => '/usr/bin:/bin', # Set the PATH to include binaries
  require  => Package['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
