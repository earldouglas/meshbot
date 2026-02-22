#!/usr/bin/env python3

from meshtastic.serial_interface import SerialInterface
from throttle import Throttle
import meshbot


def main() -> None:
    throttle = Throttle(SerialInterface(), 10)
    meshbot.start()
    throttle.join()
    throttle.mesh_interface.close()


if __name__ == "__main__":
    main()
