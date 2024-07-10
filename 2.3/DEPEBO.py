#!/usr/bin/env python3
# coding=utf-8
import sys
import inkex
import math
import random
from random import randint
pi = math.pi

def generate_DEPEBO(a0, a, x, y, l, parent):
    a1 = a0 + a / 2
    a2 = a0 - a / 2
    a3 = a0

    x1 = x + math.cos(a1) * l
    y1 = y - math.sin(a1) * l
    x2 = x + math.cos(a2) * l
    y2 = y - math.sin(a2) * l
    x3 = x + math.cos(a0) * l
    y3 = y - math.sin(a0) * l

    group = parent.add(inkex.Group())
    elem1 = group.add(inkex.PathElement())

    elem1.update(
        **{
            "style": {"stroke": "#8B4513", "stroke-width": 2, "fill": "none"},
            "inkscape:label": 'DEPEBO',
            "d": ' M ' + str(x1) + ',' + str(y1) + ' L ' + str(x) + ',' + str(y) + ' L ' + str(x2) + ',' + str(y2) + ' M ' + str(x) + ',' + str(y) + ' L ' + str(x3) + ',' + str(y3)
        }
    )

    if l > 2:
        generate_DEPEBO(a1, (3/4) * a, x1, y1, random.randint(0, int(l)), group)
        generate_DEPEBO(a2, (3/4) * a, x2, y2, random.randint(0, int(l)), group)
        generate_DEPEBO(a3, (3/4) * a, x3, y3, random.randint(0, int(l)), group)
    else:
        elem2 = group.add(inkex.PathElement())
        elem2.update(
            **{
                "style": {"stroke": "Orange", "stroke-width": 2, "fill": "Orange"},
                "inkscape:label": 'DEPEBO',
                "d": ' M ' + str(x+1) + ',' + str(y) + ' L ' + str(x+2) + ',' + str(y-2) + ' L ' + str(x) + ',' + str(y-1) + ' L ' + str(x-2) + ',' + str(y-2) + ' L ' + str(x-1) + ',' + str(y) + ' L ' + str(x-1) + ',' + str(y+2) + ' L ' + str(x) + ',' + str(y+1) + ' L ' + str(x+2) + ',' + str(y+2) + 'z'
            }
        )

def draw_DEPEBO(x, y, parent, l):
    group = generate_DEPEBO(pi/2, random.uniform(0.1, pi/2), x, y, l, parent)


    elem = parent.add(inkex.PathElement())
    elem.update(
        **{
            "style": {"stroke": "#8B4513", "stroke-width": 4, "fill": "none"},
            "inkscape:label": 'DEPEBO',
            "d": ' M ' + str(x) + ',' + str(y) + ' L ' + str(x) + ',' + str(y+l)
        }
    )

    return group, elem
    
  
class DEPEBO(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--x", type=float, default=100.0, help="X центра")
        pars.add_argument("--y", type=float, default=100.0, help="Y центра")
        pars.add_argument("--l", type=float, default=100.0, help="Длина ветви")

    def effect(self):
        grp = self.svg.get_current_layer()
        x = self.svg.unittouu(str(self.options.x) + 'px')
        y = self.svg.unittouu(str(self.options.y) + 'px')
        l = self.svg.unittouu(str(self.options.l) + 'px')

        
        draw_DEPEBO(x, y, grp, l)

if __name__ == "__main__":
    DEPEBO().run()
