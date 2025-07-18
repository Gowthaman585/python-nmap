import nmap

#object creation for PortScanner
scanner = nmap.PortScanner()

#get the ip and port number
ip_address = input("Enter ip : ")
port_num = int(input("Enter port : "))

#the portnumber must be casted into string scan accepts is as string
scan_result = scanner.scan(ip_address,str(port_num))

#but in scan_result which is nested dictinary to get the status we should need to use port_number as int
openORclosed = scan_result['scan'][ip_address]['tcp'][port_num]['state']

print(f"{port_num} is {openORclosed}")