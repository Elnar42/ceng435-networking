from scapy.all import sniff, IP, ICMP

def handle_packet(packet):
    if IP in packet and ICMP in packet and packet[IP].ttl == 1 and packet[ICMP].type == 8:
        print("Received ICMP request packet:")
        packet.show()

print("Listening for ICMP request packets with TTL=1...")
sniff(filter="icmp", prn=handle_packet)
