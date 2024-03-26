# Define SSH client configuration file path
$file_path = '/etc/ssh/ssh_config'

# Ensure SSH client configuration file exists
file { $file_path:
  ensure => present,
}

# Configure SSH client to use the private key ~/.ssh/school
file_line { 'Declare identity file':
  ensure  => present,
  path    => $file_path,
  line    => '    IdentityFile ~/.ssh/school',
  require => File[$file_path],
}

# Configure SSH client to refuse to authenticate using a password
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => $file_path,
  line    => '    PasswordAuthentication no',
  require => File[$file_path],
}
