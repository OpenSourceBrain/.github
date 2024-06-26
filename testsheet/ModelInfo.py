import collections

allrefs = collections.OrderedDict()

workflows = {}


allrefs['AllenInstituteNeuroML'] = {'category':'Neocortex','name':'Allen Institute Cell Types DB (Hawrylycz et al. 2016)', 'desc':'Morphologically detailed and point neuron models based on electrophysiological recordings from visual cortex neurons', 'cite':'Billeh2020'}
allrefs['Brunel2000'] = {'category':'Neocortex','name':'Brunel (2000)', 'desc':'Spiking network illustrating balance between excitation and inhibition', 'cite':'Brunel2000'}
workflows['Brunel2000'] = ['omv-ci.yml','non-omv.yml'] # to test...
allrefs['L5bPyrCellHayEtAl2011'] = {'category':'Neocortex','name':'Hay et al. (2011)','desc':'Layer 5 pyramidal cell model constrained by somatic and dendritic recordings', 'cite':'Hay2011'}
allrefs['IzhikevichModel'] = {'category':'Neocortex','name':'Izhikevich (2003)','desc':'Spiking neuron model reproducing wide range of neuronal activity', 'cite':'Izhikevich2004'}
allrefs['BlueBrainProjectShowcase'] = {'category':'Neocortex','name':'Markram et al. (2015)','desc':'Cell models from Neocortical Microcircuit of Blue Brain Project', 'cite':'Markram2015'}
allrefs['PospischilEtAl2008'] = {'category':'Neocortex','name':'Pospischil et al. (2008)','desc':'HH based models for different classes of cortical and thalamic neurons', 'cite':'Pospischil2008'}
allrefs['PotjansDiesmann2014'] = {'category':'Neocortex','name':'Potjans and Diesmann (2014)','desc':'Microcircuit model of sensory cortex with 8 populations across 4 layers', 'cite':'Potjans2014'}

allrefs['M1NetworkModel'] = {'category':'Neocortex','name':'Dura-Bernal et al. (2017)','desc':'Model of mouse primary motor cortex (M1)', 'cite':'DuraBernal2017'}
allrefs['SadehEtAl2017-InhibitionStabilizedNetworks'] = {'category':'Neocortex','name':'Sadeh et al. (2017)','desc':'Point neuron model of Inhibition Stabilized Network', 'cite':'Sadeh2017'}
allrefs['SmithEtAl2013-L23DendriticSpikes'] = {'category':'Neocortex','name':'Smith et al. (2013)','desc':'Layer 2/3 cell model used to investigate dendritic spikes', 'cite':'Smith2013'}
allrefs['Thalamocortical'] = {'category':'Neocortex','name':'Traub et al. (2005)','desc':'Single column network model containing 14 cell populations from cortex and thalamus', 'cite':'Traub2005'}

allrefs['BahlEtAl2012_ReducedL5PyrCell'] = {'category':'Neocortex','name':'Bahl et al. (2012)','desc':'A set of reduced models of layer 5 pyramidal neurons', 'cite':'BAHL2012'}

allrefs['WilsonCowan'] = {'category':'Neocortex','name':'Wilson and Cowan (1972)','desc':'A classic rate based model describing the dynamics and interactions between the excitatory and inhibitory populations of neurons', 'cite':'WilsonCowan'}
allrefs['del-Molino2017'] = {'category':'Neocortex','name':'del-Molino2017','desc':'Rate based model showing paradoxical response reversal of top-down modulation in cortical circuits with three interneuron types', 'cite':'delMolino2017'}
allrefs['MejiasEtAl2016'] = {'category':'Neocortex','name':'MejiasEtAl2016','desc':'A rate based model simulating the dynamics of a cortical laminar structure across multiple scales: intralaminar, interlaminar, interareal and whole cortex', 'cite':'Mejias2016'}

allrefs['JoglekarEtAl18'] = 'JoglekarEtAl18' # Need to check status...
allrefs['DemirtasEtAl19'] = 'DemirtasEtAl19' # Need to check status...
allrefs['MultiscaleISN'] = 'MultiscaleISN' # Need to check status...


allrefs['GranuleCell'] = {'category':'Cerebellum','name': 'Maex and De Schutter (1998) (GrC)', 'desc':'Cerebellar granule cell', 'cite':'Maex1998'}
allrefs['SilverLabUCL/MF-GC-network-backprop-public'] = {'category':'Cerebellum','name': 'Cayco-Gajic et al. (2017)', 'desc':'Cerebellar granule cell layer network', 'cite':'Cayco-Gajic2017'}
allrefs['GranCellLayer'] = {'category':'Cerebellum','name':'Maex and De Schutter (1998)', 'desc':'3D Cerebellar granule cell layer network', 'cite':'Maex1998'}
allrefs['SolinasEtAl-GolgiCell'] = {'category':'Cerebellum','name': 'Solinas et al. (2007)', 'desc':'Cerebellar Golgi cell model', 'cite':'Solinas07a'}
allrefs['VervaekeEtAl-GolgiCellNetwork'] = {'category':'Cerebellum','name': 'Vervaeke et al. (2010)', 'desc':'Electrically connected cerebellar Golgi cell network model', 'cite':'Vervaeke10'}



allrefs['mbezaire/ca1'] = {'category':'Hippocampus','name': 'Bezaire et al. (2016)', 'desc':'Full scale network model of CA1 region of hippocampus', 'cite':'Bezaire2016'}
allrefs['FergusonEtAl2013-PVFastFiringCell'] = {'category':'Hippocampus','name': 'Ferguson et al. (2013)', 'desc':'Parvalbumin-positive interneuron from CA1, based on Izhikevich cell model', 'cite':'Ferguson2013'}
allrefs['FergusonEtAl2014-CA1PyrCell'] = {'category':'Hippocampus','name': 'Ferguson et al. (2014)', 'desc':'Pyramidal cell from CA1, based on Izhikevich cell model', 'cite':'Ferguson2014'}
allrefs['CA1PyramidalCell'] = {'category':'Hippocampus','name': 'Migliore et al. (2005)', 'desc':'Multicompartmental model of pyramidal cell from CA1 region of hippocampus', 'cite':'Migliore2005'}
allrefs['PinskyRinzelModel'] = {'category':'Hippocampus','name': 'Pinsky and Rinzel (1994)', 'desc':'Simplified model of CA3 pyramidal cell', 'cite':'Pinsky1994'}
allrefs['WangBuzsaki1996'] = {'category':'Hippocampus','name': 'Wang and Buzsaki (1996)', 'desc':'Hippocampal interneuronal network model exhibiting gamma oscillations', 'cite':'WangBuzsaki1996'}


allrefs['MiglioreEtAl14_OlfactoryBulb3D'] = {'category':'Olfactory bulb','name':'Migliore et al. (2014)', 'desc': 'Large scale 3D olfactory bulb network with detailed mitral cells and granule cells', 'cite':'Migliore2014'}

allrefs['openworm/hodgkin_huxley_tutorial'] = {'category':'Invertebrate','name': 'Hodgkin and Huxley (1952)' , 'desc': 'Classic investigation of the ionic basis of the action potential', 'cite':'Hodgkin1952'}
allrefs['FitzHugh-Nagumo'] = {'category':'Invertebrate','name': 'FitzHugh (1961)' , 'desc': 'Simplified form of Hodgkin Huxley model', 'cite':'FitzHugh1961'}
allrefs['PyloricNetwork'] = {'category':'Invertebrate','name': 'Prinz et al. (2004)' , 'desc': 'Pyloric network of the lobster stomatogastric ganglion system', 'cite':'Prinz2004'}
allrefs['openworm/muscle_model'] = {'category':'Invertebrate','name': 'Boyle and Cohen (2008)' , 'desc': 'Model of body wall muscle from C. elegans', 'cite':'Boyle2008'}
allrefs['openworm/c302'] = {'category':'Invertebrate','name': 'Gleeson et al. (2018)' , 'desc': 'A multiscale framework for modelling the nervous system of C. elegans', 'cite':'Gleeson2018'}


allrefs['MorrisLecarModel'] = {'category':'General','name':'Morris and Lecar (1981)', 'desc': 'Two dimensional reduced neuron model with calcium and potassium conductances', 'cite':'Morris1981'}
allrefs['HindmarshRose1984'] = {'category':'General','name':'Hindmarsh and Rose (1984)', 'desc': 'A simplified point cell model which captures complex firing patterns of single neurons, such as periodic and chaotic bursting', 'cite':'HindmarshRose1984'}

allrefs['ghk-nernst'] = 'ghk-nernst'



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

allrefs['neuroConstructShowcase'] = {'category':'Showcases','name':'neuroConstruct Showcase', 'desc':'Examples of neuroConstruct projects'}

allrefs['NeuroMorpho'] = {'category':'Showcases','name':'NeuroMorpho.Org', 'desc':'Examples of reconstructions from NeuroMorpho.Org'}

allrefs['MouseLightShowcase'] = {'category':'Showcases','name':'Janelia MouseLight', 'desc':'Janelia MouseLight project neuronal reconstructions'}
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
allrefs['V1NetworkModels'] = 'V1NetworkModels'
allrefs['VogelsEtAl2011'] = 'VogelsEtAl2011'
allrefs['WeilerEtAl08-LaminarCortex'] = 'WeilerEtAl08-LaminarCortex'
allrefs['HNN'] = 'HNN'


allrefs['NeuroElectroSciUnit'] = 'NeuroElectroSciUnit'
allrefs['NengoNeuroML'] = 'NengoNeuroML'
allrefs['SynapticIntegration'] = 'SynapticIntegration'
allrefs['SinusoidalVoltageProtocols'] = 'SinusoidalVoltageProtocols'



###########allrefs['korngreen-pyramidal'] = 'Almog and Korngreen, 2014'
