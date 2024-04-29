<<<<<<< HEAD
General
What is localhost/127.0.0.1
What is 0.0.0.0
What is /etc/hosts
How to display your machine’s active network interfaces
=======
Localhost (127.0.0.1):

127.0.0.1 is the IP address assigned to the loopback or local-only interface.
It’s a “fake” network adapter that can only communicate within the same host (your own machine).
When an application listens on 127.0.0.1, it only accepts connections from within the same machine.
“localhost” is the hostname associated with the 127.0.0.1 IP address.
It’s usually set in the /etc/hosts file (or the Windows equivalent, typically located at C:\Windows\System32\Drivers\etc\hosts).
You can use “localhost” just like any other hostname;
for example, try running ping localhost to see how it resolves to 127.0.0.1.
0.0.0.0:
When a server is configured to listen on 0.0.0.0, it means “listen on every available network interface.”
The loopback adapter (127.0.0.1) appears to the server process as just another network adapter on the machine.
So, a server listening on 0.0.0.0 will accept connections on all available interfaces.

/etc/hosts:
The /etc/hosts file (or its Windows equivalent) contains mappings of hostnames to IP addresses.
It’s used for local DNS resolution before querying external DNS servers.
You can add custom entries to this file to associate hostnames with specific IP addresses.
For example, adding 127.0.0.1 localhost in the hosts file ensures that “localhost” resolves to 127.0.0.1.

Displaying Active Network Interfaces:
To view your machine’s active network interfaces, you can use various commands based on your operating system:

Linux/Unix: Use the ifconfig or ip addr command.
Windows: Run ipconfig in the command prompt.
macOS: Use ifconfig or networksetup -listallhardwareports.
>>>>>>> origin/master
