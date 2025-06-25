import requests, csv, subprocess

#fetch  botnet IP file as a text 
response = requests.get("https://feodotracker.abuse.ch/downloads/ipblocklist.csv").text

#delete previuos IPs from inbound/ outbound
rule = "netsh advfirewall firewall delete rule name='BadIP'"
subprocess.run(["Powershell", "-Command", rule])

#filter IPs from the doc
mycsv = csv.reader(filter(lambda x: not x.startswith("#"), response.splitlines()))
for row in mycsv:
    ip = row[1]
    if(ip)!=("dst_ip"):
        print("Added Rule to block:", ip)
        #add ips to outbound
        rule="netsh advfirewall firewall add rule name='BadIP' Dir=Out Action=Block RemoteIP="+ip
        subprocess.run(["Powershell", "-Command", rule])
        #add ips to inbound
        rule="netsh advfirewall firewall add rule name='BadIP' Dir=In Action=Block RemoteIP="+ip
        subprocess.run(["Powershell", "-Command", rule])
		
