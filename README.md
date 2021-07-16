# py-plot

Repository containing handy plotting functions that can be used from other scripts. This will reduce the amount of boilerplate code and centralise plotting styles.

Input to functions should be a python dictionary with the following example format:


```javascript
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
```

Where 'data' is a dictionary for a single figure. It can be used to create several subfigures and several lines per subfigure.