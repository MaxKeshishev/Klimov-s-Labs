#!/usr/bin/env python
# coding=utf-8
import sys
import inkex
from lxml import etree
def draw_SVG_ornament(ct, hg, wg, parent):
    xk = wg / 100
    yk = hg / 100
    style = {'fill': '#C20030'}
    for i in range (0, ct):
        elem = parent.add(inkex.PathElement())
        elem.update(**{
            'style': style,
            'inkscape:label': 'Ornament',
            'd': 'M ' + str(0*xk + wg*i) + ',' + str(0*yk) +
            'M ' + str(100*xk + wg*i) + ',' + str(100*yk) +
            'M ' + str(10*xk + wg*i) + ',' + str(10*yk) +
            ' L ' + str(40*xk + wg*i) + ',' + str(10*yk) +
            ' L ' + str(40*xk + wg*i) + ',' + str(30*yk) +
            ' L ' + str(50*xk + wg*i) + ',' + str(30*yk) +
            ' L ' + str(50*xk + wg*i) + ',' + str(10*yk) +
            ' L ' + str(60*xk + wg*i) + ',' + str(10*yk) +
            ' L ' + str(60*xk + wg*i) + ',' + str(30*yk) +
            ' L ' + str(70*xk + wg*i) + ',' + str(30*yk) +
            ' L ' + str(70*xk + wg*i) + ',' + str(10*yk) +
            ' L ' + str(90*xk + wg*i) + ',' + str(10*yk) +
            ' L ' + str(90*xk + wg*i) + ',' + str(20*yk) +
            ' L ' + str(80*xk + wg*i) + ',' + str(20*yk) +
            ' L ' + str(80*xk + wg*i) + ',' + str(80*yk) +
            ' L ' + str(90*xk + wg*i) + ',' + str(80*yk) +
            ' L ' + str(90*xk + wg*i) + ',' + str(90*yk) +
            ' L ' + str(70*xk + wg*i) + ',' + str(90*yk) +
            ' L ' + str(70*xk + wg*i) + ',' + str(70*yk) +
            ' L ' + str(60*xk + wg*i) + ',' + str(70*yk) +
            ' L ' + str(60*xk + wg*i) + ',' + str(90*yk) +
            ' L ' + str(50*xk + wg*i) + ',' + str(90*yk) +
            ' L ' + str(50*xk + wg*i) + ',' + str(70*yk) +
            ' L ' + str(40*xk + wg*i) + ',' + str(70*yk) +
            ' L ' + str(40*xk + wg*i) + ',' + str(90*yk) +
            ' L ' + str(10*xk + wg*i) + ',' + str(90*yk) +
            ' L ' + str(10*xk + wg*i) + ',' + str(70*yk) +
            ' L ' + str(20*xk + wg*i) + ',' + str(70*yk) +
            ' L ' + str(20*xk + wg*i) + ',' + str(80*yk) +
            ' L ' + str(30*xk + wg*i) + ',' + str(80*yk) +
            ' L ' + str(30*xk + wg*i) + ',' + str(60*yk) +
            ' L ' + str(40*xk + wg*i) + ',' + str(60*yk) +
            ' L ' + str(40*xk + wg*i) + ',' + str(40*yk) +
            ' L ' + str(30*xk + wg*i) + ',' + str(40*yk) +
            ' L ' + str(30*xk + wg*i) + ',' + str(20*yk) +
            ' L ' + str(20*xk + wg*i) + ',' + str(20*yk) +
            ' L ' + str(20*xk + wg*i) + ',' + str(30*yk) +
            ' L ' + str(10*xk + wg*i) + ',' + str(30*yk) +
            ' z'
            })
    return elem

class ornament(inkex.EffectExtension):
    def add_arguments(self, pars):
        pars.add_argument("--number", type = int, default = 10, help="Number of rapports")
        pars.add_argument("--height", type = float, default = 100.0, help="Height")
        pars.add_argument("--weight", type = float, default = 100.0, help="Weight")
    def effect(self):
        centre = self.svg.namedview.center
        grp_transform = 'translate' + str(centre)
        grp_name = 'Group Name'
        grp_attribs = {inkex.addNS('label', 'inkscape'): grp_name, 'transform': grp_transform}
        grp = self.svg.get_current_layer()
        ct = self.options.number
        hg = self.svg.unittouu(str(self.options.height) + 'px')
        wg = self.svg.unittouu(str(self.options.weight) + 'px')
        draw_SVG_ornament(ct,hg,wg,grp)
        
if __name__ == '__main__':
    ornament().run()
