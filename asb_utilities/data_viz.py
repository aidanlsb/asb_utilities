def altair_theme():
    """
    This function defines an Altair theme.
    """
    # Typography
    title_font = 'Lato'
    label_font = 'Lato'
    font_color = '#000000'
    axis_color = '#000000'
    
    # Color schemes
    background_color = 'white'
    markColor = '#21C4FF' # Blue

    categorical_palette = [
        '#21C4FF', # Blue
        '#003459', # Prussian Blue
        '#C3CED0', # Gray
        '#D00000', # Boston Red
        '#FEC601', # Golden Poppy
    ]

    ordinal_palette = categorical_palette

    ramp_palette = [
        '#21C4FF', # Light Blue
        '#003459'   # Dark Blue
    ]

    diverging_palette = [
        '#21C4FF', # Blue
        '#FEC601', # Golden
        '#D00000' # Red
    ]

    return {
        'width': 685,
        'height': 380,
        'config': {
            'title': {
                'fontSize': 24,
                'anchor': 'middle',
                'fontColor': font_color,
                'font': title_font
            },
            'mark': {'color': markColor},
            'background': background_color,
            # 'arc': {'fill': markColor },
            # 'area': {'fill': markColor },
            # 'line': {'stroke': markColor },
            # 'path': { 'stroke': markColor },
            # 'rect': {'fill': markColor},
            # 'shape': {'stroke': markColor },
            # 'symbol': {'fill': markColor, 'size': 30 },
             'range': {
                'category': categorical_palette,
                'ordinal': ordinal_palette,
                'ramp': ramp_palette,
                'diverging': diverging_palette,
                'heatmap': diverging_palette,
            },
             'view': {
                'stroke': 'transparent'
            },
             'axisX': {
                'grid': False,
                'titleFont': title_font,
                'labelFont': label_font,
                'domainColor': axis_color,
                'tickColor': axis_color
            },
            'axisY': {
                'domain': False,
                'ticks': False,
                'titleFont': title_font,
                'labelFont': label_font,
                'gridDash': (4,2)
            }
        }
    }