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
                        'marker' : '*',
                        'linestyle': '-'
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
                ? 'errorbars': [
                    {
                        'x' : [],
                        'x-error': [],
                        'y-error': [],
                        'y' : [],
                        'label' : 'Example label',
                        'c' : 'red',
                        'marker' : '*',
                        
                    }                    
                ],
                'title' : '',
                'xlabel' : '',
                'ylabel' : '',
                'ylim': [],
                'labelsize' : 12,
                'legend' : True,
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
    'save' : True,
    'name' : 'test',
    'path' : ''
}

Where 'data' is a dictionary for a single figure. It can be used to
create several subfigures and several lines per subfigure.

@author: bobz
"""
import json
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
    plt.rc('text.latex', preamble=r'\usepackage{sfmath}\usepackage{siunitx}\usepackage{wasysym}')

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
        
        ax2 = {}
            
        if 'lines' in p:
            for l in p['lines']:
                x = l['x']
                y = l['y']
                if 'linestyle' not in l:
                    linestyle = '-'
                else:
                    linestyle = l['linestyle']
                # markers_on = [0]
                if 'ylabel2' in l:
                    ax2 = ax[i,j].twinx()
                    ax2.plot(x,y, 
                                 color = l['color'],
                                 marker = l['marker'],
                                 label = l['label'],
                                 linestyle = linestyle,
                                 # markevery=markers_on
                                 )
                    ax2.legend(loc="upper right")
                else:
                    ax[i,j].plot(x,y, 
                                     color = l['color'],
                                     marker = l['marker'],
                                     label = l['label'],
                                     linestyle = linestyle,
                                     # markevery=markers_on
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

        if 'errorbars' in p:
            for l in p['errorbars']:
                x = l['x']
                y = l['y']
                ax[i,j].errorbar(x,y,
                                xerr=l['x-error'],
                                yerr=l['y-error'],
                                label=l['label'],
                                fmt = 'x',
                                capsize=5
                )
        if 'texts' in p:
            for text in p['texts']:
                x = text['x']
                y = text['y']
                ax[i,j].text(x,y,
                             text['text']
                )        
        if 'ylim' in p:
            ax[i,j].set_ylim(p['ylim'])
        
        if 'xlim' in p:
            ax[i,j].set_xlim(p['xlim'])
            
        ax[i,j].set_xlabel(p['xlabel'], fontdict=font)
        ax[i,j].set_ylabel(p['ylabel'], fontdict=font)
        
        if 'ylabel2' in p:
            ax2.set_ylabel(p['ylabel2'], fontdict=font)
            
        ax[i,j].set_title(p['title'], fontdict=font_title)
        ax[i,j].tick_params(labelsize = p['labelsize'])
        
        if p['legend']:
            ax[i,j].legend(loc='upper left',prop=font_legend)
            # ax[i,j].legend(loc='best',prop=font_legend)
        
        if p['grid']:
            ax[i,j].grid()
            
    if 'suptitle' in data:
        fig.suptitle(data['suptitle'])
    
    if data['save']:
        location = data['path'] + data['name']
    
        fig.savefig(location+'.eps', format='eps')
        fig.savefig(location+'.png', format='png')
        
        with open(location + '.json', 'w') as f:
            json.dump(data, f, indent = 2)
        
        
def plotter_json(fileLocator):
    with open(fileLocator, "r") as f:
        data = json.load(f)
    plotter(data)    