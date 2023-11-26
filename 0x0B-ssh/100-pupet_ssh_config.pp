# doc

exec { 'echo':
  path => 'usr/bin:/bin',
  command => 'echo '' IdentifyFile ~/.ssh/school\n PasswordAuthentication no'' >> /etc/ssh/ssh_config',
  return => [0, 1],
} 
