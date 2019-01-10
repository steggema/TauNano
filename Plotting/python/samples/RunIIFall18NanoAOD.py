from InsideWTop.Plotting.samples.Sample import Sample

s_data = [

    Sample('SingleMuon_Run2018A_06Jun2018', '/SingleMuon/SingleMuon_Run2018A_06Jun2018/NANOAOD'),
    Sample('SingleMuon_Run2018A_ver3', '/SingleMuon/Run2018A-14Sep2018_ver3-v1/NANOAOD'),
    Sample('SingleMuon_Run2018B_ver1', '/SingleMuon/Run2018B-14Sep2018_ver1-v1/NANOAOD'),
    Sample('SingleMuon_Run2018B_ver2', '/SingleMuon/Run2018B-14Sep2018_ver2-v1/NANOAOD'),
    # Sample('SingleMuon_Run2018B_ver3', '/SingleMuon/Run2018B-14Sep2018_ver3-v1/NANOAOD'),
    Sample('SingleMuon_Run2018C_ver1', '/SingleMuon/Run2018C-14Sep2018_ver1-v1/NANOAOD'),
    Sample('SingleMuon_Run2018C_ver2', '/SingleMuon/Run2018C-14Sep2018_ver2-v1/NANOAOD'),
    Sample('SingleMuon_Run2018C_ver3', '/SingleMuon/Run2018C-14Sep2018_ver3-v1/NANOAOD'),
    Sample('SingleMuon_Run2018D_14Sep2018', '/SingleMuon/SingleMuon_Run2018D_14Sep2018/NANOAOD'),
]

s_mc = [
    Sample('TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8', '/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIIFall18NanoAOD-102X_upgrade2018_realistic_v12-v1/NANOAODSIM', 831.76 ),
    
    Sample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_2018_pileup', '/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall18NanoAOD-102X_upgrade2018_realistic_v12_ext1-v1/NANOAODSIM', 5765.4),
    Sample('WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', '/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall18NanoAOD-102X_upgrade2018_realistic_v12-v1/NANOAODSIM', 61526.7),
    # Sample('W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/NANOAODSIM', 8104.0),
    # Sample('W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/NANOAODSIM', 2793.0),
    # Sample('W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 992.5),
    # Sample('W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 544.3),
    # Sample('WW_TuneCP5_13TeV-pythia8', 'WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 75.88),
    # Sample('WZ_TuneCP5_13TeV-pythia8', 'WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 27.6),
    # Sample('ZZ_TuneCP5_13TeV-pythia8', 'ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 12.14),
    # Sample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 35.85),
    # Sample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM', 35.85),
    # Sample('ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM', 136.02),
    # Sample('ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 80.95),
]