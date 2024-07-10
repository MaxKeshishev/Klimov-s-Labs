#!/usr/bin/env python3
# coding=utf-8
import sys
import inkex
from lxml import etree
import random
import math

def generation_tree(a0,x,y,l,s,n):
    if n>0:
        a1 = a0 + 3.14/3
        a2 = a1 + 3.14/3
        x1 = x + 2*l*math.cos(a1)
        y1 = y - 2*l*math.sin(a1)
        x2 = x + 2*l*math.cos(a2)
        y2 = y - 2*l*math.sin(a2)
        cx = (x + x + l*math.cos(a1) + x + l*math.cos(a2))/3
        cy = (y + y - l*math.sin(a1) + y - l*math.sin(a2))/3
        s = s + " M " + str(x) + "," + str(y) + " L " + str(x + l*math.cos(a1)) + "," + str(y - l*math.sin(a1)) + " L " + str(x + l*math.cos(a2)) + "," + str(y - l*math.sin(a2)) + " L " + str(x) + "," + str(y) + " L " + str(x2) + "," + str(y2) + " L " + str(x) + "," + str(y) + " L " + str(x1) + "," + str(y1)
        s = s + " M " + str(cx) + "," + str(cy) + " L " + str(cx) + "," + str(cy - l/8)
        s = s + " M " + str(cx) + "," + str(cy) + " L " + str(cx) + "," + str(cy + l/8)
        s = s + " M " + str(cx) + "," + str(cy) + " L " + str(cx + l/6) + "," + str(cy - l/8)
        s = s + " M " + str(cx) + "," + str(cy) + " L " + str(cx + l/6) + "," + str(cy + l/8)
        s = s + generation_tree(a0-3.14/6,x1,y1,l//2,'',n-1)
        s = s + generation_tree(a0+3.14/6,x2,y2,l//2,'', n-1)
    return s
        
def draw_BETKA(x,y,l,n,grp):
    style = {"stroke": "#000000", "stroke-width": '0.2px', "fill": "none"}
    elem = grp.add(inkex.PathElement())
    elem.update(
        **{
            "style": style,
            "inkscape:label": 'BETKA',
            "d": generation_tree(0,x,y,l,'',n)
        }
    )
    return elem

           

class BETKA(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--n", type=int, default=3.0, help="Глубина рекурсии")
        pars.add_argument("--l", type=float, default=100.0, help="Длина ветки")
        pars.add_argument("--x", type=float, default=100.0, help="Х центра")
        pars.add_argument("--y", type=float, default=100.0, help="Y центра")

    def effect(self):
        grp = self.svg.get_current_layer()
        x = self.svg.unittouu(str(self.options.x) + 'px')
        y = self.svg.unittouu(str(self.options.y) + 'px')
        l = self.svg.unittouu(str(self.options.l) + 'px')
        n = self.options.n
        draw_BETKA(x,y,l,n,grp)

if __name__ == "__main__":
    BETKA().run()
