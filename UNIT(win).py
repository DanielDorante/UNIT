import os
# set command variables#
command0 = "ping 8.8.8.8"
command1 = "tracert 8.8.8.8"
command2 = "ipconfig"

ans=True
while ans:
    print ("""
    Simple Network Explorer 
    Daniel(c)
    1.Ping the Internet
    2.Trace Internet route
    3.Network Adapter Details
    4.Customized ping
    5.Exit/Quit
    """"")
    ans=input("What would you like to do? ")
    if ans=="1": 
      os.system(command0)
    elif ans=="2":
      os.system(command1)
    elif ans=="3":
      os.system(command2)
    elif ans=="4":
      add=input("what IP address would you like to ping? ") 
      num=input("how man packets would you like to send? ")
      command3 = "ping " + (add) + (" -n ") + (num)
      os.system(command3)
    elif ans=="5":
      print("\n goodbye")
      exit()
    elif ans !="":
      print("\n Not Valid Choice Try again")
