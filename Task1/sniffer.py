from scapy.all import sniff, IP

def packet_callback(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto

        print("Source IP:", src)
        print("Destination IP:", dst)
        print("Protocol:", proto)
        print("---------------------------")

print("Starting Network Sniffer...")

sniff(prn=packet_callback, count=10)