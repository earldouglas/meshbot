from stub_mesh_interface import StubMeshInterface
import meshbot


def test_hello():

    meshbot.start()

    mesh_interface = StubMeshInterface()

    try:
        observed = mesh_interface.sendAndReceive("Hello")
        expected = None
        assert observed == expected
    finally:
        mesh_interface.close()
