

def get_mp_template(param):

    if param == 'tile_info':
        hdr, fields = 7, ['type', 'pfaf_code', 'lon', 'lat', 'ig', 'jg', 'cell_frac', 'pfaf_index']

    elif param == 'catchment':
        hdr, fields = 0, ['tile_index', 'pfaf_code', 'min_lon', 'max_lon', 'min_lat', 'max_lat', 'mean_elev']

    elif param == 'tau_param':
        hdr, fields = 0, ['tile_index', 'pfaf_code', 'atau2', 'btau2', 'atau5', 'btau5']

    elif param == 'ts':
        hdr, fields = 0, ['tile_index', 'pfaf_code', 'gnu', 'tsa1', 'tsa2', 'tsb1', 'tsb2']

    elif param == 'bf':
        hdr, fields = 0, ['tile_index', 'pfaf_code', 'gnu', 'bf1', 'bf2', 'bf3']

    elif param == 'ar':
        hdr, fields = 0, ['tile_index', 'pfaf_code', 'gnu', 'ars1', 'ars2', 'ars3', 'ara1', 'ara2', 'ara3', 'ara4',
                          'arw1', 'arw2', 'arw3', 'arw4' ]

    elif param == 'soil_param':
        hdr, fields = 0, ['tile_index', 'pfaf_code', 'soil_class_top', 'soil_class_com', 'BEE', 'PSIS', 'POROS',
                          'COND', 'WPWET', 'soildepth', 'gravel', 'OrgCarbon_top', 'OrgCarbon_rz', 'sand_top',
                          'clay_top', 'sand_rz', 'clay_rz', 'WPWET_top', 'POROS_top']

    else:
        print 'No template found for "' + param + '".'
        hdr, fields = (None, None)

    return hdr, fields





