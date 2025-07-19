def Ip_Address(ip):
    if len(ip) !=4:
        return'Invalid Ip adress'
    if ((ip[0]>=0 and ip[0]<=255)and
        (ip[1]>=0 and ip[1]<=255)and
        (ip[2]>=0 and ip[2]<=255) and
        (ip[3]>=0 and ip[3]<=255)):
       return "valid Ip address"
    else:
        return "Invalid Ip address"
inp=list(map(int,input().split(".")))
print(Ip_Address(inp))


