import xml.dom.minidom
from ncclient import manager
m = manager.connect(
 host="192.168.56.102",
 port=830,
 username="cisco",
 password="cisco123!",
 hostkey_verify=False
 )

'''
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
'''

netconf_reply = m.get_config(source="running")
# print(netconf_reply)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_filter = """
<filter>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
# netconf_reply = m.get_config(source="running", filter=netconf_filter)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_hostname = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <hostname>CSR1kv</hostname>
 </native>
</config>
"""
# netconf_reply = m.edit_config(target="running", config=netconf_hostname)
# print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_loopback = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>1</name>
 <description>My first NETCONF loopback</description>
 <ip>
 <address>
 <primary>
 <address>10.1.1.1</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
# --------------------------------------the code follow this line will effects this line code

netconf_newloop = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>2</name>
 <description>My second NETCONF loopback</description>
 <ip>
 <address>
 <primary>
 <address>10.1.2.1</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_newloop)
# It will return "RPCError: inconsistent value: Device refused one or more commands,If IP address is the same subnet"


