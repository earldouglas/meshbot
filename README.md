MeshBot is a basic call-and-response bot for
[Meshtastic](https://meshtastic.org/) nodes.

## Features

### Ping

* Rx: `Ping`
* Tx: `Pong`

## Usage

Make sure our radio's serial interface is enabled under `Settings` ->
`Security` -> `Serial console`, then connect it to your computer via
USB.

Build Meshbot with `nix-build`:

```sh
$ nix-build
```

Run the resulting script:

```sh
./result/bin/meshbot
```
