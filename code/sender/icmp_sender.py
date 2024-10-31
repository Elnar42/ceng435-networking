from scapy.all import IP, ICMP, send

receiver_ip = "receiver"
packet = IP(dst=receiver_ip, ttl=1) / ICMP()

print("Sending ICMP packet with TTL=1 to receiver...")
send(packet)
print("ICMP packet sent.")
