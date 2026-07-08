"""
Regression Metrics

Comprehensive regression evaluation utilities for CircuitBench.

Modules
-------
error_metrics
goodness_of_fit
residuals
diagnostics
influence
uncertainty
benchmarking
reporting
"""

from . import error_metrics
from . import goodness_of_fit
from . import residuals
from . import diagnostics
from . import influence
from . import uncertainty
from . import benchmarking
from . import reporting

from .error_metrics import *
from .goodness_of_fit import *
from .residuals import *
from .diagnostics import *
from .influence import *
from .uncertainty import *
from .benchmarking import *
from .reporting import *

__version__ = "0.1.0"
