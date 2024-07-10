#!/usr/bin/env python3
# coding=utf-8
import sys
import inkex
from lxml import etree
import random
import math
 
def generation_CHEIIINHKA(a,x,y,l,s,n,k):
    if n>0:
        for i in range(k):
            an=6.28/k*i
            xn=x+math.cos(an)*l
            yn=y-math.sin(an)*l
            s=s+" M " + str(xn) + "," + str(yn)+ " L " + str(x) + "," + str(y)   
            s=s+generation_CHEIIINHKA(an,xn,yn,l//3,'',n-1,k)
    return s
        
def draw_CHEIIINHKA(x,y,l,n,grp,k):
    style = {"stroke": "#000000", "stroke-width": '1px', "fill": "none"}
    elem = grp.add(inkex.PathElement())
    elem.update(
        **{
            "style": style,
            "inkscape:label": 'snow',
            "d": generation_CHEIIINHKA(6.28,x,y,l,'',n,k)
        }
    )
    return elem
    

class CHEIIINHKA(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--n", type=int, default=3.0, help="Глубина рекурсии")
        pars.add_argument("--l", type=float, default=100.0, help="Длина ветки")
        pars.add_argument("--x", type=float, default=100.0, help="X центра")
        pars.add_argument("--y", type=float, default=100.0, help="Y центра")
        pars.add_argument("--k", type=int, default=6.0, help="Количество веток")

    def effect(self):
        grp = self.svg.get_current_layer()
        x = self.svg.unittouu(str(self.options.x) + 'px')
        y = self.svg.unittouu(str(self.options.y) + 'px')
        l = self.svg.unittouu(str(self.options.l) + 'px')
        n = self.options.n
        k = self.options.k
        draw_CHEIIINHKA(x,y,l,n,grp,k)

if __name__ == "__main__":
    CHEIIINHKA().run()
