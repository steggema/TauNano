"""return cross section for a given sample."""

xsec_dict = {}

xsec_dict["WJetsToQQ_HT"] = 95.14
xsec_dict["ZJetsToQQ_HT600toInf"] = 41.34
xsec_dict["QCD_Pt_170to300_"] = 117276.
xsec_dict["QCD_Pt_300to470_"] = 7823.
xsec_dict["QCD_Pt_470to600_"] = 648.2
xsec_dict["QCD_Pt_600to800_"] = 186.9
xsec_dict["QCD_Pt_800to1000_"] = 32.293
xsec_dict["QCD_Pt_1000to1400_"] = 9.4183
xsec_dict["QCD_Pt_1400to1800_"] = 0.84265
xsec_dict["QCD_Pt_1800to2400_"] = 0.114943
xsec_dict["QCD_Pt_2400to3200_"] = 0.006830
xsec_dict["QCD_Pt_3200toInf_"] = 0.000165445
xsec_dict["QCD_HT100to200"] = 27990000
xsec_dict["QCD_HT200to300"] = 1712000.
xsec_dict["QCD_HT300to500"] = 347700.
xsec_dict["QCD_HT500to700"] = 32100.
xsec_dict["QCD_HT700to1000"] = 6831.
xsec_dict["QCD_HT1000to1500"] = 1207.
xsec_dict["QCD_HT1500to2000"] = 119.9
xsec_dict["QCD_HT2000toInf"] = 25.24
xsec_dict["QCD_Pt-15to7000"] = 2.022100000e+09
xsec_dict["QCD_Pt_15to7000"] = xsec_dict["QCD_Pt-15to7000"]
xsec_dict["TTToHadronic"] = 831.76 * 0.6741 * 0.6741
xsec_dict["TTToSemiLeptonic"] = 831.76 * 0.3272 * 0.6741 * 2.
xsec_dict["TTTo2L2Nu"] = 831.76 * 0.3272 * 0.3272
xsec_dict["TT_Tune"] = 831.76
xsec_dict["WJetsToLNu_HT-100To200"] = 1347 * 1.21
xsec_dict["WJetsToLNu_HT-200To400"] = 360 * 1.21
xsec_dict["WJetsToLNu_HT-400To600"] = 48.9 * 1.21
xsec_dict["WJetsToLNu_HT-600To800"] = 12.08 * 1.21
xsec_dict["WJetsToLNu_HT-800To1200"] = 5.26 * 1.21
xsec_dict["WJetsToLNu_HT-1200To2500"] = 1.33 * 1.21
xsec_dict["WJetsToLNu_HT-70To100"] = 1270. * 1.21
xsec_dict["WJetsToLNu_HT-2500ToInf"] = 0.03089 * 1.21
xsec_dict["WJetsToLNu_TuneCUETP8M1"] = 50380.0 * 1.22
xsec_dict["W1JetsToLNu_TuneCUETP8M1"] = 9644.5 * 1.22
xsec_dict["W2JetsToLNu_TuneCUETP8M1"] = 3144.5 * 1.22
xsec_dict["W3JetsToLNu_TuneCUETP8M1"] = 954.8 * 1.22
xsec_dict["W4JetsToLNu_TuneCUETP8M1"] = 485.6 * 1.22
xsec_dict["WW_Tune"] = 118.7
xsec_dict["WZ_Tune"] = 47.13
xsec_dict["ZZ_Tune"] = 16.5
xsec_dict["ST_s-channel_4f_leptonDecays"] = 11.36 * 0.3272
xsec_dict["ST_t-channel_top_4f_leptonDecays"] = 136.02 * 0.322
xsec_dict["ST_t-channel_antitop_4f_leptonDecays"] = 80.95 * 0.322
xsec_dict["ST_t-channel_antitop_4f_inclusiveDecays"] = 136.02
xsec_dict["ST_t-channel_top_4f_inclusiveDecays"] = 80.95
xsec_dict["ST_tW_antitop_5f_inclusiveDecays"] = 35.6
xsec_dict["ST_tW_top_5f_inclusiveDecays_"] = 35.6
xsec_dict["SingleMuon"] = 1.
xsec_dict["SingleElectron"] = 1.
xsec_dict["JetHT"] = 1.
xsec_dict["data"] = 1.


def getXsec(sample):
    for eachKey in xsec_dict.keys():
        if sample.find(eachKey):
            return xsec_dict[eachKey]
    print "Cross section not defined for this sample!"
    raise ValueError
