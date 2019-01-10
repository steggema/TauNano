#!/bin/bash
BASEDIR=/eos/cms/store/cmst3/group/htautau/NanoAOD/Skims/2018
OUTDIR=$BASEDIR
# change delimiter to forward slash
# IFS='/'
for i in $BASEDIR/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_2018/; do
  haddnano.py ${OUTDIR}/`basename ${i%/*}`.root $i/*.root
done
