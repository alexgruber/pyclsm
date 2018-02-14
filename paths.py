
import os
import platform

class paths(object):

    def __init__(self, root=None, domain=None):

        if root is None:
            sys = 'win' if platform.system() == 'Windows' else 'lnx'
            if sys == 'win':
                # default path for local copies on a windows machine
                self.root = r'C:\Users\u0116961\Documents\CLSM'
            else:
                # default path on the HPC
                self.root = '/scratch/leuven/320/vsc32046/output/CLSM'

        if domain is None:
            domain = 'SMAP_EASEv2_M36'

        self.mp_root = os.path.join(self.root, 'model_parameters', domain)

        self.mp_paths = {'tile_info': os.path.join(self.mp_root, 'til', 'SMAP_EASEv2_M36_964x406.til'),
                         'catchment_info': os.path.join(self.mp_root,'clsm','catchment.def')}

