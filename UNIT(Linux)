import subprocess

# Set command variables
command0 = "ping -c 4 8.8.8.8"  # Ping the Internet with 4 packets
command1 = "traceroute 8.8.8.8"  # Trace Internet route
command2 = "ip a"  # Display network interfaces information

ans = True
while ans:
    print("""
    Simple Network Explorer (Linux)
    Daniel(c)
    1. Ping the Internet
    2. Trace Internet route
    3. Network Adapter Details
    4. Customized ping
    5. Exit/Quit
    """)
    ans = input("What would you like to do? ")
    if ans == "1":
        subprocess.run(command0, shell=True)
    elif ans == "2":
        subprocess.run(command1, shell=True)
    elif ans == "3":
        subprocess.run(command2, shell=True)
    elif ans == "4":
        add = input("What IP address would you like to ping? ")
        num = input("How many packets would you like to send? ")
        command3 = f"ping -c {num} {add}"  # Customized ping command
        subprocess.run(command3, shell=True)
    elif ans == "5":
        print("\nGoodbye")
        exit()
    elif ans != "":
        print("\nNot Valid Choice, Try again")
