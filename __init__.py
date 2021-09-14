from .hatchet_vis import Roundtrip

# Function to make module loading possible
def load_ipython_extension(ipython):
    ipython.register_magics(Roundtrip)
    