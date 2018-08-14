#!/bin/bash
BASEDIR=/eos/cms/store/cmst3/group/exovv/clange/InsideWTop/Skims
OUTDIR=$BASEDIR
# change delimiter to forward slash
# IFS='/'
for i in $BASEDIR/*/; do
  haddnano.py ${OUTDIR}/`basename ${i%/*}`.root $i/*.root
done
