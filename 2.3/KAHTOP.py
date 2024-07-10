#!/usr/bin/env python3
# coding=utf-8
import sys
import inkex
import random


def generate_KAHTOP(x, y, l, parent, n):
    if n>0:
        x1=x-l
        y1=y-l
        x2=x+l
        y2=y-l
        x3=x+l
        y3=y+l
        x4=x-l
        y4=y+l
        group = parent.add(inkex.Group())
        if l > 2:
            generate_KAHTOP(x1, y1, l//2, group, n-1)
            generate_KAHTOP(x2, y2, l//2, group, n-1)
            generate_KAHTOP(x3, y3, l//2, group, n-1)
            generate_KAHTOP(x4, y4, l//2, group, n-1)

        elem = group.add(inkex.PathElement())
        elem.update(
            **{
                "style": {"stroke": "#000000", "stroke-width": 1, "fill": "white"},
                "inkscape:label": 'KAHTOP',
                "d": ' M ' + str(x1) + ',' + str(y1) + ' L ' + str(x2) + ',' + str(y2) + ' L ' + str(x3) + ',' + str(y3) + ' L ' + str(x4) + ',' + str(y4) + 'z'
            }
        )
        
def draw_KAHTOP(x, y, parent, l, n):
    group = generate_KAHTOP(x, y, l, parent, n)
    return group

class KAHTOP(inkex.EffectExtension):
    def add_arguments(self, pars):		
        pars.add_argument("--n", type=int, default=3.0, help="Глубина рекурсии")
        pars.add_argument("--l", type=float, default=100.0, help="Сторона квадрата")
        pars.add_argument("--x", type=float, default=100.0, help="X центра")
        pars.add_argument("--y", type=float, default=100.0, help="Y центра")

    def effect(self):
        grp = self.svg.get_current_layer()
        l = self.svg.unittouu(str(self.options.l) + 'px')
        x = self.svg.unittouu(str(self.options.x) + 'px')
        y = self.svg.unittouu(str(self.options.y) + 'px')
        n = self.options.n
        draw_KAHTOP(x, y, grp, l, n)

if __name__ == "__main__":
    KAHTOP().run()
