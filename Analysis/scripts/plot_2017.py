from InsideWTop.Plotting.PlotConfigs import HistogramCfg
from InsideWTop.Plotting.HistCreator import createHistograms
from InsideWTop.Plotting.HistDrawer import HistDrawer
from InsideWTop.Analysis.plotting.Variables import mumu_vars, taumu_vars
from InsideWTop.Analysis.plotting.Samples_2017 import createSampleLists

from InsideWTop.Analysis.plotting.qcdEstimationMSSMltau import estimateQCDWMSSM, createQCDWHistograms

# from InsideWTop.H2TauTau.proto.plotter.helper_methods import plotDataOverMCEff

# always cut on category, otherwise normalisation is off!
total_weight = '1.'

print 'Total weight:', total_weight

# channels = ['mt']
channels = ['mm']

int_lumi = 41368
r_qcd_os_ss = 1.17

cuts = {}
cuts['mm'] = {'inclusive':'nSelMuons >= 2 && mvis > 50. && pt_1 > 29. && HLT_IsoMu27'}
cuts['mt'] = {'inclusive':'nSelMuons == 1 && pt_1 > 29. && HLT_IsoMu27 && pt_2 > 30. && idMVAoldDM2017v2_2 & 32 && idDecayMode_2==1 && idAntiMu_2 & 2 && idAntiEle_2 & 1 && q_1 != q_2'}

weights = {}
weights['mm'] = "genWeight * puWeight * effSF_1 * effSF_2"
weights['mt'] = "genWeight * puWeight * effSF_1"

# -> Command line
analysis_dir = '/eos/cms/store/cmst3/group/htautau/NanoAOD/Skims/'
print "Analysis dir:", analysis_dir

variables = {}
variables['mm'] = mumu_vars
variables['mt'] = taumu_vars

for channel in channels:
    for cut_name, cut in cuts[channel].items():
        hist_dict = {}
        samples_mc, samples_data, samples, all_samples, sampleDict = createSampleLists(analysis_dir, weight=weights[channel], channel=channel)
        if channel == 'mt':
            samples = createQCDWHistograms(samples, hist_dict, int_lumi, weight=total_weight, r_qcd_os_ss=r_qcd_os_ss)

        cfg_example = HistogramCfg(name='example', var=None, cfgs=samples, cut=cut, lumi=int_lumi, weight=total_weight)

        print cfg_example.cut
        cfg_example.vars = variables[channel]

        if channel == 'mt':
            estimateQCDWMSSM(hist_dict, cut, mt_cut='(mt_1<40)', r_qcd_os_ss=r_qcd_os_ss, vars=variables[channel])

        plots = createHistograms(cfg_example, verbose=False)
        for variable in variables[channel]:
            plot = plots[variable.name]
            # plot.Group('Diboson', ['WWTo1L1Nu2Q', 'WWTo1L1Nu2Q', 'WZTo1L1Nu2Q'])
            plot.Group('Top', ['TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8', 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
                               'ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8',
                               'ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8',
                               'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
                               'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8'])
            plot.Group('WJets', ['W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8', 'W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8'])
            plot.Group('Diboson', ['WW_TuneCP5_13TeV-pythia8', 'WZ_TuneCP5_13TeV-pythia8', 'ZZ_TuneCP5_13TeV-pythia8'])
            plot.Group('ZLL', ['DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_ext1', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8', 'DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_comb'])

            plot.Group('data_obs', ['data'])
            HistDrawer.draw(plot, plot_dir='plots_{}/{}'.format(channel, cut_name), channel=channel)
            # plot.WriteDataCard(filename='datacard_mm.root', dir='mm_' + cut_name)
