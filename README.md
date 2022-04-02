# RPMidi
A Raspberry Pi Pico MIDI Player, written in MicroPython.

## What is this, exactly?
This is a somewhat dysfunctional MIDI player for a Raspberry Pi Pico. TL;DR, it allows you to take MIDI files,
and shove them down your Raspberry Pi Pico's GPIO pins as PWM signals.

## Cool! How do I use it?
* Download the source code and extract it's contents onto your Raspberry Pi Pico.
Make sure that it's running MicroPython first. I would recommend using Thonny.
* Download a MIDI file (No more than 4 voices)!
* Shove your MIDI file into this converter: https://github.com/LenShustek/miditones
and add your song data in songs.py.
* See main.py for the rest!

## GPIO defaults
GPIO Pins 6-9 are used by default.

* 6 -> Channel A0
* 7 -> Channel A1
* 8 -> Channel B0
* 9 -> Channel B1

Of course, since the Raspberry Pi Pico's pins are almost entirely PWM-friendly, you can remap this to whatever
pins you want in rpmidi.py (as long as they are PWM supported, which should'nt be a problem).

## Changelog
| Version | Info |
| ------- | ---- |
| v1.0 | Initial commit. |

## Known bugs
* If MIDI files have more than 4 voices, the MIDI timing will get borked.
* TODO: find more bugs

## Credits
Thanks to LenShustek for providing the [Miditones](https://github.com/LenShustek/miditones) converter, evilwombat for the [stm-bmc](https://github.com/evilwombat/stm-bmc)
project (Mainly inspiration for the default music), and the Raspberry Pi Foundation for creating the Raspberry Pi Pico!
