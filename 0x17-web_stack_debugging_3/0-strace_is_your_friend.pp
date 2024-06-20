# puppet command to deal with typo in wp-settings.php

# Fix wp-settings.php using sed command
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
