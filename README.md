[![Build status](https://github.com/earldouglas/meshbot/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/earldouglas/meshbot/actions/workflows/build.yml)

MeshBot is a basic call-and-response bot for
[Meshtastic](https://meshtastic.org/) nodes.

## Features

<table>
<tr><th>Rx</th><th>Tx</th></tr>

<tr>
<td>
<pre>Ping</pre>
</td>
<td>
<pre>Pong</pre>
</td>
</tr>

<tr>
<td>
<pre>Test</pre>
</td>
<td>
<pre>3af5: Received after 2 hops.
SNR 11.75dB  RSSI -71dBm</pre>
</td>
</tr>

<tr>
<td>
<pre>Fortune</pre>
</td>
<td>
<pre>Let's call it an accidental feature.
	--Larry Wall</pre>
</td>
</tr>

</table>

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
