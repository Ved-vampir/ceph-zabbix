ceph-zabbix
===========

Zabbix plugin for Ceph monitoring

Installation
===========

On every monitoring node follow steps:

1. Copy zabbix_agent_ceph_plugin.conf to /etc/zabbix/zabbix_agentd.d folder.

2. Copy ceph-status.sh to /opt folder (or another, but in this case don't forget to change path in conf file). Make sure, that zabbix user has an execute rights on this script.

3. Set read right on ceph keyring file for zabbix user (e.g. like this: sudo setfacl -m "u:zabbix:r" /etc/ceph/ceph.client.admin.keyring)

4. Restart zabbix agent service (/etc/init.d/zabbix-agent restart)

5. Make sure, that zabbix agent was started successfully (e.g. via ps aux | grep zabbix) and that zabbix user can call ceph commands (try to run sudo -u zabbix ceph -s)

After this go to zabbix UI and add templates for metrics. Link them to nodes.

All metrics will work this global Ceph commands, so, they can be used on any Ceph node.

Make sure, bc is installed on nodes (it is used bu script)

What's next
==============

Actually zabbix agent pull data from script.
One option is to send directly from the script to zabbix trough zabbix-trapper
