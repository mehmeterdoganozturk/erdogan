from SnmpConnections import SnmpProtocol
from QueryExecuter import querytrigger
from Backbone import Backbone
from Switch import Switch
from Client import Client

dbclass = querytrigger()

sql = "SELECT backbone.id as id, backbone.ip as ip, bina.ad as binaad,bina.id as binaid FROM backbone INNER JOIN bina ON (backbone.binaid = bina.id) WHERE backbone.switchkontrol = 1 ORDER BY backbone.id ASC"
records = dbclass.simpleselectquery(sql)

if(len(records) > 0):
    backbones = []
    SnmpProtocol = SnmpProtocol()
    for record in records:
        switches = []
        backbone = Backbone(str(record[0]), record[1], record[2], record[3])
        backbones.append(backbone)
        stmt = SnmpProtocol.execute(backbone.ip, '1.3.6.1.2.1.4.22.1.1', '"INTEGER: 28"')
        eachline = stmt.splitlines()
        for i in eachline:
            a = (i.split('.'))
            switch = Switch(a[11] + "." + a[12] + "." + a[13] + "." + a[14].split(' ')[0])
            switches.append(switch)
            backbone.setswitches(switches)

for backbone in backbones:
    print(backbone.id)
    print(backbone.binaad)
    print(backbone.ip)
    switches = backbone.switches
    for switchsingle in switches:
        stmt2 = SnmpProtocol.execute(switchsingle.ip,'1.3.6.1.2.1.17.7.1.2.2.1.2','-v "INTEGER: 418"')
        eachline = stmt2.splitlines()
        print("SwitchIp:"+switchsingle.ip)
        for i in eachline:
            clients = []
            #mac decimal to hexa-START
            a = (i.split('.'))
            mac1 = hex(int(a[14])).split('x')[-1]
            mac2 = hex(int(a[15])).split('x')[-1]
            mac3 = hex(int(a[16])).split('x')[-1]
            mac4 = hex(int(a[17])).split('x')[-1]
            mac5 = hex(int(a[18])).split('x')[-1]
            mac6 = hex(int(a[19].split(' ')[0])).split('x')[-1]
            if(len(mac1)<2):
                mac1 = '0'+mac1
            if (len(mac2) < 2):
                mac2 = '0' + mac2
            if (len(mac3) < 2):
                mac3 = '0' + mac3
            if (len(mac4) < 2):
                mac4 = '0' + mac4
            if (len(mac5) < 2):
                mac5 = '0' + mac5
            if (len(mac6) < 2):
                mac6 = '0' + mac6
            # mac decimal to hexa-END

            client = Client(mac1+':'+mac2+':'+mac3+':'+mac4+':'+mac5+':'+mac6)
            clients.append(client)
            switch.setClients(clients)
            for clientmac in clients:
                print(clientmac.mac)

