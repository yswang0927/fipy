#!/usr/bin/env python

## 
 # ###################################################################
 #  FiPy - Python-based finite volume PDE solver
 # 
 #  FILE: "parameters.py"
 #                                    created: 8/27/04 {10:29:10 AM} 
 #                                last update: 8/27/04 {4:01:07 PM} { 1:23:41 PM}
 #  Author: Jonathan Guyer
 #  E-mail: guyer@nist.gov
 #  Author: Daniel Wheeler
 #  E-mail: daniel.wheeler@nist.gov
 #    mail: NIST
 #     www: http://ctcms.nist.gov
 #  
 # ========================================================================
 # This software was developed at the National Institute of Standards
 # and Technology by employees of the Federal Government in the course
 # of their official duties.  Pursuant to title 17 Section 105 of the
 # United States Code this software is not subject to copyright
 # protection and is in the public domain.  PFM is an experimental
 # system.  NIST assumes no responsibility whatsoever for its use by
 # other parties, and makes no guarantees, expressed or implied, about
 # its quality, reliability, or any other characteristic.  We would
 # appreciate acknowledgement if the software is used.
 # 
 # This software can be redistributed and/or modified freely
 # provided that any derivative works bear some notice that they are
 # derived from it, and any modified versions bear some notice that
 # they have been modified.
 # ========================================================================
 #  
 #  Description: 
 # 
 #  History
 # 
 #  modified   by  rev reason
 #  ---------- --- --- -----------
 #  2003-11-17 JEG 1.0 original
 # ###################################################################
 ##

"""

This file keeps all the geometry and material properties necessary to
run a trench level set electrochemistry problem in one
location. Everything is in S.I. units.

"""

parameters = { 'material properties' : { 'Faradays constant' : 9.6e4,
                                         'gas constant' : 8.314},

               'geometry parameters' : { 'trench depth' : 0.5e-6,
                                         'aspect ratio' : 2,
                                         'trench spacing' : 0.6e-6,
                                         'boundary layer depth' : 0.3e-6},

               'accelerator properties' : { 'rate constant' : { 'constant' : (1.76),
                                                                'overpotential dependence' :
                                                                (-245e-6)
                                                                }
                                            },

               'metal ion properties' : { 'atomic volume' : 7.1e-6,
                                          'ion charge' : 2,
                                          'diffusion coefficient' : 5.6e-10,},

               'experimental parameters' : { 'exchange current density' : { 'constant' : 0.26,
                                                                            'accelerator dependence' : 45},
                                             'transfer coefficient' : 0.5,
                                             'temperature' : 298.,
                                             'overpotential' : -0.3,
                                             'initial accelerator coverage' : 0.,
                                             'bulk metal ion concentration' : 250.,
                                             'bulk accelerator concentration' : 5e-3},

               'control parameters' : { 'simulation end time' : 100,
                                        'cfl number' : 0.2,
                                        'cell size' : 0.1e-7,
                                        'number of cells in narrow band' : 10,
                                        'cells below trench' : 10 }
               }
