# Puppet manifest file to install a package

# Install python
package { 'python3.8':
  ensure => present,
}

# pip
package { 'python3-pip':
  ensure => present,
}

# flask
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# werkzeug
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
