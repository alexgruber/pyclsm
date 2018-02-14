

import pandas as pd

from pyclsm.paths import paths
from pyclsm.templates import templates


class CLSM(paths,templates):

    def __init__(self, domain=None):

        super(CLSM, self).__init__(domain=domain)

    def __getitem__(self, item):
        return getattr(self, item)

    def read_model_parameters(self, params=None):

        if params is None:
            params = ['tile_info', 'catchment_info']

        for param in params:
            hdr, fields = self.get_mp_template(param)
            data = pd.read_csv(self.mp_paths[param], delim_whitespace=True, header=hdr, names=fields)

            self.__setattr__(param,data)


