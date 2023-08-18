import collections


allrefs = collections.OrderedDict()

'''
{'category':'Neocortex','name':'XXX', desc:''}
'''

allrefs['AllenInstituteNeuroML'] = {'category':'Neocortex','name':'Allen Institute Cell Types DB (Hawrylycz et al. 2016)', 'desc':'Morphologically detailed and point neuron models based on electrophysiological recordings from visual cortex neurons'}
allrefs['Brunel2000'] = {'category':'Neocortex','name':'Brunel (2000)', 'desc':'Spiking network illustrating balance between excitation and inhibition'}
allrefs['L5bPyrCellHayEtAl2011'] = {'category':'Neocortex','name':'Hay et al. (2011)','desc':'Layer 5 pyramidal cell model constrained by somatic and dendritic recordings'}
allrefs['IzhikevichModel'] = {'category':'Neocortex','name':'Izhikevich (2003)','desc':'Spiking neuron model reproducing wide range of neuronal activity'}
allrefs['BlueBrainProjectShowcase'] = {'category':'Neocortex','name':'Markram et al. (2015)','desc':'Cell models from Neocortical Microcircuit of Blue Brain Project'}
allrefs['PospischilEtAl2008'] = {'category':'Neocortex','name':'Pospischil et al. (2008)','desc':'HH based model for different classes of cor- tical and thalamic neurons'}

allrefs['PotjansDiesmann2014'] = 'Potjans and Diesmann (2014)'

allrefs['M1NetworkModel'] = 'Dura-Bernal et al. (2017)'
allrefs['SadehEtAl2017-InhibitionStabilizedNetworks'] = 'Sadeh et al. (2017)'
allrefs['SmithEtAl2013-L23DendriticSpikes'] = 'Smith et al. (2013)'
#allrefs['VERTEXShowcase'] = 'Tomsett et al. (2014)'
allrefs['Thalamocortical'] = 'Traub et al. (2005)'
allrefs['del-Molino2017'] = 'del-Molino2017'
allrefs['WilsonCowan'] = 'WilsonCowan'
allrefs['MejiasEtAl2016'] = 'MejiasEtAl2016'
allrefs['JoglekarEtAl18'] = 'JoglekarEtAl18'
allrefs['DemirtasEtAl19'] = 'DemirtasEtAl19'



allrefs['GranCellLayer'] = {'category':'Cerebellum','name':'Maex and De Schutter (1998)', 'desc':'Cerebellar granule cell layer network'}

allrefs['SilverLabUCL/MF-GC-network-backprop-public'] = 'Cayco-Gajic et al. (2017)'
allrefs['GranuleCell'] = 'Maex and De Schutter (1998) GrC'
allrefs['SolinasEtAl-GolgiCell'] = 'Solinas et al. (2007)'
allrefs['VervaekeEtAl-GolgiCellNetwork'] = 'Vervaeke et al. (2010)'


allrefs['mbezaire/ca1'] = 'Bezaire et al. (2016)'
allrefs['FergusonEtAl2013-PVFastFiringCell'] = 'Ferguson et al. (2013)'
allrefs['CA1PyramidalCell'] = 'Migliore et al. (2005)'
allrefs['PinskyRinzelModel'] = 'Pinsky and Rinzel (1994)'
allrefs['WangBuzsaki1996'] = 'Wang and Buzsaki (1996)'


allrefs['MiglioreEtAl14_OlfactoryBulb3D'] = 'Migliore et al. (2014)'


allrefs['openworm/muscle_model'] = 'Boyle and Cohen (2008)'
allrefs['FitzHugh-Nagumo'] = 'FitzHugh (1961)'
allrefs['openworm/hodgkin_huxley_tutorial'] = 'Hodgkin and Huxley (1952)'
allrefs['PyloricNetwork'] = 'Prinz et al. (2004)'
allrefs['NeuroMorpho'] = 'NeuroMorpho.Org'
allrefs['FitzHugh-Nagumo'] = 'FitzHugh-Nagumo'
allrefs['MorrisLecarModel'] = 'MorrisLecarModel'


allrefs['--------------------------'] = '--------------------------'


allrefs['MouseLightShowcase'] = {'category':'Showcases','name':'Janelia MouseLight', 'desc':'Janelia MouseLight project neuronal reconstructions'}
allrefs['NESTShowcase'] = {'category':'Showcases','name':'NESTShowcase', 'desc':'Examples of interactions with simulator NEST'}
allrefs['PyNNShowcase'] = {'category':'Showcases','name':'PyNNShowcase', 'desc':'Examples of interactions between PyNN and NeuroML'}
allrefs['NetPyNEShowcase'] = {'category':'Showcases','name':'NetPyNEShowcase', 'desc':'Examples of interactions between NeuroML and NetPyNE'}
allrefs['SBMLShowcase'] = {'category':'Showcases','name':'SBMLShowcase', 'desc':'Examples of interactions between NeuroML and SBML'}


allrefs['BrianShowcase'] = 'BrianShowcase'
allrefs['MOOSEShowcase'] = 'MOOSEShowcase'
allrefs['ArborShowcase'] = 'ArborShowcase'
allrefs['EDENShowcase'] = 'EDENShowcase'
allrefs['BindsNETShowcase'] = 'BindsNETShowcase'
allrefs['NWBShowcase'] = 'NWBShowcase'
allrefs['ConnectivityShowcase'] = 'ConnectivityShowcase'
allrefs['TheVirtualBrainShowcase'] = 'TheVirtualBrainShowcase'
allrefs['PsyNeuLinkShowcase'] = 'PsyNeuLinkShowcase'
allrefs['NEURONShowcase'] = 'NEURONShowcase'

allrefs['-------------------------'] = '--------------------------'

allrefs['Drosophila_Projection_Neuron'] = 'Drosophila_Projection_Neuron'
allrefs['FergusonEtAl2014-CA1PyrCell'] = 'FergusonEtAl2014-CA1PyrCell'
allrefs['FergusonEtAl2013-PVFastFiringCell'] = 'FergusonEtAl2013-PVFastFiringCell'
allrefs['NorenbergEtAl2010_DGBasketCell'] = 'NorenbergEtAl2010_DGBasketCell'
allrefs['DentateGyrus2005'] = 'DentateGyrus2005'
allrefs['StriatalSpinyProjectionNeuron'] = 'StriatalSpinyProjectionNeuron'
allrefs['OlfactoryTest'] = 'OlfactoryTest'
allrefs['CerebellarNucleusNeuron'] = 'CerebellarNucleusNeuron'
allrefs['GranCellRothmanIf'] = 'GranCellRothmanIf'
allrefs['PurkinjeCell'] = 'PurkinjeCell'
allrefs['Cerebellum3DDemo'] = 'Cerebellum3DDemo'
allrefs['GranularLayerSolinasNieusDAngelo2010'] = 'GranularLayerSolinasNieusDAngelo2010'
allrefs['epiasini/BillingsEtAl2014_GCL_Models'] = 'BillingsEtAl2014_GCL_Models'
allrefs['MainenEtAl_PyramidalCell'] = 'MainenEtAl_PyramidalCell'
allrefs['RothmanEtAl_KoleEtAl_PyrCell'] = 'RothmanEtAl_KoleEtAl_PyrCell'
allrefs['LarkumEtAl2009'] = 'LarkumEtAl2009'
allrefs['FarinellaEtAl_NMDAspikes'] = 'FarinellaEtAl_NMDAspikes'
allrefs['korngreen-pyramidal'] = 'korngreen-pyramidal'
allrefs['dLGNinterneuronHalnesEtAl2011'] = 'dLGNinterneuronHalnesEtAl2011'
allrefs['L23PyramidalCellTutorial'] = 'L23PyramidalCellTutorial'
allrefs['EbnerEtAl2019'] = 'EbnerEtAl2019'
allrefs['BahlEtAl2012_ReducedL5PyrCell'] = 'BahlEtAl2012_ReducedL5PyrCell'
allrefs['V1NetworkModels'] = 'V1NetworkModels'
allrefs['VERTEXShowcase'] = 'VERTEXShowcase'
allrefs['VogelsEtAl2011'] = 'VogelsEtAl2011'
allrefs['WeilerEtAl08-LaminarCortex'] = 'WeilerEtAl08-LaminarCortex'
allrefs['MultiscaleISN'] = 'MultiscaleISN'
allrefs['HNN'] = 'HNN'




allrefs['NSGPortalShowcase'] = 'NSGPortalShowcase'
allrefs['NeuroElectroSciUnit'] = 'NeuroElectroSciUnit'
allrefs['NengoNeuroML'] = 'NengoNeuroML'
allrefs['StochasticityShowcase'] = 'StochasticityShowcase'
allrefs['SynapticIntegration'] = 'SynapticIntegration'
allrefs['SinusoidalVoltageProtocols'] = 'SinusoidalVoltageProtocols'
allrefs['ONNXShowcase'] = 'ONNXShowcase'


allrefs['CSAShowcase'] = 'CSAShowcase'
allrefs['neuroConstructShowcase'] = 'neuroConstructShowcase'
allrefs['ghk-nernst'] = 'ghk-nernst'




###########allrefs['korngreen-pyramidal'] = 'Almog and Korngreen, 2014'

all_cells = collections.OrderedDict()



#all_cells['Traub_DeepAxAx'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/DeepAxAx.cell.nml'

all_cells['L23_Smith'] = './coreprojects/SmithEtAl2013-L23DendriticSpikes/NeuroML2/L23_NoHotSpot.cell.nml', 'Smith et al. (2013<br/OLM cell', '#F3F3F3', '35degC', [-0.1, -0.05, 0, 0.25, 0.4]

all_cells['Pospi_LTS'] = './coreprojects/PospischilEtAl2008/NeuroML2/cells/LTS/LTS.cell.nml','Pospischil et al. (2008<br/>Low Threshold Spiking cell', '#F3F3F3', '36degC', [-0.025, -0.0125, 0, 0.05, 0.2]

all_cells['SolinasEtAl-GolgiCell'] = './coreprojects/SolinasEtAl-GolgiCell/NeuroML2/Golgi.cell.nml','Solinas et al. 2007<br/>Cerebellar Golgi Cell', '#FFB380', '23degC', [-0.025, -0.0125, 0, 0.03, 0.05]

all_cells['ca1'] = 'coreprojects/ca1/NeuroML2/cells/olm.cell.nml', 'Bezaire et al. 2016<br/>OLM interneuron', '#FFE680', '34degC', [-0.1, -0.05, 0, 0.05, 0.1]

# High rheobase: 700 pA...
#all_cells['mitral'] = 'coreprojects/MiglioreEtAl14_OlfactoryBulb3D/NeuroML2/MitralCells/Exported/Mitral_0_0.cell.nml', 'Migliore et al. 2005<br/>Mitral cell', '#C6E4E4', '35degC', [-0.1, -0.05, 0, 0.25, 0.5]

all_cells['HH'] = './coreprojects/hodgkin_huxley_tutorial/Tutorial/Source/hhcell.cell.nml', 'Hodgkin and Huxley, 1952<br/>Single compartment cell', 'D3BC5F', '6.3degC', [-0.025, -0.0125, 0, 0.03, 0.075]

all_cells['Pyloric_LP'] = './coreprojects/PyloricNetwork/neuroConstruct/generatedNeuroML2/LP.cell.nml','Prinz et al. 2004<br/>Lateral Pyloric (LP) neuron', 'D3BC5F', '10degC', [-0.1, -0.05, 0, 0.03, 0.1]

#all_cells['Pospi_FS'] = './coreprojects/PospischilEtAl2008/NeuroML2/cells/FS/FS.cell.nml'

########   Problem with H channel???
#all_cells['GranuleCell'] = './coreprojects/GranuleCell/neuroConstruct/generatedNeuroML2/Granule_98.cell.nml'


##all_cells['Pospi_RS'] = './coreprojects/PospischilEtAl2008/NeuroML2/cells/RS/RS.cell.nml'


#all_cells['FitzHughNagumo'] = './coreprojects/FitzHugh-Nagumo/NeuroML2/FN.cell.nml'

#all_cells['L5PC_Hay'] = './coreprojects/L5bPyrCellHayEtAl2011/neuroConstruct/generatedNeuroML2/L5PC.cell.nml'
#all_cells['CA1'] = './coreprojects/CA1PyramidalCell/neuroConstruct/generatedNeuroML2/CA1.cell.nml'
#all_cells['Traub_L23PyrFRB'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/L23PyrFRB.cell.nml'

'''
all_cells['Traub_DeepAxAx'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/DeepAxAx.cell.nml'
all_cells['Traub_L5TuftedPyrRS'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/L5TuftedP
all_cells['Traub_DeepAxAx'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/DeepAxAx.cell.nml'yrRS.cell.nml'
all_cells['Traub_DeepLTSInter'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/DeepLTSInter.cell.nml'
all_cells['Traub_SupBasket'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/SupBasket.cell.nml'
all_cells['Traub_SupLTSInter'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/SupLTSInter.cell.nml'
all_cells['Traub_L5TuftedPyrIB'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/L5TuftedPyrIB.cell.nml'
all_cells['Traub_SupAxAx'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/SupAxAx.cell.nml'
all_cells['Traub_L23PyrRS'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/L23PyrRS.cell.nml'
all_cells['Traub_nRT'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/nRT.cell.nml'
all_cells['Traub_DeepBasket'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/DeepBasket.cell.nml'
all_cells['Traub_TCR'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/TCR.cell.nml'
all_cells['Traub_L6NonTuftedPyrRS'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/L6NonTuftedPyrRS.cell.nml'
all_cells['Traub_L4SpinyStellate'] = './coreprojects/Thalamocortical/neuroConstruct/generatedNeuroML2/L4SpinyStellate.cell.nml'
all_cells['L23_Smith'] = './coreprojects/SmithEtAl2013-L23DendriticSpikes/NeuroML2/L23_NoHotSpot.cell.nml'
'''
