#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:38:31 2020

Input to functions should be a python dictionary with the following example
format:

data =  {
    'plots' : [   
            {
                ?'lines' : [
                    {
                        'x' : [],
                        'y' : [],
                        'label' : 'Example label',
                        'color' : 'red',
                        'marker' : '*'
                    }
                ],
                ?'scatters': [
                    {
                        'x' : [],
                        'y' : [],
                        'label' : 'Example label',
                        'c' : 'red',
                        'marker' : '*'
                    }
                ],
                'title' : '',
                'xlabel' : '',
                'ylabel' : '',
                'labelsize' : 12,
                'grid' : True,
                'ij' : [0, 0]
            }
        ],
    'nrows' : 2,
    'ncols' : 1,
    'sharex' : False,
    'sharey' : True,
    ?'suptitle' : 'Global figure title',
    'figsize' : (8,6),
    'save' : {
        'name' : 'test',
        'path' : ''
    }
}

Where 'data' is a dictionary for a single figure. It can be used to
create several subfigures and several lines per subfigure.

@author: bobz
"""
import math, json
import numpy as np
import matplotlib.pyplot as plt


# GLOBALS

font_title = {
    'family': 'sans-serif',
    'color':  'black',
    'weight': 'normal',
    'size': 16,
}

font = {
    'family': 'sans-serif',
    'color':  'black',
    'weight': 'normal',
    'size': 14,
}

font_legend = {
    'family': 'sans-serif',
    'weight': 'normal',
    'size': 12,
}

def global_init():
    plt.rc('text', usetex=True)
    plt.rc('font', family='sans-serif', size=14)
    plt.rc('text.latex', preamble=[r'\usepackage{sfmath}',  r'\usepackage{siunitx}'])

def plotter(data):
    global_init()
    nrows = data['nrows']
    ncols = data['ncols']
    
    fig, ax = plt.subplots(
                            nrows,
                            ncols,
                            sharex = data['sharex'],
                            sharey = data['sharey'],
                            squeeze = False,
                            figsize = data['figsize']
    )
    
    
    for p in data['plots']:
        i = p['ij'][0]
        j = p['ij'][1]
        if 'lines' in p:
            for l in p['lines']:
                x = l['x']
                y = l['y']
                ax[i,j].plot(x,y, 
                                 color = l['color'],
                                 marker = l['marker'],
                                 label = l['label']
                )

        if 'scatters' in p:
            for l in p['scatters']:
                x = l['x']
                y = l['y']
                ax[i,j].scatter(x,y, 
                                    c = l['color'],
                                    marker = l['marker'],
                                    label = l['label']
                )
            
        
        ax[i,j].set_xlabel(p['xlabel'], fontdict=font)
        ax[i,j].set_ylabel(p['ylabel'], fontdict=font)
        ax[i,j].set_title(p['title'], fontdict=font_title)
        ax[i,j].tick_params(labelsize = p['labelsize'])
        
        if p['grid']:
            ax[i,j].grid()
            
    if 'suptitle' in data:
        fig.suptitle(data['suptitle'])
    
    location = data['save']['path'] + data['save']['name']
    
    fig.savefig(location+'_eps', format='eps')
    fig.savefig(location+'_png', format='png')
    
    with open(location + '.json', 'w') as f:
        json.dump(data, f, indent = 2)