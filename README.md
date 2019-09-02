# crab_MC_Generation
GEN-SIM generation

```
cmsrel CMSSW_10_2_3
cd CMSSW_10_2_3/src
git@github.com:gourangakole/crab_MC_Generation.git
crab submit -c crabConfig_B2G-RunIIFall18GS-00005.py
```

# DIGI-RECO step

start with fresh shell
login to lxplus7

```
ssh -Y username@lxplus7.cern.ch
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src/
cmsenv
git@github.com:gourangakole/crab_MC_Generation.git
cd crab_MC_Generation/DIGI-RECO
cmsRun config_DIGI102X_step1.py #look at the input GENSIM file 
cmsRun config_DIGI102X_step2.py #look at the input file that generated in step1
```

# MiniAOD step

start with fresh shell
login to lxplus7

```
ssh -Y username@lxplus7.cern.ch
cmsrel CMSSW_10_2_5
cd CMSSW_10_2_5/src/
cmsenv
git@github.com:gourangakole/crab_MC_Generation.git
cd crab_MC_Generation/MiniAOD
cmsRun config_MiniAOD.py #look at the input AOD file that is generated in DIGI-RECO step2
```

# NanoAOD step

start with fresh shell
login to lxplus7

```
ssh -Y username@lxplus7.cern.ch
cmsrel CMSSW_10_2_15
cd CMSSW_10_2_15/src/
cmsenv
git@github.com:gourangakole/crab_MC_Generation.git
cd crab_MC_Generation/NanoAODv5
cmsRun config_NanoAODv5.py #look at the input MINIAOD file that is generated in MiniAOD step
```

