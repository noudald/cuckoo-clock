"""Cuckoo Clock - cuckoo-clock.py

Created by Noud Aldenhoven, september 2012

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import time
import pygame
import sys

def playcuckoo(n):
    pygame.init()

    i = 0
    while i < n:
        pygame.mixer.Sound('kukuklok.wav').play()
        print "KUKU..."
        time.sleep(1)
        i = i+1

    return 0

while True:
    if time.localtime()[4] == 0:
        playcuckoo(time.localtime()[3]%12)
        time.sleep(60)
    time.sleep(1)
    a, b, c = time.localtime()[3:6]
    sys.stdout.write("%i:%2i:%2i       \r" % (a,b,c))
    sys.stdout.flush()
