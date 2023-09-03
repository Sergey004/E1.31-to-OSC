# Description:

TL;DR: Now **you** walking RGB controller (Unfortunately with only one virtual light LED)

# Setup 

Install dependencies

```bash
$ pip install -r requirements.txt
```
OpenRGB setup

Don't forget enadle E1.31 protocol

![image](https://github.com/Sergey004/E1.31-to-OSC/assets/11889498/78d5cdbc-f4ae-4eea-a753-3697ff50e5bf)


Note: a "device" name can be absolutely any device name 

![image](https://github.com/Sergey004/E1.31-to-OSC/assets/11889498/22c15b11-c8d5-4521-ac1f-8706993e5195)


Next, it's up to your imagination to do whatever you want with this data.

Values transferred via OSC

|Var name|Type|Value|
|---|---|---|
|Rcolor|float|0-1|
|Gcolor|float|0-1|
|Bcolor|float|0-1|
