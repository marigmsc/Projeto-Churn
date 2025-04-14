# Use relative imports (a single dot . means current package directory)
from .mainmodel import MainModel
from .LWTA import LWTA, Gsoftmax  # Be explicit if possible, avoid '*'
from .helper import *             # Or be explicit: from .helper import relevant_functions
from .model_wrapper import Num_Cat # Assuming Num_Cat is here

# Optional: Define __all__ to control what 'from STAB import *' imports
__all__ = ['MainModel', 'LWTA', 'Gsoftmax', 'Num_Cat'] # Add other necessary names
