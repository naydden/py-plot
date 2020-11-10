# py-plot

Repository containing handy plotting functions that can be used from other scripts. This will reduce the amount of boilerplate code and centralise plotting styles.

Input to functions should be a python dictionary with the following example format:


```javascript
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
    'save' : {
        'name' : 'test',
        'path' : ''
    }
}
```

Where 'data' is a dictionary for a single figure. It can be used to create several subfigures and several lines per subfigure.