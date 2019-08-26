from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'request_TprimeTPrimeTotGammatGluon_cfg_GEN-SIM_2019-08-17'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'B2G-RunIIFall18GS-00005_3_cfg.py'
config.JobType.numCores = 8

config.Data.outputPrimaryDataset = 'TprimeTPrimeTotGammatGluon'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = config.Data.unitsPerJob * 1000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'TprimeTPrimeTotGammatGluon_cfg_GEN-SIM'

config.Site.storageSite = 'T2_US_UCSD'
#config.Site.blacklist = ['T3_US_Baylor']
