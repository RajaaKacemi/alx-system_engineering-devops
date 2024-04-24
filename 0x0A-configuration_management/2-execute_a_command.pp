# This Puppet manifest kills a process named "killmenow" using the exec resource and pkill command.

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
