import matplotlib.pyplot as plt

from pcapng import FileScanner   
from sys    import argv

DUMP_PATH = argv[1] if len(argv) >= 3 else ""
HIST_PATH = argv[2] if len(argv) >= 3 else ""


def dump_parser(packet_id):
    intervals = []

    with open(DUMP_PATH, 'rb') as fp:
        packets = list(FileScanner(fp))

        for idx in range(packet_id, len(packets) - 1):
            try:
                intervals.append(packets[idx].timestamp - packets[idx - 1].timestamp)
            except AttributeError as e:
                pass

    return intervals

def intervals_hist():
    plt.rc('axes', axisbelow = True)
    plt.figure(figsize = (28, 9))
    plt.subplots_adjust(wspace = 0.2, hspace = 0.2)
    
    plt.subplot(121)
    plt.title('Histogram of the lengths of inter-packet intervals of all packets')
    plt.xlabel('Time since previous packet')
    plt.ylabel('Probability')
    plt.grid(True, linestyle = '--', linewidth = 0.5)
    plt.hist(dump_parser(0), 35, density = 1, facecolor = 'r', alpha = 0.75)

    plt.subplot(122)
    plt.title('Histogram of the lengths of inter-packet intervals of packets from 100 to 236')
    plt.xlabel('Time since previous packet')
    plt.ylabel('Probability')
    plt.grid(True, linestyle = '--', linewidth = 0.5)
    plt.hist(dump_parser(100), 35, density = 1, facecolor = 'r', alpha = 0.75)

    plt.savefig(HIST_PATH)


if __name__ == "__main__":       
    intervals_hist() if len(argv) >= 3 else print("Usage:   histogram.py 'path_to_dump' 'full_path_to_histogram'")
