import scapy.all as s
from scapy_http import http
def paket_dinle(interface):
	s.sniff(iface=interface,store=False,prn=paket_analiz)
def paket_analiz(paket):
	if paket.haslayer(http.HTTPRequest):
		if paket.haslayer(s.Raw):
			print(paket[s.Raw].load)
paket_dinle("wlan0")
