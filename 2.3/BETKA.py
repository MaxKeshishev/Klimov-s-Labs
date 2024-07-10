#!/usr/bin/env python3
# coding=utf-8
import sys
import inkex
from lxml import etree
import random
import math

def generation_tree(a0,a,x,y,l,s,n):
    if n>0:
        a1=a0+a/2
        a2=a0-a/2
        a3=a0
        x1=x+math.cos(a1)*l
        y1=y-math.sin(a1)*l
        x2=x+math.cos(a2)*l
        y2=y-math.sin(a2)*l
        x3=x+math.cos(a3)*l
        y3=y-math.sin(a3)*l
        s=s+" M " + str(x1) + "," + str(y1)+ " L " + str(x) + "," + str(y) + " L " + str(x2) + "," + str(y2)
        s=s+" M " + str(x3) + "," + str(y3)+ " L " + str(x) + "," + str(y)  
        s=s+generation_tree(a1,a-a/4,x1,y1,l//2,'',n-1)
        s=s+generation_tree(a2,a-a/4,x2,y2,l//2,'', n-1)
        s=s+generation_tree(a3,a-a/4,x3,y3,l//2,'', n-1)
    return s
        
def draw_BETKA(x,y,l,a0,a,n,grp):
    style = {"stroke": "#000000", "stroke-width": '1px', "fill": "none"}
    elem = grp.add(inkex.PathElement())
    elem.update(
        **{
            "style": style,
            "inkscape:label": 'BETKA',
            "d": generation_tree(3.14/2,3.14/2,x,y,l,'',n)
        }
    )
    
    elem1 = grp.add(inkex.PathElement())
    elem1.update(
            **{
                "style": style,
                "inkscape:label": 'BETKA',
                "d": " M " + str(x) + "," + str(y)+ " L " + str(x) + "," + str(y+l)
            }
    )
    return elem
    return elem1

           

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
        draw_BETKA(x,y,l,3.14/2,3.14/2,n,grp)

if __name__ == "__main__":
    BETKA().run()
