
import os

import numpy as np

from pyclsm.paths import paths

class templates(object):

    @staticmethod
    def get_mp_template(param):

        if param == 'tile_info':
            hdr, fields = 7, ['type', 'pfaf_code', 'lon', 'lat', 'ig', 'jg', 'cell_frac', 'pfaf_index']

        elif param == 'catchment_info':
            hdr, fields = 0, ['tile_index', 'pfaf_code', 'min_lon', 'max_lon', 'min_lat', 'max_lat', 'mean_elev']

        else:
            print 'No template found for "' + param + '".'
            hdr, fields = (None, None)

        return hdr, fields


