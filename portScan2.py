import nmap

#object creation for PortScanner
scanner = nmap.PortScanner()

#get the ip and port number
ip_address = input("Enter ip : ")
port_num = int(input("Enter port : "))

#the portnumber must be casted into string scan accepts is as string
scan_result = scanner.scan(ip_address,str(port_num))

#gather the all availabe info-dict under the ip address
result = scan_result['scan'][ip_address]

#retuns all kind of protocols used by the ip
protocol = result.all_protocols()

#[0] is used to select specific list of dictionary under hostnames
print(f"host-name     :  {result['hostnames'][0]['name']}")

print(f"host-status   :  {result['status']['state']}")
print(f"port-service  :  { result['tcp'][port_num]['name']}")

#[0] is used to neglect the ['tcp'] list
print(f"protocol-used :  {protocol[0]}")