# Code used from: https://studywolf.wordpress.com/2017/11/21/matplotlib-legends-for-mean-and-confidence-interval-plots/
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
from matplotlib.colors import colorConverter as cc

class LegendObject(object):
    def __init__(self, facecolor='red', edgecolor='white', line_flag=False, line_color='black', dashed=False):
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.line_flag = line_flag
        self.line_color = line_color
        self.dashed = dashed
 
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpatches.Rectangle(
            # create a rectangle that is filled with color
            [x0, y0], width, height, facecolor=self.facecolor,
            # and whose edges are the faded color
            edgecolor=self.edgecolor, lw=2.5)
        handlebox.add_artist(patch)

        if self.line_flag:
            if self.dashed:
                line = mlines.Line2D([x0, x0+width], [y0+height/2, y0+height/2], color=self.line_color, linestyle='--', lw=2)
                handlebox.add_artist(line)
            else:
                line = mlines.Line2D([x0, x0+width], [y0+height/2, y0+height/2], color=self.line_color, lw=2)
                handlebox.add_artist(line)
 
        # if we're creating the legend for a dashed line,
        # manually add the dash in to our rectangle
        # if self.dashed:
        #     patch1 = mpatches.Rectangle(
        #         [x0 + 2*width/5, y0], width/5, height, facecolor=self.edgecolor,
        #         transform=handlebox.get_transform())
        #     handlebox.add_artist(patch1)
 
        return patch
    
class HatchedObject(object):
    def __init__(self, facecolor='None', edgecolor='gray', hatch='x', dashed=False):
        self.facecolor = facecolor
        self.edgecolor = edgecolor
        self.hatch = hatch
        self.dashed = dashed
 
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpatches.Rectangle(
            # create a rectangle that is filled with color
            [x0, y0], width, height, facecolor=self.facecolor,
            # and whose edges are the faded color
            edgecolor=self.edgecolor, hatch=self.hatch)
        handlebox.add_artist(patch)

        # if we're creating the legend for a dashed line,
        # manually add the dash in to our rectangle
        if self.dashed:
            line = mlines.Line2D([x0, x0+width], [y0+height/2, y0+height/2], color=self.edgecolor, linestyle='--', linewidth=2)
            handlebox.add_artist(line)
 
        return patch
    
class PatchObject(object):
    def __init__(self, facecolor='red', line_flag=False, line_color='black', dashed=False):
        self.facecolor = facecolor
        self.line_flag = line_flag
        self.line_color = line_color
        self.dashed = dashed
 
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        patch = mpatches.Rectangle(
            # create a rectangle that is filled with color
            [x0, y0], width, height, facecolor=self.facecolor, edgecolor=self.facecolor, lw=2)
        handlebox.add_artist(patch)

        if self.line_flag:
            if self.dashed:
                line = mlines.Line2D([x0, x0+width], [y0+height/2, y0+height/2], color=self.line_color, linestyle='--')
                handlebox.add_artist(line)
            else:
                line = mlines.Line2D([x0, x0+width], [y0+height/2, y0+height/2], color=self.line_color)
                handlebox.add_artist(line)
 
        return patch
    
class LineObject(object):
    def __init__(self, line_color='black', linewidth=1.5, linestyle='-'):
        self.line_color = line_color
        self.linewidth = linewidth
        self.linestyle = linestyle
 
    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
        x0, y0 = handlebox.xdescent, handlebox.ydescent
        width, height = handlebox.width, handlebox.height
        line = mlines.Line2D([x0, x0+width], [y0+height/2, y0+height/2], color=self.line_color, lw=self.linewidth, linestyle=self.linestyle)
        handlebox.add_artist(line)

bg = np.array([1, 1, 1])  # background of the legend is white