def validateIP(ip):
    if len(ip) !=4:
        return 'Invalid Ip Address'
    if ((ip[0]>=0 and ip[0]<=255)and
       (ip[1]>=0 and ip[1]<=255)and
       (ip[2]>=0 and ip[2]<=255)and
       (ip[3]>=0 and ip[3]<=255)):
             return 'valid Ip Address'
    else:
        return 'Invalid Ip Address'
        

inp=list(map(int,input().split()))
print(validateIP(inp))
