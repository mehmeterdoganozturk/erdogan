import os
class SnmpProtocol:

    def __init__(self,snmpcmd = "snmpwalk -v 3",username = "-u Yrg_snmp_ro",level = "-l authPriv",autprotocol = "-a MD5",privprotocol = "-x DES",authpasswd = "-A Yrg_snmp_bim2014",privpasswd = "-X Yrg_snmp_bim2015"):
        self.snmpcmd = snmpcmd
        self.username = username
        self.level = level
        self.autprotocol = autprotocol
        self.privprotocol = privprotocol
        self.authpasswd = authpasswd
        self.privpasswd = privpasswd

    def execute(self,deviceip,oid,filter = ''):
        self.deviceip = deviceip
        self.oid = oid
        self.filter = filter
        if(filter == ''):
            stmt = os.popen(self.snmpcmd + " " + self.username + " " + self.level + " " + self.autprotocol + " " + self.privprotocol + " " + self.authpasswd + " " + self.privpasswd + " " + self.deviceip + " " + self.oid).read()
        else:
            stmt = os.popen(self.snmpcmd + " " + self.username + " " + self.level + " " + self.autprotocol + " " + self.privprotocol + " " + self.authpasswd + " " + self.privpasswd + " " + self.deviceip + " " + self.oid + " |grep " + self.filter).read()
        return stmt











