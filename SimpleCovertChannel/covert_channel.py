import socket

from sys        import argv
from time       import sleep, time 


DEST_IP         = argv[1]       if len(argv) >= 3 else ""
DEST_PORT       = int(argv[2])  if len(argv) >= 3 else ""
TIME_INTERVAL   = 2


"""
    Description :   Convert string to binary string 
    Comment     :   Not used
"""
def message_to_binary(message):
    return ''.join(format(ord(i), '08b') for i in message)

def send_packet(sock):
    initial_time = time()
    sock.sendto(bytes(), (DEST_IP, DEST_PORT))

    sleep(TIME_INTERVAL - (time() - initial_time))

def send_message(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send the initial packet, it will indicate that the message transmission has begun
    send_packet(sock)

    for bit in message:
        sleep(TIME_INTERVAL) if bit == '0' else send_packet(sock)
    
    print("[Success]    Message has been sent")


if __name__ == "__main__":
    send_message(argv[3]) if len(argv) >= 4 else print("Usage:   covert_channel.py 'dest_ip' 'dest_port' 'msg_in_bits'")
