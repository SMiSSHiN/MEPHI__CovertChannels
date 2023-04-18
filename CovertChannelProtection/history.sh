#client_a
ifconfig
python3.10 SimpleCovertChannel/covert_channel.py 172.17.0.2 8888 1001
python3.10 SimpleCovertChannel/covert_channel.py 172.17.0.2 8888 1001111


# client_b
ifconfig
tcpdump -i eth0 udp port 8888 or icmp                       # смотрим, как приходят udp-дейтаграммы
iptables -P INPUT DROP                                      # запрещаем весь входящий трафик
iptables -A INPUT -p udp -m limit --limit 1/m -j ACCEPT     # разрешаем входящий трафик по лимиту
