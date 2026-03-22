from stub_mesh_interface import StubMeshInterface
import meshbot


def test_test_1_hop():

    meshbot.start()

    mesh_interface = StubMeshInterface(hop_count=1)

    try:
        rx = mesh_interface.sendAndReceive("Test")

        assert rx is not None

        observed = rx.decoded.payload
        expected = b"MN: Received after 1 hop.\nSNR 55.55dB  RSSI -77dBm"

        assert observed == expected

    finally:
        mesh_interface.close()


def test_test_2_hops():

    meshbot.start()

    mesh_interface = StubMeshInterface()

    try:
        rx = mesh_interface.sendAndReceive("Test")

        assert rx is not None

        observed = rx.decoded.payload
        expected = b"MN: Received after 2 hops.\nSNR 55.55dB  RSSI -77dBm"

        assert observed == expected

    finally:
        mesh_interface.close()
