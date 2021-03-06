from __future__ import unicode_literals
from fipy.solvers.scipy.linearPCGSolver import LinearPCGSolver as ScipyLinearPCGSolver
from fipy.solvers.pyAMG.preconditioners.smoothedAggregationPreconditioner import SmoothedAggregationPreconditioner

__all__ = ["LinearPCGSolver"]
from future.utils import text_to_native_str
__all__ = [text_to_native_str(n) for n in __all__]

class LinearPCGSolver(ScipyLinearPCGSolver):
    """
    The `LinearPCGSolver` is an interface to the PCG solver in Scipy,
    using the pyAMG `SmoothedAggregationPreconditioner` by default.
    """

    def __init__(self, tolerance=1e-15, iterations=2000, precon=SmoothedAggregationPreconditioner()):
        """
        :Parameters:
          - `tolerance`: The required error tolerance.
          - `iterations`: The maximum number of iterative steps to perform.
          - `precon`: Preconditioner to use.

        """

        super(LinearPCGSolver, self).__init__(tolerance=tolerance, iterations=iterations, precon=precon)
