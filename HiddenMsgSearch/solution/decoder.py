from pcapng import FileScanner   
from sys    import argv
from math   import ceil


DUMP_PATH       = argv[1] if len(argv) >= 2 else ""
TIME_INTERVAL   = 2


def dump_parser(packet_id):
    with open(DUMP_PATH, 'rb') as fp:
        packets     = list(FileScanner(fp))
        intervals   = []

        for idx in range(packet_id, len(packets) - 1):
            try:
                intervals.append(packets[idx].timestamp - packets[idx - 1].timestamp)
            except AttributeError as e:
                pass

    return intervals

def decoder(intervals):
    message = ""

    for interval in intervals:
        message += str(ceil(max(interval - TIME_INTERVAL, 0)))
    
    return bytes.fromhex(hex(int(message, 2))[2:]).decode("utf-8")


if __name__ == "__main__":
    print("Hidden message:  ", decoder(dump_parser(100))) if len(argv) >= 2 else print("Usage:   decoder.py 'path_to_dump'")
