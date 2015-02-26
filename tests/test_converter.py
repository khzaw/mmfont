# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0,
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mmfont.converter import uni512zg1, zg12uni51, test


def test_uni_to_zawgyi():
    uni_string = "ကျွန်တော်တို့ ပစ္စည်းများကို ကျွန်တော့်တို့ရဲ့ လက် ဖြင့် ကိုင်ကြပါသည်"
    assert uni_string == zg12uni51(uni512zg1(uni_string))

    uni_string = "လူငယ်အဆိုတော် စိုင်းစိုင်းခမ်းလှိုင်"
    assert uni_string == zg12uni51(uni512zg1(uni_string))

def test_zawgyi_to_uni():
    zawgyi_string = "ကၽြန္ေတာ္တို႔ ပစၥည္းမ်ားကို ကၽြန္ေတာ့္တို႔ရဲ့ လက္ ျဖင့္ ကိုင္ၾကပါသည္"
    assert zawgyi_string == uni512zg1(zg12uni51(zawgyi_string))
