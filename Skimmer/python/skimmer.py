"""
Generic mu-tau and dimuon selection for tau analyses.
"""

# pylint: disable=E0401,E0402,C0103,C0413

from itertools import permutations, product

import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.tools import deltaR2
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from InsideWTop.Skimmer.tools import calcMT, calcPzetaVars

DEFAULT = -999

class Skimmer(Module):
    def __init__(self, is_data=False):
        self.out = None
        self.writeHistFile = True

        # Use naming conventions for HTT sync ntuples
        self.basic_branch_names = ['pt', 'eta', 'phi', 'm', 'q', 'd0', 'dz', 'mt', 'dxy', 'dz'] #FIXME: int vars, like gen_match
        if not is_data:
            self.basic_branch_names.append('gen_match')
        self.tau_branch_names = ['puCorr', 'rawAntiEle', 'rawIso', 'rawIsodR03', 'rawMVAnewDM2017v2', 'rawMVAoldDM', 'rawMVAoldDM2017v1', 'rawMVAoldDM2017v2', 'rawMVAoldDMdR032017v2', 'decayMode', 'idAntiEle', 'idAntiMu', 'idDecayMode', 'idMVAnewDM2017v2', 'idMVAoldDM', 'idMVAoldDM2017v1', 'idMVAoldDM2017v2', 'idMVAoldDMdR032017v2']
        self.muon_branch_names = [] if is_data else ['effSF']

        self.translater = {
            'm':'mass',
            'q':'charge',
            'd0':'dxy',
            'gen_match':'genPartFlav',
        }

        self.no_reset_branches = ['nMuon', 'nElectron', 'Muon_effSF', 'Electron_effSF']

    def beginJob(self, histFile, histDirName):
        Module.beginJob(self, histFile, histDirName)
        # self.addObject( ROOT.TH1F('nGenEv',   'nGenEv',   3, 0, 3) )

    def endJob(self):
        Module.endJob(self)

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("passedMETfilters", "I")

        # Counting variables
        self.out.branch("nSelMuons", "I")
        self.out.branch("nSelTaus", "I")

        for b_name in self.basic_branch_names:
            for i_obj in ['1', '2', '3']:
                self.out.branch('_'.join([b_name, i_obj]), "F")

        for b_name in self.tau_branch_names:
            for i_obj in ['2', '3']:
                self.out.branch('_'.join([b_name, i_obj]), "F")

        for b_name in self.muon_branch_names:
            for i_obj in ['1', '2']:
                self.out.branch('_'.join([b_name, i_obj]), "F")

        self.out.branch("mvis", "F")
        self.out.branch("ptvis", "F")
        self.out.branch("pzeta_vis", "F")
        self.out.branch("pzeta_met", "F")
        self.out.branch("pzeta_disc", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def fillBasic(self, particle, p_i):
        for var in self.basic_branch_names:
            self.out.fillBranch('{}_{}'.format(var, p_i), getattr(particle, self.translate(var)))

    def fillMuon(self, particle, p_i):
        for var in self.muon_branch_names:
            self.out.fillBranch('{}_{}'.format(var, p_i), getattr(particle, self.translate(var)))

    def fillTau(self, particle, p_i):
        for var in self.tau_branch_names:
            self.out.fillBranch('{}_{}'.format(var, p_i), getattr(particle, self.translate(var)))

    def translate(self, name):
        try:
            return self.translater[name]
        except KeyError:
            return name

    def fillMETFilterDecision(self, event):
        passedMETFilters = False
        # Add filters https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#Moriond_2018
        filter_names = ["Flag_BadChargedCandidateFilter", "Flag_BadPFMuonFilter", "Flag_EcalDeadCellTriggerPrimitiveFilter", "Flag_HBHENoiseFilter", "Flag_HBHENoiseIsoFilter", "Flag_METFilters", "Flag_ecalBadCalibFilter", "Flag_globalTightHalo2016Filter", "Flag_goodVertices"]
        if all(getattr(event, filter_name) for filter_name in filter_names):
            passedMETFilters = True
        self.out.fillBranch("passedMETfilters", passedMETFilters)

    @staticmethod
    def isMuon(muon):
        return hasattr(muon, 'mediumId')

    @staticmethod
    def isTau(tau):
        return hasattr(tau, 'decayMode')

    @staticmethod
    def selectMuon(muon):
        '''Select muon passing analysis criteria
        '''
        muon.iso = -muon.pfRelIso03_all
        return muon.pt > 29. and abs(muon.eta) < 2.4 and muon.mediumId and muon.pfRelIso03_all < 0.15

    @staticmethod
    def selectTau(tau):
        '''Select muon passing analysis criteria, without isolation
        '''
        tau.iso = tau.rawMVAoldDM2017v2
        return tau.pt > 20. and abs(tau.eta) < 2.3 and tau.idDecayMode and tau.dz < 0.2

    @staticmethod
    def bestPair(pairs):
        least_iso_highest_pt = lambda cand1, cand2: (-cand1.iso, -cand1.pt, -cand2.iso, -cand2.pt)

        return sorted(pairs, key=lambda pair: least_iso_highest_pt(pair[0], pair[1]))[0]

    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""

        self.fillMETFilterDecision(event)

        # MUONS
        muons = Collection(event, 'Muon')
        muons = [muon for muon in muons if self.selectMuon(muon)]
        muons.sort(key=lambda x: x.pt, reverse=True)

        # At least one muon
        if not muons:
            return False

        taus = Collection(event, 'Tau')
        taus = [tau for tau in taus if self.selectTau(tau)]
        taus = [tau for tau in taus if not any(deltaR2(tau, muon) < 0.25 for muon in muons)]

        all_pairs = []
        if len(muons) > 1:
            all_pairs = [mumu for mumu in permutations(muons, 2)]
        else: # 1 muon
            all_pairs = [mutau for mutau in product(muons, taus)]

        # At least one pair, either mu-mu or mu-tau
        if not all_pairs:
            return False

        # Reset branch entries
        for branch_name in self.out._branches:
            if branch_name not in self.no_reset_branches:
                self.out.fillBranch(branch_name, DEFAULT)

        best_pair = self.bestPair(all_pairs)

        l1 = best_pair[0]
        l2 = best_pair[1]

        # If two muons, sort pair by pT
        if self.isMuon(l2):
            if l2.pt > l1.pt:
                best_pair = (l2, l1)

        mvis = (l1.p4() + l2.p4()).M()
        pt_vis = (l1.p4() + l2.p4()).Pt()

        self.out.fillBranch("nSelMuons", len(muons))
        self.out.fillBranch("nSelTaus", len(taus))
        self.out.fillBranch("mvis", mvis)
        self.out.fillBranch("ptvis", pt_vis)

        ptmiss = Object(event, 'MET')

        l1.mt = calcMT(l1, ptmiss)
        l2.mt = calcMT(l2, ptmiss)

        self.fillBasic(l1, 1)
        self.fillBasic(l2, 2)

        for i_cand, cand in enumerate([l1, l2]):
            if self.isMuon(cand):
                self.fillMuon(cand, i_cand + 1)
            if self.isTau(cand):
                self.fillTau(cand, i_cand + 1)

        pzeta_vis, pzeta_met, pzeta_disc = calcPzetaVars(l1, l2, ptmiss)

        self.out.fillBranch("pzeta_vis", pzeta_vis)
        self.out.fillBranch("pzeta_met", pzeta_met)
        self.out.fillBranch("pzeta_disc", pzeta_disc)

        other_taus = [tau for tau in taus if tau not in best_pair]
        if other_taus:
            l3 = other_taus[0]
            l3.mt = calcMT(l3, ptmiss)
            self.fillBasic(l3, 3)
            self.fillTau(l3, 3)

        return True

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
# ttbar_semilep = lambda: Skimmer()
