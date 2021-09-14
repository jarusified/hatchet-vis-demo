from .loader import Roundtrip

# Function to make module loading possible
def load_ipython_extension(ipython):
    ipython.register_magics(Roundtrip)
    

def main():
    """Entry point for the application script"""
    print("Call your main application code here")