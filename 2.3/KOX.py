#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
import math

def generation_KOX(x,y,l,n, grp):
    s=""
    if n == 0:
        draw_KOX(l, x, y, grp)
    else:
        s = s + generation_KOX(x-(l/2), y+(l/2), l/2, n-1, grp)
        s = s + generation_KOX(x+(l/2), y+(l/2), l/2, n-1, grp)
        s = s + generation_KOX(x+(l/2), y-(l/2), l/2, n-1, grp)
        s = s + generation_KOX(x-(l/2), y-(l/2), l/2, n-1, grp)
    return s
def draw_KOX(cur, d):
    style = {'stroke': '#000000', 'stroke-width': '1', 'fill': 'none'}
    elem = cur.add(inkex.PathElement())
    elem.update(
        **{
            "style": style,
            "inkscape:label": 'KOX',
            "d": d
        }
    )
    return elem
class KOX(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--n", type=int, default=3.0, help="Глубина рекурсии")
        pars.add_argument("--l", type=float, default=600.0, help="Сторона снежинки")
        pars.add_argument("--x", type=float, default=100.0, help="X центра")
        pars.add_argument("--y", type=float, default=600.0, help="Y центра")
        self.__pos =[0,0]
        self.__heading = 0
        self.__path = ""
        self.__draw = True
        self.__new = True
    def forward(self, mag):
        self.setpos((self.__pos[0] + math.cos(math.radians(self.__heading)) * mag,
        self.__pos[1] + math.sin(math.radians(self.__heading)) * mag))
    def right(self, deg):
        self.__heading -= deg
    def left(self, deg):
        self.__heading += deg
    def setpos(self, arg):
        if self.__new:
            self.__path += "M" + ",".join([str(i) for i in self.__pos])
            self.__new = False
        self.__pos = arg
        if self.__draw:
            self.__path += "L" + ",".join([str(i) for i in self.__pos])
    def getPath(self):
        return self.__path
    def KOX_curve(self, l, n):
        if n == 0:
            self.forward(l)
        else:
            self.KOX_curve(l/3, n-1)
            self.left(60)
            self.KOX_curve(l/3, n-1)
            self.right(120)
            self.KOX_curve(l/3, n-1)
            self.left(60)
            self.KOX_curve(l/3, n-1)
    def drawer_KOX(self,l, n):
        for i in range(3):
            self.KOX_curve(l, n)
            self.right(120)
    def effect(self):
        grp = self.svg.get_current_layer()
        x = self.svg.unittouu(str(self.options.x) + 'px')
        y = self.svg.unittouu(str(self.options.y) + 'px')
        l = self.svg.unittouu(str(self.options.l) + 'px')
        n = self.options.n
        self.__pos =[x,y]
        self.drawer_KOX(l,n)
        d = self.getPath()
        draw_KOX(grp, d)

if __name__ == '__main__':
    KOX().run()
