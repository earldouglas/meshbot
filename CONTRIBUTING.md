## Example packets

### DM packet

```
{
  'from': 111111111,
  'to': 2222222222,
  'decoded': {
    'portnum': 'TEXT_MESSAGE_APP',
    'payload': b'Test DM',
    'bitfield': 1,
    'text': 'Test DM'
  },
  'id': 3333333333,
  'rxTime': 4444444444,
  'rxSnr': 55.5,
  'hopLimit': 6,
  'wantAck': True,
  'rxRssi': -77,
  'hopStart': 8,
  'publicKey': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=',
  'pkiEncrypted': True,
  'relayNode': 99,
  'transportMechanism': 'TRANSPORT_LORA',
  'fromId': '!aaaaaaaa',
  'toId': '!bbbbbbbb'
}
```

### Broadcast packet

```
{
  'from': 111111111,
  'to': 2222222222,
  'channel': 1,
  'decoded': {
    'portnum': 'TEXT_MESSAGE_APP',
    'payload': b'Test channel 1',
    'bitfield': 1,
    'text': 'Test channel 1'
  },
  'id': 3333333333,
  'rxTime': 4444444444,
  'rxSnr': 55.55,
  'hopLimit': 6,
  'rxRssi': -77,
  'hopStart': 8,
  'relayNode': 99,
  'transportMechanism': 'TRANSPORT_LORA',
  'fromId': '!aaaaaaaa',
  'toId': '^all'
}
```

## References

* <https://python.meshtastic.org/mesh_interface.html>
* <https://python.meshtastic.org/serial_interface.html>
