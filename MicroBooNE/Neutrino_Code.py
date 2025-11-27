import pickle
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

with open('Simulation.pkl', 'rb') as infile:
  simdata = pickle.load(infile)

with open('Data.pkl', 'rb') as infile:
  data = pickle.load(infile)

for variable_name in list(simdata):
  print(variable_name)

#%%
for name in simdata.columns:
    plt.hist(simdata[name], bins=100, density=True)
    plt.xlabel(name)
    plt.ylabel('Candidates')
    plt.show()

#%%
#Simulation category of 21, it is a muon neutrino charge current interaction
#Each event is given a "weight" that represents its relative contriubution.
#The number of interactions is then the sum of the weights not the sum of the entries

plt.hist(simdata[(simdata['Simulation category'] == 21)]['Simulated neutrino energy'], bins=100, density=True, label='No weights')
plt.hist(simdata[(simdata['Simulation category'] == 21)]['Simulated neutrino energy'], bins=100, density=True, weights=simdata[simdata['Simulation category'] == 21]['Simulation weight'], label='With weights')
plt.xlabel('Simulated neutrino energy [GeV]')
plt.ylabel('Candidates')
plt.legend()
plt.show()

#%% comparing background to signal for simulated neutrino energy -- test for next part
plt.hist(simdata[(simdata['Simulation category'] == 21)]['Simulated neutrino energy'], bins=100, density=True, label='Simulated Neutrino Energy')
plt.hist(simdata[(simdata['Simulation category'] != 21)]['Simulated neutrino energy'], bins=100, density=True, label='Background')
plt.xlabel('Simulated neutrino energy [GeV]')
plt.ylabel('Candidates')
plt.show()

#%% expanding previous break to all categories
sig = simdata[simdata['Simulation category'] == 21]     # neutrino
bkg = simdata[simdata['Simulation category'] != 21]     # background

for name in simdata.columns:
    plt.hist(bkg[name], bins=100, density=True, alpha=1, label='Background')
    plt.hist(sig[name], bins=100, density=True, alpha=0.9, label='Signal')
    
    plt.xlabel(name)
    plt.ylabel('Normalised counts')
    plt.legend()
    plt.show()

#%% cutting misreconstruction events based on nonsensical energy
ecut_sig = sig[(sig['Total energy'] < 8000) & (sig['Simulated neutrino flight distance'] > 100)]
ecut_bkg = bkg[(bkg['Total energy'] < 8000) & (bkg['Simulated neutrino flight distance'] > 100)]

for name in simdata.columns:
    plt.hist(ecut_bkg[name], bins=100, density=True, alpha=1, label='Background')
    plt.hist(ecut_sig[name], bins=100, density=True, alpha=0.9, label='Signal')
    
    plt.xlabel(name)
    plt.ylabel('Normalised counts')
    plt.legend()
    plt.show()

#%% checking if cut affects signal data
plt.hist(sig['Simulated neutrino energy'], bins=np.linspace(0,7,100), density=True, label='Signal')
plt.hist(ecut_sig['Simulated neutrino energy'], bins=np.linspace(0,7,100), density=True, label='E_Cut Signal', alpha = 0.9)
plt.xlabel('Simulated neutrino energy [GeV]')
plt.ylabel('Candidates')
plt.legend()
plt.show()