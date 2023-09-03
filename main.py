import sacn
import time
import argparse
from pythonosc import udp_client

    # provide an IP-Address to bind to if you want to send multicast packets from a specific interface
receiver = sacn.sACNreceiver()
receiver.start()  # start the receiving thread
parser = argparse.ArgumentParser()
parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=9000,
      help="The port the OSC server is listening on")
args = parser.parse_args()
client = udp_client.SimpleUDPClient(args.ip, args.port)
    # define a callback function

@receiver.listen_on('universe', universe=1)  # listens on universe 1
def callback(packet):  # packet type: sacn.DataPacket
    data = packet.dmxData # print the received DMX data
    data = data[:9]
    Rcolor = data[0]
    Gcolor = data[1]
    Bcolor = data[2] 
    print(data)
    print(Rcolor)
    print(Gcolor)
    print(Bcolor)
    client.send_message("/avatar/parameters/Rcolor", float(Rcolor)/255)
    client.send_message("/avatar/parameters/Gcolor", float(Gcolor)/255)
    client.send_message("/avatar/parameters/Bcolor", float(Bcolor)/255)

# optional: if multicast is desired, join with the universe number as parameter
receiver.join_multicast(1)

time.sleep(10000)  # receive for 10 seconds

# optional: if multicast was previously joined
receiver.leave_multicast(1)

receiver.stop()