from TauNano.Plotting.PlotConfigs import SampleCfg
from TauNano.Plotting.HistCreator import setSumWeights
from TauNano.Plotting.samples.RunIIFall18NanoAOD import s_data, s_mc


def createSampleLists(analysis_dir='samples/', weight='', channel='mm'):
    ztt_cut = '(gen_match_2 == 5)'
    zl_cut = '(gen_match_2 > 0 && gen_match_2 < 5)'
    zj_cut = '(gen_match_2 == 0)'

    tree_prod_name = ''
    samples_essential = []

    samples_signal = []
    # SampleCfg(name=sample.name, dir_name=sample.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name,
    #                     xsec=5., sumweights=sample.nGenEvents, weight_expr=('*'.join([weight])), is_signal=True))

    samples_data = [
        SampleCfg(name='data', dir_name=s.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, is_data=True) for s in s_data
    ]

    samples_mc = [
        SampleCfg(name=s.name, dir_name=s.name, ana_dir=analysis_dir, tree_prod_name=tree_prod_name, xsec=s.xsec, weight_expr=weight) for s in s_mc
    ]

    if channel == 'mt':
        samples_to_add = []
        for s_cfg in samples_mc:
            if 'DY' in s_cfg.name:
                samples_to_add += [
                    SampleCfg(name='ZTT', dir_name=s_cfg.dir_name, ana_dir=s_cfg.ana_dir, tree_prod_name=s_cfg.tree_prod_name, xsec=s_cfg.xsec, weight_expr='*'.join(['({})'.format(s_cfg.weight_expr), ztt_cut])),
                    SampleCfg(name='ZL', dir_name=s_cfg.dir_name, ana_dir=s_cfg.ana_dir, tree_prod_name=s_cfg.tree_prod_name, xsec=s_cfg.xsec, weight_expr='*'.join(['({})'.format(s_cfg.weight_expr), zl_cut])),
                    SampleCfg(name='ZJ', dir_name=s_cfg.dir_name, ana_dir=s_cfg.ana_dir, tree_prod_name=s_cfg.tree_prod_name, xsec=s_cfg.xsec, weight_expr='*'.join(['({})'.format(s_cfg.weight_expr), zj_cut]))
                ]
        samples_mc = [s for s in samples_mc if not 'DY' in s.name] + samples_to_add

    samples_essential = samples_mc

    samples = samples_essential + samples_data + samples_signal
    all_samples = samples_mc + samples_data

    weighted_list = []

    for sample in samples_mc:
        if sample.name not in weighted_list:
            setSumWeights(sample)

    sampleDict = {s.name: s for s in all_samples}

    return samples_mc, samples_data, samples, all_samples, sampleDict

# samples_mc, samples_data, samples, all_samples, sampleDict = createSampleLists()
