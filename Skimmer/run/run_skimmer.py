#!/bin/env python
# pylint: disable=E0401,C0103
from argparse import ArgumentParser
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import muonSF2017
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import puAutoWeight
from InsideWTop.Skimmer.skimmer import Skimmer

# need to keep this for grid-control
# @FILE_NAMES@

maxEvents = -1

cut_dict = {}
cut_dict["base"] = "nMuon>0"
cut_dict["muon_trigger"] = "(HLT_IsoMu27 || HLT_IsoMu24)"

# REDIRECTOR = "root://xrootd-cms.infn.it//"
REDIRECTOR = "root://cms-xrd-global.cern.ch//"

parser = ArgumentParser(description='Run the NanoAOD skimmer.')
parser.add_argument('inFiles', nargs="+", default="", help="Comma-separated list of input files")
parser.add_argument('--out', action="store", dest="outDir", default="./",
                    help="Output directory")
parser.add_argument('--keepdrop', action="store", dest="keepDropFile",
                    default="keep_and_drop.txt", help="Branches keep and drop file")
parser.add_argument('--isdata', action="store_true", dest="isdata", default=False,
                    help="Whether running on data")
args = parser.parse_args()

# inFiles come as combination of comma- and/or space-separated list
inFiles = ','.join(args.inFiles).replace("\"", "").split(',')
inFiles = [REDIRECTOR+f if f.startswith('/store') else f for f in inFiles]
outputDir = args.outDir
keepDropFile = args.keepDropFile

cuts = '&&'.join(['({})'.format(cut) for cut in cut_dict.values()])

modules = [Skimmer(args.isdata)] if args.isdata else [muonSF2017(), Skimmer(), puAutoWeight()]

jsonInput = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/ReReco/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt' if args.isdata else None

p = PostProcessor(outputDir, inFiles, cuts, outputbranchsel=keepDropFile,
                  modules=modules, provenance=False, fwkJobReport=False,
                  jsonInput=jsonInput, maxEvents=maxEvents)
p.run()
