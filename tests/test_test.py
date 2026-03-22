from meshbot import Meshbot
from stub_mesh_interface import StubMeshInterface


def test_test_1_hop():

    meshbot = Meshbot(qth=None)
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

    meshbot = Meshbot(qth=None)
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


def test_test_no_qth():

    meshbot = Meshbot(qth=None)
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


def test_test_some_qth():

    meshbot = Meshbot(qth="Testlandia")
    meshbot.start()

    mesh_interface = StubMeshInterface()

    try:
        rx = mesh_interface.sendAndReceive("Test")

        assert rx is not None

        observed = rx.decoded.payload
        expected = b"MN: Received in Testlandia after 2 hops.\nSNR 55.55dB  RSSI -77dBm"

        assert observed == expected

    finally:
        mesh_interface.close()
