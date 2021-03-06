from vanilla.dialogs import *



inputFonts = getFile("select masters to add feature code to", allowsMultipleSelection=True, fileTypes=["ufo"])


feaText = """languagesystem DFLT dflt;
languagesystem latn dflt;


@defaultletters = [a            f            g            i            l            r            y       ];
@slopedroman    = [a.roman      f.roman      g.roman      i.roman      l.roman      r.roman      y.roman];
@trueitalics    = [a.italic     f.italic     g.italic     i.italic     l.italic     r.italic     y.italic];

feature ss01 {
    featureNames {
		name 3 1 0x0409 "italic a, f, g, i, l, r, y"; # Win / Unicode / English US
		name 1 0 0 "italic a, f, g, i, l, r, y"; #   Mac / Roman / English
	};
    sub @defaultletters by @trueitalics;
} ss01;

feature ss02 {
    featureNames {
		name 3 1 0x0409 "roman a, f, g, i, l, r, y"; # Win / Unicode / English US
		name 1 0 0 "roman a, f, g, i, l, r, y"; #   Mac / Roman / English
	};
    sub @defaultletters by @slopedroman;
} ss02;

feature locl {
    script latn;
        language NLD exclude_dflt;
            lookup DutchIJ {
                sub I J by IJ;
            } DutchIJ;
} locl;

""" 

def addFeatureCode(f):
    f.features.text = feaText
    
    
for fontPath in inputFonts:
    f = OpenFont(fontPath, showInterface=False)
    addFeatureCode(f)
    fontName = f.info.familyName + " " + f.info.styleName
    print("feature code added to " + fontName)
    f.save()
    f.close()