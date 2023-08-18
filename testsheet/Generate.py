
from ModelInfo import allrefs, workflows
import os

info = """
## Tests on OSB models
"""

YES = ' \\multicolumn{1}{c}{Yes} '
YES = ' \\ding{51} '

categories = ['Neocortex', 'Cerebellum', 'Showcases']


for category in categories:
    info += "[%s](#%s) | "%(category, category.lower())

info += "[Others](#others) "

for category in categories:

    info += """
    \n### %s\n"""%category


    info += '  | Model | Tests | Pull requests |\n'
    info += '  |----------|:------:|:------:|\n'

    for directory in allrefs.keys():
        allinfo = allrefs[directory]

        if type(allinfo)==dict and allinfo['category']==category:

            print("Looking at: %s in %s"%(allinfo, directory))

            name = allinfo['name']
            desc = allinfo['desc']

            gh = 'OpenSourceBrain/%s'%directory if not '/' in directory else directory

            info += ' | <a href="https://github.com/%s">%s</a><br/><i><sup>%s</sup></i> |'%(gh,name, desc)

            if directory in workflows:

                for wf in workflows[directory]:
                    info += '  [![%s](https://github.com/%s/actions/workflows/%s/badge.svg)](https://github.com/%s/actions/workflows/%s) '%(wf,gh,wf,gh,wf)

                info += ' |' 

            else:
                info += ' |' if '--' in directory else \
                        '  [![OMV](https://github.com/%s/actions/workflows/omv-ci.yml/badge.svg)](https://github.com/%s/actions/workflows/omv-ci.yml) '%(gh,gh) \
                        + '  [![ ](https://github.com/%s/actions/workflows/non-omv.yml/badge.svg)](https://github.com/%s/actions/workflows/non-omv.yml) | '%(gh,gh)

            info += ' |\n' if '--' in directory else \
                    '  [![GitHub pull requests](https://img.shields.io/github/issues-pr/%s)](https://github.com/%s/pulls) | \n'%(gh,gh)

    info += '  </table>\n'



info += """
### Others
"""

count = 0

info += '  | Model | Tests | Pull requests |\n'
info += '  |----------|:------:|:------:|\n'
for directory in allrefs.keys():
    ref = allrefs[directory]

    if type(ref) == str:
        print("Looking at: %s in %s"%(ref, directory))


        gh = 'OpenSourceBrain/%s'%directory if not '/' in directory else directory

        info += ' | <a href="https://github.com/%s">%s</a> |'%(gh,ref)

        if directory in workflows:

                for wf in workflows[directory]:
                    info += '  [![%s](https://github.com/%s/actions/workflows/%s/badge.svg)](https://github.com/%s/actions/workflows/%s) '%(wf,gh,wf,gh,wf)

                info += ' |' 
        else:
            info += ' |' if '--' in directory else \
                    '  [![OMV](https://github.com/%s/actions/workflows/omv-ci.yml/badge.svg)](https://github.com/%s/actions/workflows/omv-ci.yml) '%(gh,gh) \
                    + '  [![ ](https://github.com/%s/actions/workflows/non-omv.yml/badge.svg)](https://github.com/%s/actions/workflows/non-omv.yml) | '%(gh,gh)

        info += ' |\n' if '--' in directory else \
                '  [![GitHub pull requests](https://img.shields.io/github/issues-pr/%s)](https://github.com/%s/pulls) | \n'%(gh,gh)

        count+=1

info += '  </table>\n'


readme = open('README.md','w')
readme.write(info)
readme.close()
