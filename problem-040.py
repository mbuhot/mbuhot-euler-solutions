#! /usr/bin/env python3
d = "".join(str(i) for i in range(1,1000000+1))
print(int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999]))
