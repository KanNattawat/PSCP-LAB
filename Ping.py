"""pscp"""
def main():
    """main"""
    total_of_time = 0
    avg_time = 0
    sett = set()
    cal(total_of_time, avg_time, sett)

def cal(total_of_time, avg_time, sett):
    """cal"""
    con = 1
    for _ in range(2):
        locate_ip = input()

    locate_ip = input().replace("[", "")
    locate_with = locate_ip.find("with") - 1
    if locate_ip.find("]") != -1:
        locate_with -= 1
    while locate_ip[locate_with-con].isnumeric() or locate_ip[locate_with-con] == "." \
or locate_ip[locate_with-con] == ":":
        con += 1
    locate_first_ip = locate_with - con
    ip_adress = locate_ip[locate_first_ip:locate_with].replace(" ", "")

    loop(total_of_time, avg_time, sett, ip_adress)


def loop(total_of_time, avg_time, sett, ip_adress):
    """loop"""
    received = 4
    lost = 0
    lost_percent = 0
    for _ in range(4):
        packet = input()
        locate_time = packet.find("time") + 5
        locate_ms = packet.find("ms") - 1
        if locate_time - 5 == -1 or locate_ms + 1 == -1:
            received -= 1
            lost += 1
            lost_percent += 25
            continue
        elif packet[locate_time:locate_ms+1].isnumeric():
            packet_ping = int(packet[locate_time:locate_ms+1])
            if packet[locate_time - 1] == "<":
                packet_ping = 0
            total_of_time += packet_ping

        sett.add(packet_ping)

    if received != 0:
        avg_time = total_of_time / received
    print("Ping statistics for "+ip_adress+":")

    out(received, lost, lost_percent, avg_time, sett)

def out(received, lost, lost_percent, avg_time, sett):
    """out"""
    lost_percent = str(lost_percent) + "%"
    avg_time = str(int(avg_time))
    sett = sorted(sett)
    minping = str(*sett[:1])
    maxping = str(*sett[-1::])

    print("    Packets: Sent = 4,", "Received =", str(received)+",", "Lost =", str(lost), \
"(%s loss)," %lost_percent)
    if received != 0:
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = "+minping+"ms"+", Maximum = "+maxping+"ms"+", Average = "\
+avg_time+"ms")

main()
