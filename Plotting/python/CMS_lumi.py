# CMS_lumi
#   Initiated by: Gautier Hamel de Monchenault (Saclay)
#   Translated in Python by: Joshua Hardenbrook (Princeton)
#   Updated by:   Dinko Ferencek (Rutgers)
#

import ROOT

cmsTextFont = 61
extraTextFont = 52

lumiTextSize = 0.6
lumiTextOffset = 0.2

cmsTextSize = 0.75
cmsTextOffset = 0.1

relPosX = 0.045
relPosY = 0.035
relExtraDY = 1.2

extraOverCmsTextSize = 0.76

def CMS_lumi(pad, lumiText, iPosX, cmsText='CMS', writeExtraText=True, extraText=""):
    outOfFrame = False
    if iPosX/10 == 0:
        outOfFrame = True

    alignY_ = 3
    alignX_ = 2
    if iPosX/10 == 0:
        alignX_ = 1
    if iPosX == 0:
        alignY_ = 1
    if iPosX/10 == 1:
        alignX_ = 1
    if iPosX/10 == 2:
        alignX_ = 2
    if iPosX/10 == 3:
        alignX_ = 3
    align_ = 10*alignX_ + alignY_

    l = pad.GetLeftMargin()
    t = pad.GetTopMargin()
    r = pad.GetRightMargin()
    b = pad.GetBottomMargin()

    pad.cd()


    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)

    extraTextSize = extraOverCmsTextSize*cmsTextSize

    latex.SetTextFont(42)
    latex.SetTextAlign(31)
    latex.SetTextSize(lumiTextSize*t)

    latex.DrawLatex(1-r, 1-t+lumiTextOffset*t, lumiText)

    if outOfFrame:
        latex.SetTextFont(cmsTextFont)
        latex.SetTextAlign(11)
        latex.SetTextSize(cmsTextSize*t)
        latex.DrawLatex(l, 1-t+lumiTextOffset*t, cmsText)

    pad.cd()

    posX_ = 0
    if iPosX % 10 <= 1:
        posX_ = l + relPosX*(1-l-r)
    elif iPosX % 10 == 2:
        posX_ = l + 0.5*(1-l-r)
    elif iPosX % 10 == 3:
        posX_ = 1-r - (relPosX+0.1)*(1-l-r)-.02
        if writeExtraText:
            posX_ = 1-r - (relPosX+0.1)*(1-l-r)-.12

    posY_ = 1-t - relPosY*(1-t-b)

    if not outOfFrame:
        latex.SetTextFont(cmsTextFont)
        latex.SetTextSize(cmsTextSize*t)
        latex.SetTextAlign(align_)
        latex.DrawLatex(posX_, posY_, cmsText)
        if writeExtraText:
            latex.SetTextFont(extraTextFont)
            latex.SetTextAlign(align_)
            latex.SetTextSize(extraTextSize*t)
            latex.DrawLatex(posX_, posY_ - relExtraDY*cmsTextSize*t, extraText)
    elif writeExtraText:
        if iPosX == 0:
            posX_ = l + relPosX*(1-l-r)
            posY_ = 1-t+lumiTextOffset*t

        latex.SetTextFont(extraTextFont)
        latex.SetTextSize(extraTextSize*t)
        latex.SetTextAlign(align_)
        latex.DrawLatex(posX_+0.05, posY_, extraText)

    pad.Update()
