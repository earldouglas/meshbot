from stub_mesh_interface import StubMeshInterface
import meshbot


def test_ping():

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
