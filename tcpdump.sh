#保存为cap文件格式
#tcpdump -i wlan0 host 192.168.1.106 -w liu.cap

#保存为pcap文件格式
tcpdump -w test.pcap -i wlan0
#读取pcap文件格式
tcpdump -nnr test.pcap



