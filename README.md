# python_systemfssecurity
some works performed for the security of filesystems

What I want to do here:
Because of some problems from 1st line support like:
*after on-site service the machine has slowed down
*there's some problems with machine performance
*and others similar cases...

I want to write some file system monitor to check if any files from the service flash drive(because they use their pendrives to reinstall/backup the OS/software) are gonna attempt to do some nasty things on the device FS.

Probably the final version of that script should work as a running in backgroud FS monitor, with the FS states changes synchronization with Apache Kafka instance on the projects network(TBA later).
