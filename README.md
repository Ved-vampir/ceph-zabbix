ceph-zabbix
===========

Zabbix plugin for Ceph monitoring

Installation
===========
Edit the *zabbix_agent_ceph_plugin.conf* to set the path to the bash script (default is /opt/ceph-status.sh) then add it to your zabbix agent config

Copy ceph-status.sh and help.py to folder, which is in conf. Check, that ceph-status.sh has a execute permition

Add the xml template and link them to your node.

Link the ceph templates to your hosts

Add user zabbix to sudoers for ceph and rados

zabbix ALL = NOPASSWD: /usr/bin/ceph

zabbix ALL = NOPASSWD: /usr/bin/rados

Check that bc is installed

Restart zabbix agent on every node, where conf was changed

What's next
==============

Actually zabbix agent pull data from script.
One option is to send directly from the script to zabbix trough zabbix-trapper
