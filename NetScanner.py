import scapy.all as scapy

#1-Arp_request
#2-Broadcast
#3-Response

#Agda bu ip adresini bulmaya calisiyor
arpRequestPacket = scapy.ARP(pdst = "10.0.2.1/24")

#Scapy kutuphanesinde ki help metodu gibi
#scapy.ls(scapy.ARP())

broadcastPacket = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
#scapy.ls(scapy.Ether())

combinedPacket = broadcastPacket/arpRequestPacket

(answeredList, unansweredList) = scapy.srp(combinedPacket, timeout = 1)

#Cevap veren iplerin ozeti
answeredList.summary()