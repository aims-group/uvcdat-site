import vcs,cdms2,os,sys

x=vcs.init()



f=cdms2.open(os.path.join(sys.prefix,"sample_data","ta_ncep_87-6-88-4.nc"))

vr = "ta"
s=f(vr,slice(0,1),longitude=slice(90,91),squeeze=1)
x.plot(s)
fnm = "test_vcs_flipY.png"
x.png(fnm)
