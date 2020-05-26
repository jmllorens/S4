#!/usr/bin/env python3
import S4B as S4
import numpy as np
from pprint import pprint

S = S4.New(Lattice=((1,0),(0,1)), NumBasis=5)
S.SetOptions(Verbosity=9)
S.SetMaterial(Name = "Silicon", Epsilon = 12+0.01j)
S.SetMaterial(Name = "Vacuum",  Epsilon = 1.0)
S.AddLayer(Name = 'l0', Thickness = 0, Material = 'Vacuum')
S.AddLayer(Name = 'l1', Thickness = 0.6, Material = 'Silicon')
S.AddLayer(Name = 'l2', Thickness = 0, Material = 'Vacuum')

S.SetRegionCircle(
        Layer = 'l1',
        Material = 'Vacuum',
        Center = (0,0),
        Radius = 0.2
)

S.SetExcitationPlanewave(
        IncidenceAngles=(
                10, # polar angle in [0,180)
                30  # azimuthal angle in [0,360)
        ),
        sAmplitude = 0.707+0.707j,
        pAmplitude = 0.707-0.707j,
        Order = 0
)

S.SetFrequency(1.2)

Glist = S.GetBasisSet()
pprint(len(Glist))

#pprint(np.array(Glist))
(forw,back) = S.GetPowerFlux(Layer = 'l0', zOffset = 0)
#pprint(forw)
#pprint(back)
(forw,back) = S.GetPowerFlux(Layer = 'l2', zOffset = 0)
#pprint(forw)
#pprint(back)
# SMatrix = np.array(S.GetSMatrix(0,2))
# pprint((SMatrix.shape, SMatrix.mean()))
EHN = S.GetFieldsByN(-0.1, -0.1, -0.1)
EH = S.GetFields(-0.1, -0.1, -0.1)
EHN = np.array(EHN)
EH = np.array(EH)
pprint("I am in python")
EHN = np.array(EHN)
pprint("STOOOP")
pprint((EHN.shape, EHN.mean()))
pprint((EHN[0,:,:].sum(axis=0), EH[0,:]))
