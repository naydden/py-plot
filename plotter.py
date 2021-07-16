#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:38:31 2020

Input to functions should be a python dictionary with the following example
format:

data =  {
    'globals:': {
        'font': {
                'family': 'sans-serif',
                'color':  'black',
                'weight': 'normal',
                'size': 10,
        },
        'font_title':  {
                'family': 'sans-serif',
                'color':  'black',
                'weight': 'normal',
                'size': 12,
        },
        'font_legend':  {
                'family': 'sans-serif',
                'color':  'black',
                'weight': 'normal',
                'size': 8,
        }
    },
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
                ? 'texts': [
                    {
                         'annotate': False,
                         'x': 2,
                         'y': 200,
                         'text': 'stable',
                         'rotation': 0                               
                     },
                ],
                'title' : '',
                'description': '',
                'xlabel' : '',
                'ylabel' : '',
                'ylim': [],
                'xlim': [],
                'labelsize' : 12,
                'legend' : 'best',
                'legend-title': 'Legend title here or empty',
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
import json, os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



# GLOBALS

font_title = {
    'family': 'sans-serif',
    'color':  'black',
    'weight': 'normal',
    'size': 12,
}

font_g = {
    'family': 'sans-serif',
    'color':  'black',
    'weight': 'normal',
    'size': 11,
}

font_legend = {
    'family': 'sans-serif',
    'weight': 'normal',
    'size': 10,
}

def global_init(font={'family' : 'sans-serif', 'size' : 14}):
    plt.rc('text', usetex=True)
    plt.rc('font', family=font['family'], size=font['size'])
    plt.rc('text.latex', preamble=r'\usepackage{sfmath}\usepackage{siunitx}\usepackage{wasysym}')
    plt.rcParams['figure.constrained_layout.use'] = True

def plotter(data):
    global_init()
    nrows = data['nrows']
    ncols = data['ncols']

    font_l = {}
    font_legend_l = {}
    font_title_l = {}
    
    if 'globals' in data:
        font_l = data['globals']['font']
        font_legend_l = data['globals']['font_legend']
        font_title_l = data['globals']['font_title']
        
        global_init(font_l)
        
    else: 
        font_l = font_g
        font_legend_l = font_legend
        font_title_l = font_title
        
    
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
                    
                    ax2.legend(loc="upper right", prop=font_legend_l)
                else:
                    ax[i,j].plot(x,y, 
                                     color = l['color'],
                                     marker = l['marker'],
                                     label = l['label'],
                                     linestyle = linestyle,
                                     linewidth=1
                                     # markevery=markers_on
                     )
                    # ax[i,j].xaxis.set_major_locator(ticker.MultipleLocator(1))

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
                if text['annotate']:
                    xi = text['x']
                    yi = text['y']
                    xe = text['xe']
                    ye = text['ye']
                    ax[i,j].annotate('', xy=(xi, yi), xytext=(xe, ye),
                                     arrowprops=dict(arrowstyle="<-", facecolor='black'))   
                else:
                    x = text['x']
                    y = text['y']
                    ax[i,j].text(x,y,
                                 text['text'],
                                 rotation = text['rotation']
                    )
                
        if 'ylim' in p:
            ax[i,j].set_ylim(p['ylim'])
        
        if 'xlim' in p:
            ax[i,j].set_xlim(p['xlim'])
            
        ax[i,j].set_xlabel(p['xlabel'], fontdict=font_l)
        ax[i,j].set_ylabel(p['ylabel'], fontdict=font_l)
        
        if 'ylabel2' in p:
            ax2.set_ylabel(p['ylabel2'], fontdict=font_l)
          
        if 'title' in p:
            ax[i,j].set_title(p['title'], fontdict=font_title_l)
        ax[i,j].tick_params(labelsize = p['labelsize'])
        
        if 'legend' in p:
            if 'legend-title' in p:
                ax[i,j].legend(loc=str(p['legend']),prop=font_legend_l, title=p['legend-title'], title_fontsize=font_legend_l['size'])
            else:
                ax[i,j].legend(loc=str(p['legend']),prop=font_legend_l)
        
        if p['grid']:
            ax[i,j].grid()
            
    if 'suptitle' in data:
        fig.suptitle(data['suptitle'])
    
    if data['save']:
        if not os.path.exists(data['path']):
            os.makedirs(data['path'])
        location = data['path'] + data['name']
    
        fig.savefig(location+'.eps', format='eps')
        fig.savefig(location+'.svg', format='svg')
        fig.savefig(location+'.png', format='png')
        
        with open(location + '.json', 'w') as f:
            json.dump(data, f, indent = 2)
        
        
def plotter_json(fileLocator):
    global_init()
    with open(fileLocator, "r") as f:
        data = json.load(f)
    plotter(data)    