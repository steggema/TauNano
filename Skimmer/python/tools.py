import math
from itertools import combinations
from ROOT import TVector3

def calcMT(cand1, cand2):
    '''Calculates the transverse mass for two objects.
    '''
    # pt = cand1.pt + cand2.pt
    # # FIXME - the following is slow for NanoAOD, consider cosine-based version
    # px = cand1.p4().px() + cand2.p4().px()
    # py = cand1.p4().py() + cand2.p4().py()
    mt2 = 2*cand1.pt*cand2.pt*(1 - math.cos(cand1.phi - cand2.phi))
    return math.sqrt(mt2)
    # try:
        # return math.sqrt(pt*pt - px*px - py*py)
    # except ValueError:
    #     print 'Funny rounding issue in MT calculation', pt, px, py
    #     print cand1.px(), cand1.py(), cand1.pt()
    #     print cand2.px(), cand2.py(), cand2.pt()
    #     return 0.

def calcMtTotal(cands):
    return math.sqrt(sum(calcMT(c1, c2)**2 for c1, c2 in combinations(cands, 2)))

def calcPzetaVars(cand1, cand2, met):
    c1_pt_vec = TVector3(cand1.p4().Px(), cand1.p4().Py(), 0.)
    c2_pt_vec = TVector3(cand2.p4().Px(), cand2.p4().Py(), 0.)
    met_pt_vec = TVector3(met.pt*math.cos(met.phi), met.pt*math.sin(met.phi), 0.)
    zeta_axis = (c1_pt_vec.Unit() + c2_pt_vec.Unit()).Unit()
    pzeta_vis = c1_pt_vec*zeta_axis + c2_pt_vec*zeta_axis
    pzeta_met = met_pt_vec*zeta_axis
    pzeta_disc = pzeta_met -0.5*pzeta_vis
    return pzeta_vis, pzeta_met, pzeta_disc
