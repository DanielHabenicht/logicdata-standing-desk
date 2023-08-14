# logicdata-standing-desk

This repository is about reverse engineering a standing desk from Kinnarps.
It applies to all hight adjustable tables with the [`LOGICDATA COMPACT-e-2L-O-V-EU Revision 2/1.9.14`](/hardware/main_unit.png) main units with the controller [`LOGICDATA HSF MDF 4M4 Rev3`](/hardware/controller_2.png) (click the link for pictures).

The controller and main unit are connected via a `MAS 70S DIN` connector.
It has the following layout:

By hooking up a logic analyzer the following functions could be recorded (see records folder for raw files from [Salea Logic Analyzer](https://www.saleae.com/downloads/)).

| Line   | Name    | Description                                                        |
| ------ | ------- | ------------------------------------------------------------------ |
| SHIELD | GND     | Ground                                                             |
| 0      | SERIAL  | Serial communication for the display (height)                      |
| 1      | -       | No function recorded                                               |
| 2      | SIGNAL1 | Different functions.                                               |
| 3      | SIGNAL2 | Different functions.                                               |
| 4      | SIGNAL3 | Different functions.                                               |
| 5      | TOGGLE  | Function toggle for other lines (HIGH - UP/DOWN or LOW - FUNCTION) |
| 6      | Vcc     | Voltage supply                                                     |

Depending on the `TOGGLE` line the other lines have different functions.

| TOGGLE | SIGNAL1 (line 2) | SIGNAL2 (line 3) | SIGNAL3 (line 4) | Description          |
| ------ | ---------------- | ---------------- | ---------------- | -------------------- |
| HIGH   | HIGH             | LOW              | -                | Button Down          |
| HIGH   | LOW              | HIGH             | -                | Button Up            |
| LOW    | LOW              | HIGH             | LOW              | Button position 1    |
| LOW    | HIGH             | LOW              | LOW              | Button position 2    |
| LOW    | HIGH             | LOW              | HIGH             | Button position 3    |
| LOW    | LOW              | HIGH             | HIGH             | Button position 4    |
| HIGH   | LOW              | LOW              | HIGH             | Button position save |

# Discussion about Logicdata Desks

https://web.archive.org/web/20230812201115/https://www.mikrocontroller.net/topic/373579

# Other projects

https://github.com/phord/RoboDesk
https://github.com/davidknezic/desk
