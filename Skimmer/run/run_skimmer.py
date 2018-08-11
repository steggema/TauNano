#!/bin/env python
# pylint: disable=E0401,C0103
from argparse import ArgumentParser
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import PostProcessor
from InsideWTop.Skimmer.skimmer import Skimmer

# need to keep this for grid-control
# @FILE_NAMES@

cut_dict = {}
cut_dict["base"] = "nFatJet>0&&FatJet_msoftdrop>30&&FatJet_pt>200&&MET_sumEt>40"
cut_dict["muon"] = "nMuon>0&&HLT_Mu50"
cut_dict["electron"] = "nElectron>0&&HLT_Ele115_CaloIdVT_GsfTrkIdT"
REDIRECTOR = "root://xrootd-cms.infn.it//"

parser = ArgumentParser(description='Run the NanoAOD skimmer.')
parser.add_argument('inFiles', nargs="+", default="", help="Comma-separated list of input files")
parser.add_argument('--out', action="store", dest="outDir", default="./",
                    help="Output directory")
parser.add_argument('--keepdrop', action="store", dest="keepDropFile",
                    default="keep_and_drop.txt", help="Branches keep and drop file")
args = parser.parse_args()

# inFiles come as combination of comma- and/or space-separated list
inFiles = ','.join(args.inFiles).replace("\"", "").split(',')
inFiles = [REDIRECTOR+f if f.startswith('/store') else f for f in inFiles]
outputDir = args.outDir
keepDropFile = args.keepDropFile

if inFiles[0].find("SingleMuon") != -1:
    channel = "mu"
    cuts = "{}&&({})".format(cut_dict["base"], cut_dict["muon"])
    print "Processing a Single Muon dataset file..."
elif inFiles[0].find("SingleElectron") != -1:
    channel = "el"
    cuts = "{}&&({})".format(cut_dict["base"], cut_dict["electron"])
    print "Processing a Single Electron dataset file..."
else:
    print "Processing MC..."
    channel = "elmu"
    cuts = "{}&&(({})||({}))".format(cut_dict["base"], cut_dict["electron"], cut_dict["muon"])

p = PostProcessor(outputDir, inFiles, cuts, keepDropFile,
                  modules=[Skimmer(channel)], provenance=False, fwkJobReport=False)
p.run()
