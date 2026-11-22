def main():
    drop = 0
    count = 0
    inp = []

    cap = int(input("Enter the bucket size:\n"))
    process = int(input("Enter the processing rate:\n"))
    nsec = int(input("Enter the number of seconds you want to simulate:\n"))

    for i in range(nsec):
        pkt = int(input(f"Enter the size of the packet entering at {i + 1} sec:\n"))
        inp.append(pkt)

    print("\nSecond | Packet Received | Packet Sent | Packet Left | Dropped")
    print("----------------------------------------------------------------")

    for i in range(nsec):
        count += inp[i]
        if count > cap:
            drop = count - cap
            count = cap

        mini = min(count, process)
        count -= mini
        print(f"{i + 1}\t {inp[i]}\t\t {mini}\t\t {count}\t\t {drop}")
        drop = 0

    sec = nsec
    while count != 0:
        sec += 1
        if count > cap:
            drop = count - cap
            count = cap

        mini = min(count, process)
        count -= mini
        print(f"{sec}\t 0\t\t {mini}\t\t {count}\t\t {drop}")
        drop = 0


if __name__ == "__main__":
    main()