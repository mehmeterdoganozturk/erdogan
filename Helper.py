class Helper:

    def decimaltohex(decimal):
        a = (decimal.split('.'))
        mac1 = hex(int(a[14])).split('x')[-1]
        mac2 = hex(int(a[15])).split('x')[-1]
        mac3 = hex(int(a[16])).split('x')[-1]
        mac4 = hex(int(a[17])).split('x')[-1]
        mac5 = hex(int(a[18])).split('x')[-1]
        mac6 = hex(int(a[19].split(' ')[0])).split('x')[-1]
        if (len(mac1) < 2):
            mac1 = '0' + mac1
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

        return (mac1 + ':' + mac2 + ':' + mac3 + ':' + mac4 + ':' + mac5 + ':' + mac6)