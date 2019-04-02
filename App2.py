from SnmpConnections import SnmpProtocol
from QueryExecuter import querytrigger
from Backbone import Backbone
from Switch import Switch
from Client import Client
from Helper import Helper


soru1 = "Bina Seçiniz:\n\n"
dbclass = querytrigger()

sql = "SELECT backbone.id as id, backbone.ip as ip, bina.ad as binaad,bina.id as binaid FROM backbone INNER JOIN bina ON (backbone.binaid = bina.id) WHERE backbone.switchkontrol = 1 ORDER BY backbone.id ASC"
records = dbclass.simpleselectquery(sql)

if(len(records) > 0):
    for record in records:
        soru1 = soru1+str(record[0])+". "+record[2]+" - "+record[1]+"\n"
    soru1 = soru1+"\nçıkmak için q"
    print(soru1)
