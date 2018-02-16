
import os
import platform


class settings(object):

    def __init__(self):

        self.set_paths()


    def set_paths(self):

        self.root = r'C:\Users\u0116961\Documents\CLSM'

        domain = 'SMAP_EASEv2_M36'

        self.mp_root = os.path.join(self.root, 'model_parameters', domain)
        self.mp_paths = {'tile_info': os.path.join(self.mp_root, 'til', 'SMAP_EASEv2_M36_964x406.til'),
                         'catchment': os.path.join(self.mp_root,'clsm','catchment.def'),
                         'tau_param': os.path.join(self.mp_root, 'clsm', 'tau_param.dat'),
                         'ts': os.path.join(self.mp_root, 'clsm', 'ts.dat'),
                         'bf': os.path.join(self.mp_root, 'clsm', 'bf.dat'),
                         'ar': os.path.join(self.mp_root, 'clsm', 'ar.new'),
                         'soil_param': os.path.join(self.mp_root, 'clsm', 'soil_param.dat'),
                         }

