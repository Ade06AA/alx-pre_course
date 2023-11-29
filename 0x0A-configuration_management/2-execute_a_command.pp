# using exec
$pkill = '/usr/bin/pkill'
exec {'kill a process':
  command => "${pkill} -f killmenow"
}
