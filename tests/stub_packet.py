from meshtastic.protobuf.mesh_pb2 import MeshPacket


def stub_packet(my_node_num: int, payload: str) -> MeshPacket:

    packet: MeshPacket = MeshPacket()

    all = 0xFFFFFFFF

    setattr(packet, "from", my_node_num)
    packet.to = all
    packet.channel = 1
    packet.decoded.portnum = "TEXT_MESSAGE_APP"
    packet.decoded.payload = f"{payload}".encode("ASCII")
    packet.decoded.bitfield = 1
    packet.id = 3333333333
    packet.rx_time = 1234567890
    packet.rx_snr = 55.55
    packet.hop_limit = 6
    packet.rx_rssi = -77
    packet.hop_start = 8
    packet.relay_node = 99
    packet.transport_mechanism = "TRANSPORT_LORA"

    return packet
