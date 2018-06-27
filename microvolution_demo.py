import pyvolution as mv
import sys

try:
    lic = mv.Licensing.GetInstance()
    lic.SetPath(...)

    params = mv.DeconParameters()
    params.nx = 512
    params.ny = 512
    params.nz = 32
    params.iterations = 10
    params.wavelength = 525 # wavelength is lambda in C++/Java/C#
    params.dr = 100
    params.dz = 250
    params.NA = 0.6
    params.RI = 1.0
    params.ns = 1.33
    params.psfType = mv.PSFType.Widefield
    params.psfModel = mv.PSFModel.Vectorial
    params.generatePsf = True
    params.scaling = mv.Scaling.U16

    launcher = mv.DeconvolutionLauncher()
    launcher.SetParameters(params);

    for i in range(params.nz):
        launcher.SetImageSlice(...2D numpy array...)

    launcher.Run()

    for i in range(params.nz):
        launcher.RetrieveImageSlice(...)

    launcher.Reset()
except:
    print("Error:", sys.exc_info())
