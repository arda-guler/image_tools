rgb_contraster: assigns max (255) or min (0) values to
                RGB (and alpha if available) channels
                depending on whether their current value
                is higher than half (127).
				
rgb_contraster_shaded: 
                does what rgb_contraster does, but instead
                of raising the color value to max, it
                instead raises it to the pixel's brightness
                value
				
rgb_separator:  assigns max value to whichever color is
                the dominant one in a pixel. if multiple
                colors are equally dominant, their
                combination is used.
				
rgb_separator_shaded:
                does what rgb_separator does, but instead
                of raising the color value to max, it
                instead raises it to the pixel's brightness
                value
