from InsideWTop.Plotting.PlotConfigs import SampleCfg
from InsideWTop.Plotting.HistCreator import setSumWeights

class Sample(object):
    """Define MC and data samples."""

    def __init__(self, name, das_id, xsec=None):
        self.name = name
        self.das_id = das_id
        self.xsec = xsec # None: data sample


s_data = [
    Sample('SingleMuon_Run2017B', '/SingleMuon/Run2017B-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017C', '/SingleMuon/Run2017C-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017D', '/SingleMuon/Run2017D-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017E', '/SingleMuon/Run2017E-31Mar2018-v1/NANOAOD'),
    Sample('SingleMuon_Run2017F', '/SingleMuon/Run2017F-31Mar2018-v1/NANOAOD'),
]

s_mc = [
    Sample('TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8', 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 88.29),
    Sample('TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8', 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/NANOAODSIM', 365.35),
    Sample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 5765.4),
    Sample('DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017RECOSIMstep_12Apr2018_94X_mc2017_realistic_v14_ext1-v1/NANOAODSIM', 5765.4),
    Sample('/W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v3/NANOAODSIM', 8104.0),
    Sample('/W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v4/NANOAODSIM', 2793.0),
    Sample('/W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 992.5),
    Sample('/W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 544.3),
    Sample('WW_TuneCP5_13TeV-pythia8', 'WW_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 75.88),
    Sample('WZ_TuneCP5_13TeV-pythia8', 'WZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 27.6),
    Sample('ZZ_TuneCP5_13TeV-pythia8', 'ZZ_TuneCP5_13TeV-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 12.14),
    Sample('ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 35.85),
    Sample('ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8', 'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM', 35.85),
    Sample('ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_new_pmx_94X_mc2017_realistic_v14-v1/NANOAODSIM', 136.02),
    Sample('ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8', 'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8/RunIIFall17NanoAOD-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/NANOAODSIM', 80.95),
]

def createSampleLists(analysis_dir='samples/', channel='mm', weight=''):
    tree_prod_name = ''
    samples_essential = []

    samples_signal = []
    # SampleCfg(name=sample.name, dir_name=sample.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name,
    #                     xsec=5., sumweights=sample.nGenEvents, weight_expr=('*'.join([weight])), is_signal=True))

    samples_data = [
        SampleCfg(name='data', dir_name=s.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, is_data=True) for s in s_data
    ]
    
    samples_mc = [
        SampleCfg(name=s.name, dir_name=s.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=s.xsec) for s in s_mc
    ]
    samples_essential = samples_mc

    samples = samples_essential + samples_data + samples_signal
    all_samples = samples_mc + samples_data

    weighted_list = []

    for sample in samples_mc:
        if sample.name not in weighted_list:
            setSumWeights(sample)

    sampleDict = {s.name: s for s in all_samples}

    return samples_mc, samples_data, samples, all_samples, sampleDict

samples_mc, samples_data, samples, all_samples, sampleDict = createSampleLists()
