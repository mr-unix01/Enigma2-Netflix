# Initial testing (Dreambox Two)

This is an **interface-only scaffold**, not a Netflix client. No authentication, network requests, DASH playback, or DRM license exchange is implemented.

## Target

- Dreambox Two (ARM64)
- DreamOS / Newnigma2 with Enigma2
- Python runtime provided by the receiver

## Before installing

1. Confirm the receiver's Python version and Enigma2 plugin API compatibility.
2. Back up any existing plugin directory.
3. Copy the `plugin/Plugins/Extensions/Enigma2Netflix` directory into `/usr/lib/enigma2/python/Plugins/Extensions/` only after reviewing the code.
4. Restart Enigma2, not the whole receiver.
5. Open the plugin from the Plugins menu. Confirm that OK, EXIT, and BACK close the screen.

No installer or .deb is provided yet. Do not install on a production receiver without reviewing and testing.

## Verified platform prerequisites

- `WidevineProcessor` registered as an Enigma2 stream processor factory.
- `dreamwidevine` service started and listening on its UNIX socket.
- GStreamer `dashdemux` available.

These checks do not prove Netflix support. Future playback testing must use authorized test media and licensing.
