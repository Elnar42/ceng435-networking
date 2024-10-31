from scapy.all import IP, ICMP, send

receiver_ip = "receiver"
message = "HI, FROM SENDER"

packet = IP(dst=receiver_ip, ttl=1) / ICMP() / message

send(packet)
print("ICMP packet with message sent successfully")
