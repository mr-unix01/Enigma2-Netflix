# Enigma2-Netflix

Experimental Enigma2 plugin project for Dreambox Two running DreamOS / Newnigma2.

## Project status

**Research and compatibility testing — no working Netflix playback yet.**

Verified on the target receiver:
- Enigma2 loads and registers `WidevineProcessor` (`Registered factory: WidevineProcessor`).
- `dreamwidevine` daemon starts and listens on `/var/run/widevine_socket`.
- The Widevine CDM library is present.
- GStreamer 1.10.4 exposes `dashdemux` for MPEG-DASH.

These checks **do not establish Netflix compatibility**. Netflix playback may require supported authentication, device provisioning/certification, and a compatible DRM/video pipeline.

## Planned milestones

1. Validate playback of a publicly available, unencrypted MPEG-DASH test stream in Enigma2.
2. Validate an authorized Widevine-protected test stream and license workflow.
3. Determine whether Netflix authentication and playback can be supported on this hardware without bypassing DRM or access controls.
4. If feasible, implement a remote-control-friendly Enigma2 interface and Debian package.

## Target platform

- Dreambox Two, ARM64
- DreamOS / Newnigma2
- Enigma2 StreamServices and WidevineProcessor

## License

GPL-3.0. This project is unofficial and is not affiliated with or endorsed by Netflix.
