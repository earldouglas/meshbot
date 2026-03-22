from meshbot import Meshbot
from stub_mesh_interface import StubMeshInterface


def test_hello():

    meshbot = Meshbot(qth=None)
    meshbot.start()

    mesh_interface = StubMeshInterface()

    try:
        observed = mesh_interface.sendAndReceive("Hello")
        expected = None
        assert observed == expected
    finally:
        mesh_interface.close()
