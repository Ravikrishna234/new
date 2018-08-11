"""SOCIALNETWORKING"""

def follow(network, arg1, arg2):
    """social"""
    if arg1 not in network:
        network[arg1] = [arg2]
    else:
        network[arg1].append(arg2)
    return network

def unfollow(network, arg1, arg2):
    """social"""
    network[arg1].remove(arg2)
    return network

def delete_person(network, arg1):
    """social"""
    for i in network.values():
        if arg1 in i:
            i.remove(arg1)
    if arg1 in network.keys():
        del network[arg1]
    return network

def main():
    """social"""
    network = eval(input())
    lines = int(input())
    for i in range(lines):
        i += 1
        line = input()
        output = line.split(" ")
        if output[0] == "follow":
            network = follow(network, output[1], output[2])
        elif output[0] == "unfollow":
            network = unfollow(network, output[1], output[2])
        elif output[0] == "delete":
            network = delete_person(network, output[1])

    print(network)

if __name__ == "__main__":
    main()
