
from ModelInfo import allrefs
import os

info = """
## Tests on OSB models
"""

YES = ' \\multicolumn{1}{c}{Yes} '
YES = ' \\ding{51} '

count = 0

info += '  | Model | Tests | Pull requests |\n'
info += '  |----------|:------:|:------:|\n'
for directory in allrefs.keys():
    ref = allrefs[directory]

    print("Looking at: %s in %s"%(ref, directory))

    gh = 'OpenSourceBrain/%s'%directory if not '/' in directory else directory

    info += ' | <a href="https://github.com/%s">%s</a> |'%(gh,ref)

    info += ' |' if '--' in directory else \
            '  [![OMV](https://github.com/%s/actions/workflows/omv-ci.yml/badge.svg)](https://github.com/%s/actions/workflows/omv-ci.yml) '%(gh,gh) \
            + '  [![ ](https://github.com/%s/actions/workflows/non-omv.yml/badge.svg)](https://github.com/%s/actions/workflows/non-omv.yml) | '%(gh,gh)

    info += ' |\n' if '--' in directory else \
            '  [![GitHub pull requests](https://img.shields.io/github/issues-pr/%s)](https://github.com/%s/pulls) | \n'%(gh,gh)

    count+=1

info += '  </table>\n'

'''
    if count < 11:
        info += '    F3F3F3} '
    elif count < 15:
        info += '    FFB380} '
    elif count < 20:
        info += '    \\cellcolor[HTML]{FFE680} '
    elif count < 21:
        info += '    \\cellcolor[HTML]{C6E4E4} '
    elif count < 25:
        info += '    \\cellcolor[HTML]{D3BC5F} '
    else:
        info += '    \\cellcolor[HTML]{E4A59E} '


    info += '  %s & '%ref
    travis = 'coreprojects/%s/.travis.yml'%(directory)
    travis_file = open(travis) if os.path.isfile(travis) else []
    engines = []
    for line in travis_file:
        line = line.strip()
        if 'OMV_ENGINE' in line and not line.startswith('#'):
            eng = line.split('=')[1].strip()
            engines.append(eng)

    engines = sorted(engines)


    if 'jNeuroML_validate' in engines:
        info += YES
    info += ' &'

    arrow = '$\\,\\to\\,$'
    arrow = '$\\rightarrow$ '

    for engine in engines:
        if 'jNeuroML_PyNN_NEURON' in engine:
            sim = engine.replace('jNeuroML','NeuroML').replace('_',arrow)
            info += ' %s '%sim
        elif  'PyNN' in engine:
            sim = engine[5:]
            if sim[-1]=='1': sim=sim[:-1]
            info += ' %s;'%sim

    if info[-1]==';':
        info = info[:-1]

    info += ' &'

    if 'jNeuroML' in engines:
        info += YES
    info += ' &'

    if 'jNeuroML_NEURON' in engines:
        info += YES
    info += ' &'


    print("  Engines: %s"%engines)

    excl = ['NON_OMV_TESTS', 'jNeuroML', 'jNeuroML_NEURON', 'jNeuroML_validate', \
            'PyNN_Brian1', 'PyNN_NEURON', 'PyNN_Nest','jNeuroML_validatev1', \
            'PyLEMS_NeuroML2', 'jNeuroML_PyNN_NEURON']

    for engine in engines:
        if len(engine)>0 and not engine in excl:
            print("    Adding %s"%engine)
            info += ' %s;'%engine.replace('Py_neu','neu').replace('jNeuroML','NeuroML').replace('_',arrow)

    if info[-1]==';':
        info = info[:-1]

    info += '\\\\ \\hline \n'

    '''



readme = open('README.md','w')
readme.write(info)
readme.close()
