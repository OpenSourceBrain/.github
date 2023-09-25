import collections

allrefs = collections.OrderedDict()

workflows = {}


allrefs['AllenInstituteNeuroML'] = {'category':'Neocortex','name':'Allen Institute Cell Types DB (Hawrylycz et al. 2016)', 'desc':'Morphologically detailed and point neuron models based on electrophysiological recordings from visual cortex neurons'}
allrefs['Brunel2000'] = {'category':'Neocortex','name':'Brunel (2000)', 'desc':'Spiking network illustrating balance between excitation and inhibition'}
workflows['Brunel2000'] = ['omv-ci.yml','non-omv.yml'] # to test...
allrefs['L5bPyrCellHayEtAl2011'] = {'category':'Neocortex','name':'Hay et al. (2011)','desc':'Layer 5 pyramidal cell model constrained by somatic and dendritic recordings'}
allrefs['IzhikevichModel'] = {'category':'Neocortex','name':'Izhikevich (2003)','desc':'Spiking neuron model reproducing wide range of neuronal activity'}
allrefs['BlueBrainProjectShowcase'] = {'category':'Neocortex','name':'Markram et al. (2015)','desc':'Cell models from Neocortical Microcircuit of Blue Brain Project'}
allrefs['PospischilEtAl2008'] = {'category':'Neocortex','name':'Pospischil et al. (2008)','desc':'HH based model for different classes of cortical and thalamic neurons'}
allrefs['PotjansDiesmann2014'] = {'category':'Neocortex','name':'Potjans and Diesmann (2014)','desc':'Microcircuit model of sensory cortex with 8 populations across 4 layers'}

allrefs['M1NetworkModel'] = {'category':'Neocortex','name':'Dura-Bernal et al. (2017)','desc':'Model of mouse primary motor cortex (M1)'}
allrefs['SadehEtAl2017-InhibitionStabilizedNetworks'] = {'category':'Neocortex','name':'Sadeh et al. (2017)','desc':'Point neuron model of Inhibition Stabilized Network'}
allrefs['SmithEtAl2013-L23DendriticSpikes'] = {'category':'Neocortex','name':'Smith et al. (2013)','desc':'Layer 2/3 cell model used to investigate den- dritic spikes'}
allrefs['Thalamocortical'] = {'category':'Neocortex','name':'Traub et al. (2005)','desc':'Single column network model containing 14 cell populations from cortex and thalamus'}

allrefs['WilsonCowan'] = {'category':'Neocortex','name':'Wilson and Cowan (1972)','desc':'A classic rate based model describing the dynamics and interactions between the excitatory and inhibitory populations of neurons'}
allrefs['del-Molino2017'] = {'category':'Neocortex','name':'del-Molino2017','desc':'Rate based model showing paradoxical response reversal of top-down modulation in cortical circuits with three interneuron types'}
allrefs['MejiasEtAl2016'] = {'category':'Neocortex','name':'MejiasEtAl2016','desc':'A rate based model simulating the dynamics of a cortical laminar structure across multiple scales: intralaminar, interlaminar, interareal and whole cortex'}

allrefs['JoglekarEtAl18'] = 'JoglekarEtAl18' # Need to check status...
allrefs['DemirtasEtAl19'] = 'DemirtasEtAl19' # Need to check status...


allrefs['GranCellLayer'] = {'category':'Cerebellum','name':'Maex and De Schutter (1998)', 'desc':'Cerebellar granule cell layer network'}

allrefs['mbezaire/ca1'] = {'category':'Hippocampus','name': 'Bezaire et al. (2016)', 'desc':'Full scale network model of CA1 region of hippocampus'}
allrefs['FergusonEtAl2013-PVFastFiringCell'] = {'category':'Hippocampus','name': 'Ferguson et al. (2013)', 'desc':'Parvalbumin-positive interneuron from CA1, based on Izhikevich cell model'}
allrefs['FergusonEtAl2014-CA1PyrCell'] = {'category':'Hippocampus','name': 'Ferguson et al. (2014)', 'desc':'Pyramidal cell from CA1, based on Izhikevich cell model'}
allrefs['CA1PyramidalCell'] = {'category':'Hippocampus','name': 'Migliore et al. (2005)', 'desc':'Multicompartmental model of pyramidal cell from CA1 region of hippocampus'}
allrefs['PinskyRinzelModel'] = {'category':'Hippocampus','name': 'Pinsky and Rinzel (1994)', 'desc':'Simplified model of CA3 pyramidal cell'}
allrefs['WangBuzsaki1996'] = {'category':'Hippocampus','name': 'Wang and Buzsaki (1996)', 'desc':'Hippocampal interneuronal network model exhibiting gamma oscillations'}


allrefs['MiglioreEtAl14_OlfactoryBulb3D'] = {'category':'Olfactory bulb','name':'Migliore et al. (2014)', 'desc': 'Large scale 3D olfactory bulb network'}


allrefs['openworm/hodgkin_huxley_tutorial'] = {'category':'Invertebrate','name': 'Hodgkin and Huxley (1952)' , 'desc': 'Classic investigation of the ionic basis of the action potential'}
allrefs['openworm/muscle_model'] = {'category':'Invertebrate','name': 'Boyle and Cohen (2008)' , 'desc': 'Model of body wall muscle from C. elegans'}
allrefs['FitzHugh-Nagumo'] = {'category':'Invertebrate','name': 'FitzHugh (1961)' , 'desc': 'Simplified form of Hodgkin Huxley model'}
allrefs['PyloricNetwork'] = {'category':'Invertebrate','name': 'Prinz et al. (2004)' , 'desc': 'Pyloric network of the lobster stomatogastric ganglion system'}



allrefs['SilverLabUCL/MF-GC-network-backprop-public'] = 'Cayco-Gajic et al. (2017)'
allrefs['GranuleCell'] = 'Maex and De Schutter (1998) GrC'
allrefs['SolinasEtAl-GolgiCell'] = 'Solinas et al. (2007)'
allrefs['VervaekeEtAl-GolgiCellNetwork'] = 'Vervaeke et al. (2010)'






allrefs['NeuroMorpho'] = 'NeuroMorpho.Org'
allrefs['FitzHugh-Nagumo'] = 'FitzHugh-Nagumo'
allrefs['MorrisLecarModel'] = 'MorrisLecarModel'


allrefs['--------------------------'] = '--------------------------'


allrefs['MouseLightShowcase'] = {'category':'Showcases','name':'Janelia MouseLight', 'desc':'Janelia MouseLight project neuronal reconstructions'}
allrefs['NESTShowcase'] = {'category':'Showcases','name':'NEST Showcase', 'desc':'Examples of interactions with simulator NEST'}
allrefs['PyNNShowcase'] = {'category':'Showcases','name':'PyNN Showcase', 'desc':'Examples of interactions between PyNN and NeuroML'}
allrefs['NetPyNEShowcase'] = {'category':'Showcases','name':'NetPyNE Showcase', 'desc':'Examples of interactions between NeuroML and NetPyNE'}
allrefs['SBMLShowcase'] = {'category':'Showcases','name':'SBML Showcase', 'desc':'Examples of interactions between NeuroML and SBML'}

allrefs['BrianShowcase'] = {'category':'Showcases','name':'Brian Showcase', 'desc':'Examples of interactions between NeuroML and Brian'}
allrefs['MOOSEShowcase'] = {'category':'Showcases','name':'MOOSE Showcase', 'desc':'Examples of interactions between NeuroML and MOOSE'}
allrefs['ArborShowcase'] = {'category':'Showcases','name':'Arbor Showcase', 'desc':'Examples of interactions between NeuroML and Arbor'}
allrefs['EDENShowcase'] = {'category':'Showcases','name':'EDEN Showcase', 'desc':'Examples of interactions between NeuroML and EDEN'}

allrefs['TheVirtualBrainShowcase'] = {'category':'Showcases','name':'The Virtual Brain Showcase', 'desc':'Examples of interactions between NeuroML and TVB'}
allrefs['NEURONShowcase'] = {'category':'Showcases','name':'NEURON Showcase', 'desc':'Examples of interactions between NeuroML and NEURON'}

allrefs['neuroConstructShowcase'] = {'category':'Showcases','name':'neuroConstructShowcase', 'desc':'Examples of neuroConstruct projects'}

allrefs['NSGPortalShowcase'] = {'category':'Showcases','name':'NSGPortalShowcase', 'desc':'Interactions with Neuroscience Gateway'}
workflows['NSGPortalShowcase'] = []

allrefs['BindsNETShowcase'] = 'BindsNETShowcase'   # No example code yet...
allrefs['PsyNeuLinkShowcase'] = 'PsyNeuLinkShowcase'   # All working examples moved to MDF repo...
allrefs['NWBShowcase'] = 'NWBShowcase'     # No NeuroML in here...
workflows['NWBShowcase'] = ['ci.yml']
allrefs['ConnectivityShowcase'] = 'ConnectivityShowcase'  # No real simulator there...

allrefs['VERTEXShowcase'] = 'VERTEXShowcase'  # No longer maintained...
allrefs['StochasticityShowcase'] = 'StochasticityShowcase' # Not really a sim focussed showcase...

# allrefs['ONNXShowcase'] = 'ONNXShowcase'  # All working examples moved to MDF repo...
# allrefs['CSAShowcase'] = 'CSAShowcase'  # No longer maintained...

allrefs['ghk-nernst'] = 'ghk-nernst'

allrefs['-------------------------'] = '--------------------------'

allrefs['Drosophila_Projection_Neuron'] = 'Drosophila_Projection_Neuron'
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
allrefs['VogelsEtAl2011'] = 'VogelsEtAl2011'
allrefs['WeilerEtAl08-LaminarCortex'] = 'WeilerEtAl08-LaminarCortex'
allrefs['MultiscaleISN'] = 'MultiscaleISN'
allrefs['HNN'] = 'HNN'





allrefs['NeuroElectroSciUnit'] = 'NeuroElectroSciUnit'
allrefs['NengoNeuroML'] = 'NengoNeuroML'
allrefs['SynapticIntegration'] = 'SynapticIntegration'
allrefs['SinusoidalVoltageProtocols'] = 'SinusoidalVoltageProtocols'



###########allrefs['korngreen-pyramidal'] = 'Almog and Korngreen, 2014'
