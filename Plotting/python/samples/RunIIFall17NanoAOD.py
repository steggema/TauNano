from InsideWTop.Plotting.samples.Sample import Sample

s_data = [
    Sample('SingleMuon_Run2017B_json', '/SingleMuon/Run2017B-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017C_json', '/SingleMuon/Run2017C-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017D_json', '/SingleMuon/Run2017D-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017E_json', '/SingleMuon/Run2017E-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017F_json', '/SingleMuon/Run2017F-31Mar2018-v1/NANOAOD'),
]

s_mc = [
    Sample('TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8', 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 88.29),
    Sample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM', 365.35),
    # Sample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 5765.4),
    # Sample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM', 5765.4),
    # FIXME: This is a manual haddNano.py, need to see how to solve this in the future
    Sample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_comb', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM', 5765.4),
    Sample('W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/NANOAODSIM', 8104.0),
    Sample('W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/NANOAODSIM', 2793.0),
    Sample('W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 992.5),
    Sample('W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 544.3),
    Sample('WW_TuneCP5_13TeV-pythia8', 'WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 75.88),
    Sample('WZ_TuneCP5_13TeV-pythia8', 'WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 27.6),
    Sample('ZZ_TuneCP5_13TeV-pythia8', 'ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 12.14),
    Sample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 35.85),
    Sample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM', 35.85),
    Sample('ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM', 136.02),
    Sample('ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 80.95),
]