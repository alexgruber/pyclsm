

import pandas as pd

from pyclsm.templates import get_mp_template

from pyclsm.settings import settings


class CLSM(settings):

    def __init__(self):

        super(CLSM, self).__init__()

        self.load_model_parameters()
        self.load_forcing()

    def __getitem__(self, item):
        return getattr(self, item)


    def load_settings(self):
        pass

    def load_forcing(self):
        pass

    def load_model_parameters(self, params=None):

        if params is None:
            params = self.mp_paths.keys()

        for param in params:
            hdr, fields = get_mp_template(param)
            data = pd.read_csv(self.mp_paths[param], delim_whitespace=True, header=hdr, names=fields)

            self.__setattr__(param,data)


    def run(self, gpi):

        #use settings...
        runperiod = none

        # initialize first time step
        forcing = None # t
        prognostic = None # t-1
        diagnostic = None # t-1
        for t in runperiod:

            # run model
            prognostic = None # t
            diagnostic = None # t

            # get forcing
            forcing = None # t+1


            yield t, forcing, prognostic, diagnostic