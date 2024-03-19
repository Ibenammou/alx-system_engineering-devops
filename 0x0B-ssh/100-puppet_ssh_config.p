# ssh configuration with Puppet

include stdlib

file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}

# file { '/home/ubuntu/.ssh/':
  # ensure => directory,
# }

# file { '/home/ubuntu/.ssh/config':
  # ensure  => present,
  # content => "Host *\n
               # IdentityFile ~/.ssh/school\n
               # PasswordAuthentication no\n",
  # replace => true,
# }

# augeas { 'ssh_config_password_auth':
  # context => '/files/etc/ssh/ssh_config',
  # changes => ['set Host[1]/PasswordAuthentication no'],
# }

# augeas { 'ssh_config_identity_file':
  # context => '/files/etc/ssh/ssh_config',
  # changes => ['set Host[1]/IdentityFile ~/.ssh/school'],
# }
