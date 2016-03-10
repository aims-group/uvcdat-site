---
title: Changelog
layout: default

---

<a name="2.4"></a>

# 2.4 Changelog

[New Features Documentation](/releases/2.4_features.html)

## Closed Issues

### ACME

 * **Bug**: [average() indentation error](https://github.com/UV-CDAT/uvcdat/issues/1048)

### Build

 * **Bug**: [sample data doesn't get re-downloaded if it's deleted](https://github.com/UV-CDAT/uvcdat/issues/133)
 * **Bug**: ["This warning is for project developers" message during ccmake?](https://github.com/UV-CDAT/uvcdat/issues/462)
 * **Bug**: [Sample data is all over the place](https://github.com/UV-CDAT/uvcdat/issues/1362)
 * **Bug**: [-DBUILD_PARALLEL=ON fails on mac (at least)](https://github.com/UV-CDAT/uvcdat/issues/667)
 * **Bug**: [cdms2 not building in current master](https://github.com/UV-CDAT/uvcdat/issues/1498)
 * **Bug**: [runtest does not understand mpi -n arg](https://github.com/UV-CDAT/uvcdat/issues/1499) ([#1500](https://github.com/UV-CDAT/uvcdat/pull/1500))
 * **Bug**: [Error building pyOpenSSL on OSX](https://github.com/UV-CDAT/uvcdat/issues/1084)
 * **Bug**: [CMake not able to find gfortran installed via apt-get](https://github.com/UV-CDAT/uvcdat/issues/1628)
 * **Bug**: [SciPy fails to build on CentOS 6.6](https://github.com/UV-CDAT/uvcdat/issues/1192)
 * **Bug**: [openssl cmake error on RHEA](https://github.com/UV-CDAT/uvcdat/issues/1751) ([#1756](https://github.com/UV-CDAT/uvcdat/pull/1756))
 * **Bug**: [Fonts not installed at the right location on Mac OSX](https://github.com/UV-CDAT/uvcdat/issues/1483)
 * **Bug**: [pip/easy_install error in some build](https://github.com/UV-CDAT/uvcdat/issues/1486)
 * **Bug**: [Fix travis pyexpat build time error](https://github.com/UV-CDAT/uvcdat/issues/1263) ([#1674](https://github.com/UV-CDAT/uvcdat/pull/1674))
 * **Bug**: [VTK build error not reported to CDash](https://github.com/UV-CDAT/uvcdat/issues/1317)
 * **Bug**: [pep8 executable looked for in wrong place on mac](https://github.com/UV-CDAT/uvcdat/issues/1386) ([#1387](https://github.com/UV-CDAT/uvcdat/pull/1387))
 * **Bug**: [flake8 not properly added to repo](https://github.com/UV-CDAT/uvcdat/issues/1425) ([#1430](https://github.com/UV-CDAT/uvcdat/pull/1430))
 * **Bug**: [fetching uvcdat-testdata broken on mac](https://github.com/UV-CDAT/uvcdat/issues/1427)
 * **Bug**: [older git checkout error](https://github.com/UV-CDAT/uvcdat/issues/1355)
 * **Bug**: [system picks up wrong pip when building ipython and tornado ](https://github.com/UV-CDAT/uvcdat/issues/269)
 * **Bug**: [build on Ubuntu 15.10](https://github.com/UV-CDAT/uvcdat/issues/1639)
 * **Bug**: [iPython3.0 merged update not found in master branch](https://github.com/UV-CDAT/uvcdat/issues/1441)
 * **Enhancement**: [Update cython to 0.22](https://github.com/UV-CDAT/uvcdat/issues/1128) ([#1436](https://github.com/UV-CDAT/uvcdat/pull/1436))
 * **Enhancement**: [Update matplotlib to 1.4.3](https://github.com/UV-CDAT/uvcdat/issues/1126) ([#1329](https://github.com/UV-CDAT/uvcdat/pull/1329))
 * **Enhancement**: [Update IPython to 3.0](https://github.com/UV-CDAT/uvcdat/issues/1127) ([#1330](https://github.com/UV-CDAT/uvcdat/pull/1330), [#1443](https://github.com/UV-CDAT/uvcdat/pull/1443))
 * **Enhancement**: [Update pip to 6.0.8](https://github.com/UV-CDAT/uvcdat/issues/1053) ([#1382](https://github.com/UV-CDAT/uvcdat/pull/1382))
 * **Enhancement**: [Update scipy to 0.16.1](https://github.com/UV-CDAT/uvcdat/issues/1193) ([#1654](https://github.com/UV-CDAT/uvcdat/pull/1654), [#1467](https://github.com/UV-CDAT/uvcdat/pull/1467))
 * **Enhancement**: [Fix test suite for LEAN mode](https://github.com/UV-CDAT/uvcdat/issues/1575) ([#1578](https://github.com/UV-CDAT/uvcdat/pull/1578))
 * **Enhancement**: [Update python-seawater to 3.3.4](https://github.com/UV-CDAT/uvcdat/issues/1686) ([#1687](https://github.com/UV-CDAT/uvcdat/pull/1687))
 * **Enhancement**: [CMake warning that might break things eventually](https://github.com/UV-CDAT/uvcdat/issues/1011) ([#1536](https://github.com/UV-CDAT/uvcdat/pull/1536))
 * **Enhancement**: [Configuring travis/buildbot testing to be more robust](https://github.com/UV-CDAT/uvcdat/issues/1384)
 * **Enhancement**: [Configure travis to additionally test "full" builds](https://github.com/UV-CDAT/uvcdat/issues/1033)
 * **Enhancement**: [Update pyspharm](https://github.com/UV-CDAT/uvcdat/issues/1070) ([#1444](https://github.com/UV-CDAT/uvcdat/pull/1444))
 * **Enhancement**: [Update vacumm to source from github (2.5.1 to 3.0.0)](https://github.com/UV-CDAT/uvcdat/issues/1635) ([#1685](https://github.com/UV-CDAT/uvcdat/pull/1685))
 * **Enhancement**: [Update FFmpeg to 2.5.3](https://github.com/UV-CDAT/uvcdat/issues/1029) ([#1381](https://github.com/UV-CDAT/uvcdat/pull/1381))

### DV3D

 * **Bug**: [Fix vcs3d failing test ](https://github.com/UV-CDAT/uvcdat/issues/1305)
 * **Bug**: [mac dv3d sample data put in different place](https://github.com/UV-CDAT/uvcdat/issues/1501) ([#1503](https://github.com/UV-CDAT/uvcdat/pull/1503))
 * **Bug**: [dv3d tests reverse baseline / test images](https://github.com/UV-CDAT/uvcdat/issues/950)
 * **Bug**: [(q)uit does not work correctly in a DV3D interactive canvas (exits python)](https://github.com/UV-CDAT/uvcdat/issues/953)
 * **Enhancement**: [DV3D keyword error](https://github.com/UV-CDAT/uvcdat/issues/1152)

### UVCDAT GUI

 * **Bug**: [Full screen plots do not work](https://github.com/UV-CDAT/uvcdat/issues/1638)
 * **Bug**: [Plots break after removing a cell and then adding it again.](https://github.com/UV-CDAT/uvcdat/issues/1124)
 * **Bug**: [vcs anim and multiple canvas](https://github.com/UV-CDAT/uvcdat/issues/338)
 * **Bug**: [generate range and pattern broken from GUI](https://github.com/UV-CDAT/uvcdat/issues/1573)
 * **Bug**: [Warning: Stenciling is not enabled on Isoline](https://github.com/UV-CDAT/uvcdat/issues/1576)
 * **Bug**: [GUI cannot switch dimensions](https://github.com/UV-CDAT/uvcdat/issues/1375)
 * **Bug**: [Isoline Labels don't show up initially in GUI](https://github.com/UV-CDAT/uvcdat/issues/1619)
 * **Bug**: [slab sub-selecting not working in UVCDAT GUI.](https://github.com/UV-CDAT/uvcdat/issues/1466) ([#1637](https://github.com/UV-CDAT/uvcdat/pull/1637))
 * **Bug**: [Colormap in GUI broken](https://github.com/UV-CDAT/uvcdat/issues/1721)
 * **Bug**: [ uvcdat writing thousands of tempfiles to users' .uvcdat directory](https://github.com/UV-CDAT/uvcdat/issues/1428)
 * **Bug**: [paraview still seems to be needed via matplotlib](https://github.com/UV-CDAT/uvcdat/issues/165)
 * **Bug**: [Plots initially too big for plot window.](https://github.com/UV-CDAT/uvcdat/issues/1632)
 * **Bug**: [clear seems to be not working on esgf search interface](https://github.com/UV-CDAT/uvcdat/issues/151)
 * **Bug**: [http get method in esgf browser, probably need to be replaced with proper wget script](https://github.com/UV-CDAT/uvcdat/issues/150) ([#1637](https://github.com/UV-CDAT/uvcdat/pull/1637))
 * **Enhancement**: [animation frame not updated when runnnig vcs animation in gui](https://github.com/UV-CDAT/uvcdat/issues/335) ([#1637](https://github.com/UV-CDAT/uvcdat/pull/1637))
 * **Enhancement**: [animation loop keeps going even after unchecking it](https://github.com/UV-CDAT/uvcdat/issues/336)
 * **Enhancement**: [Cosmetic Bug: dots in Scatter plot are hardly visible. ](https://github.com/UV-CDAT/uvcdat/issues/1281) ([#1617](https://github.com/UV-CDAT/uvcdat/pull/1617))
 * **Enhancement**: [Error message that makes no sense when trying to open a file that doesn't exists (from bookmarks for example)](https://github.com/UV-CDAT/uvcdat/issues/87) ([#1662](https://github.com/UV-CDAT/uvcdat/pull/1662), [#1394](https://github.com/UV-CDAT/uvcdat/pull/1394))
 * **Enhancement**: [Redirect all (i.e. non-Python) application output to log file](https://github.com/UV-CDAT/uvcdat/issues/1239) ([#1623](https://github.com/UV-CDAT/uvcdat/pull/1623))
 * **Enhancement**: [Provide UI option to control labels spacing](https://github.com/UV-CDAT/uvcdat/issues/1677)

### VCS

 * **Bug**: [vcs.Canvas.setantialiasing unusable](https://github.com/UV-CDAT/uvcdat/issues/1400) ([#1422](https://github.com/UV-CDAT/uvcdat/pull/1422))
 * **Enhancement**: [Labels are too close together](https://github.com/UV-CDAT/uvcdat/issues/1339) ([#1485](https://github.com/UV-CDAT/uvcdat/pull/1485))
 * **Bug**: [lambert proj appears to be broken??](https://github.com/UV-CDAT/uvcdat/issues/1763) ([#1768](https://github.com/UV-CDAT/uvcdat/pull/1768))
 * **Bug**: [Meshfill + interact() leads to error message](https://github.com/UV-CDAT/uvcdat/issues/1764) ([#1769](https://github.com/UV-CDAT/uvcdat/pull/1769))
 * **Bug**: [hatches/patterns don't work in vcs 2.0.beta](https://github.com/UV-CDAT/uvcdat/issues/541) ([#1516](https://github.com/UV-CDAT/uvcdat/pull/1516))
 * **Bug**: [isofill broken for discontinued](https://github.com/UV-CDAT/uvcdat/issues/1734) ([#1735](https://github.com/UV-CDAT/uvcdat/pull/1735))
 * **Bug**: [Meshfill plot does not wrap for bounds outside 0-360](https://github.com/UV-CDAT/uvcdat/issues/1746)
 * **Bug**: [vcs_test_init_open_sizing fails on small monitors](https://github.com/UV-CDAT/uvcdat/issues/1792)
 * **Bug**: [Remove x.png size parameters ?](https://github.com/UV-CDAT/uvcdat/issues/1068)
 * **Bug**: [animation does not work on projected plots](https://github.com/UV-CDAT/uvcdat/issues/1086) ([#1657](https://github.com/UV-CDAT/uvcdat/pull/1657))
 * **Bug**: [XvsY error](https://github.com/UV-CDAT/uvcdat/issues/1620) ([#1669](https://github.com/UV-CDAT/uvcdat/pull/1669), [#1621](https://github.com/UV-CDAT/uvcdat/pull/1621))
 * **Bug**: [Contour labels are don't show up in exported file (PDF)](https://github.com/UV-CDAT/uvcdat/issues/1626)
 * **Bug**: [isolines GUI editor not connected](https://github.com/UV-CDAT/uvcdat/issues/1625) ([#1688](https://github.com/UV-CDAT/uvcdat/pull/1688))
 * **Bug**: [yname doesn't change with autot](https://github.com/UV-CDAT/uvcdat/issues/1624)
 * **Bug**: [Animation and Resizing causes issues](https://github.com/UV-CDAT/uvcdat/issues/1629) ([#1634](https://github.com/UV-CDAT/uvcdat/pull/1634))
 * **Bug**: [Resize Window Core Dump](https://github.com/UV-CDAT/uvcdat/issues/236)
 * **Bug**: [setting colormap on object seem to not be picked up](https://github.com/UV-CDAT/uvcdat/issues/1271) ([#1523](https://github.com/UV-CDAT/uvcdat/pull/1523))
 * **Bug**: [grabWindowPixmap() broken for QCDATWidget](https://github.com/UV-CDAT/uvcdat/issues/1276)
 * **Bug**: [Patterns & Hatches on Boxfill, Isofill](https://github.com/UV-CDAT/uvcdat/issues/1577) ([#1582](https://github.com/UV-CDAT/uvcdat/pull/1582))
 * **Bug**: [Error when clicking on a_boxfill to get point values.](https://github.com/UV-CDAT/uvcdat/issues/1374)
 * **Bug**: [renderTemplate needs list, gets None](https://github.com/UV-CDAT/uvcdat/issues/1139)
 * **Bug**: [template.title.textorientation/table does not accept text object](https://github.com/UV-CDAT/uvcdat/issues/1087) ([#1509](https://github.com/UV-CDAT/uvcdat/pull/1509))
 * **Bug**: [Isofill Blank Spots on Solid with Indices/Levels](https://github.com/UV-CDAT/uvcdat/issues/1645) ([#1700](https://github.com/UV-CDAT/uvcdat/pull/1700))
 * **Bug**: [pattern are not wrapped around](https://github.com/UV-CDAT/uvcdat/issues/1644) ([#1690](https://github.com/UV-CDAT/uvcdat/pull/1690))
 * **Bug**: [vcs removeobject function broken](https://github.com/UV-CDAT/uvcdat/issues/1423)
 * **Bug**: [New libx264/h264 library bug needs fix](https://github.com/UV-CDAT/uvcdat/issues/1586) ([#1592](https://github.com/UV-CDAT/uvcdat/pull/1592))
 * **Bug**: [Line width is inconsistent across platforms](https://github.com/UV-CDAT/uvcdat/issues/1359) ([#1360](https://github.com/UV-CDAT/uvcdat/pull/1360))
 * **Bug**: [x.close() brokn if more than one plot on](https://github.com/UV-CDAT/uvcdat/issues/961)
 * **Bug**: [Continents are off](https://github.com/UV-CDAT/uvcdat/issues/1106) ([#1706](https://github.com/UV-CDAT/uvcdat/pull/1706), [#1717](https://github.com/UV-CDAT/uvcdat/pull/1717))
 * **Bug**: [Editing a label, rotate to ~311 degrees, open font menu -> segfault](https://github.com/UV-CDAT/uvcdat/issues/1093) ([#1514](https://github.com/UV-CDAT/uvcdat/pull/1514))
 * **Bug**: [bad error message if png output dir doesn't exist](https://github.com/UV-CDAT/uvcdat/issues/1396) ([#1556](https://github.com/UV-CDAT/uvcdat/pull/1556))
 * **Bug**: [x.png(outFileName, width=XX, height=XX) doesn't resize output file](https://github.com/UV-CDAT/uvcdat/issues/1588)
 * **Bug**: [fillarea dos not respect transparency](https://github.com/UV-CDAT/uvcdat/issues/1732) ([#1733](https://github.com/UV-CDAT/uvcdat/pull/1733))
 * **Bug**: [polar plot in isofill is not an option and isoline polar plot has wrong tic marks](https://github.com/UV-CDAT/uvcdat/issues/729)
 * **Bug**: [can't switch to portrait mode while in background mode](https://github.com/UV-CDAT/uvcdat/issues/1446) ([#1557](https://github.com/UV-CDAT/uvcdat/pull/1557))
 * **Bug**: [Saving an animation at 4 frames per second on mac creates green animation](https://github.com/UV-CDAT/uvcdat/issues/1118) ([#1564](https://github.com/UV-CDAT/uvcdat/pull/1564))
 * **Bug**: [canvas.getcolormapname behaviour changed](https://github.com/UV-CDAT/uvcdat/issues/1567) ([#1568](https://github.com/UV-CDAT/uvcdat/pull/1568))
 * **Enhancement**: [colormap need user level func to set colorindices](https://github.com/UV-CDAT/uvcdat/issues/1484) ([#1553](https://github.com/UV-CDAT/uvcdat/pull/1553))
 * **Enhancement**: [Isofill does not work with mercator if given lat coordinates values -90, 90 (the edges)](https://github.com/UV-CDAT/uvcdat/issues/587)
 * **Enhancement**: [Enable anti-aliasing ON by default and OFF for testing](https://github.com/UV-CDAT/uvcdat/issues/1432) ([#1442](https://github.com/UV-CDAT/uvcdat/pull/1442))
 * **Enhancement**: [turn antialiasing ON by default (and OFF in tests)](https://github.com/UV-CDAT/uvcdat/issues/1433)
 * **Enhancement**: [VCS write metadata in image](https://github.com/UV-CDAT/uvcdat/issues/1000)
 * **Enhancement**: [Provide a 'transparent' color for missing values (isofill/boxfill/etc... plots)](https://github.com/UV-CDAT/uvcdat/issues/1042) ([#1516](https://github.com/UV-CDAT/uvcdat/pull/1516))
 * **Enhancement**: [allow colors to define opacity](https://github.com/UV-CDAT/uvcdat/issues/1643)
 * **Enhancement**: [allow user to reference color by string or rgba tuple](https://github.com/UV-CDAT/uvcdat/issues/1642)
 * **Enhancement**: [EzTemplate object has no close function](https://github.com/UV-CDAT/uvcdat/issues/1585) ([#1591](https://github.com/UV-CDAT/uvcdat/pull/1591))
 * **Enhancement**: [setantialiasing not working if set too early](https://github.com/UV-CDAT/uvcdat/issues/1447)

### VTK

 * **Bug**: [`size` keyword argument has no effect in `vcs.init`](https://github.com/UV-CDAT/uvcdat/issues/1347) ([#1548](https://github.com/UV-CDAT/uvcdat/pull/1548), [#1562](https://github.com/UV-CDAT/uvcdat/pull/1562), [#1563](https://github.com/UV-CDAT/uvcdat/pull/1563))

### VisTrails

 * **Bug**: [CDMS3DPlot -> CDMSCell connections are invalid](https://github.com/UV-CDAT/uvcdat/issues/1346)

### cdms2

 * **Bug**: [cdms2 netcdf use parallel flag fails](https://github.com/UV-CDAT/uvcdat/issues/1593)
 * **Bug**: [ESMF regrid problem](https://github.com/UV-CDAT/uvcdat/issues/1125) ([#1574](https://github.com/UV-CDAT/uvcdat/pull/1574))
 * **Bug**: [problem with opendap file](https://github.com/UV-CDAT/uvcdat/issues/1475)
 * **Bug**: [Problems writing netcdf data - _FillValue error](https://github.com/UV-CDAT/uvcdat/issues/1479)
 * **Bug**: [cdms2 cannot open files if xml generated by cdscan contains different base urls](https://github.com/UV-CDAT/uvcdat/issues/1376)
 * **Bug**: [g2clib makefile typo](https://github.com/UV-CDAT/uvcdat/issues/1460)
 * **Bug**: [MV2.array(0.).fill_value is NaN!](https://github.com/UV-CDAT/uvcdat/issues/959) ([#1508](https://github.com/UV-CDAT/uvcdat/pull/1508))
 * **Enhancement**: [cdms2.write can't write a _FillValue attribute?](https://github.com/UV-CDAT/uvcdat/issues/1470) ([#1524](https://github.com/UV-CDAT/uvcdat/pull/1524))
 * **Enhancement**: [createVariableCopy() upcasting variables open from cdml catalog files.](https://github.com/UV-CDAT/uvcdat/issues/186) ([#1511](https://github.com/UV-CDAT/uvcdat/pull/1511))
 * **Enhancement**: [try different opendap url to bypass what seems to be firewall issues on opendap ctest](https://github.com/UV-CDAT/uvcdat/issues/1311)
 * **Enhancement**: [remove AutoAPI](https://github.com/UV-CDAT/uvcdat/issues/1358) ([#1369](https://github.com/UV-CDAT/uvcdat/pull/1369))
 * **Enhancement**: [enable netcdf parallel option](https://github.com/UV-CDAT/uvcdat/issues/1324) ([#1388](https://github.com/UV-CDAT/uvcdat/pull/1388))

### cdutil/genutil

 * **Bug**: [cdutil climos fail on file variables.](https://github.com/UV-CDAT/uvcdat/issues/1391)

## Merged Pull Requests

 * [#993: Fix git clone & update helper scripts](https://github.com/UV-CDAT/uvcdat/pull/993)
 * [#1261: Fix run tests buildbot](https://github.com/UV-CDAT/uvcdat/pull/1261)
 * [#1321: Issue 1312 tag repos](https://github.com/UV-CDAT/uvcdat/pull/1321)
 * [#1342: Sync release](https://github.com/UV-CDAT/uvcdat/pull/1342)
 * [#1348: Vtk master bump](https://github.com/UV-CDAT/uvcdat/pull/1348)
 * [#1357: Vtk master bump](https://github.com/UV-CDAT/uvcdat/pull/1357)
 * [#1389: Developers documentation](https://github.com/UV-CDAT/uvcdat/pull/1389)
 * [#1390: Sample data location updated](https://github.com/UV-CDAT/uvcdat/pull/1390)
 * [#1392: New test for 11 & 12.](https://github.com/UV-CDAT/uvcdat/pull/1392)
 * [#1393: Added a sleep for onscreen rendered tests](https://github.com/UV-CDAT/uvcdat/pull/1393)
 * [#1402: Remove creation of redundant file in source tree by test](https://github.com/UV-CDAT/uvcdat/pull/1402)
 * [#1403: Make tests fail if baselines not found](https://github.com/UV-CDAT/uvcdat/pull/1403)
 * [#1404: Fix tag detection for git clone/update scripts](https://github.com/UV-CDAT/uvcdat/pull/1404)
 * [#1418: Add flake8 test for vcs.](https://github.com/UV-CDAT/uvcdat/pull/1418)
 * [#1421: Add flake8 test for xmgrace.](https://github.com/UV-CDAT/uvcdat/pull/1421)
 * [#1426: Vtk ui test coverage](https://github.com/UV-CDAT/uvcdat/pull/1426)
 * [#1435: Issue1108 durack1 update spyder 2.3.4 to 2.3.5.2](https://github.com/UV-CDAT/uvcdat/pull/1435)
 * [#1440: R and rpy2](https://github.com/UV-CDAT/uvcdat/pull/1440)
 * [#1449: keep track of temporry elets added hen plotting](https://github.com/UV-CDAT/uvcdat/pull/1449)
 * [#1452: Fix CONTRIBUTING.md](https://github.com/UV-CDAT/uvcdat/pull/1452)
 * [#1456: Bugfixes](https://github.com/UV-CDAT/uvcdat/pull/1456)
 * [#1457: Allocate 512 char to save error message.](https://github.com/UV-CDAT/uvcdat/pull/1457)
 * [#1478: Issue1477 durack1 update spyder 2.3.5.2 to 3.0.0](https://github.com/UV-CDAT/uvcdat/pull/1478)
 * [#1480: no reason anymore to force pip at low version](https://github.com/UV-CDAT/uvcdat/pull/1480)
 * [#1488: updated json](https://github.com/UV-CDAT/uvcdat/pull/1488)
 * [#1490: Ansible vagrant install](https://github.com/UV-CDAT/uvcdat/pull/1490)
 * [#1492: get cmor via git repo](https://github.com/UV-CDAT/uvcdat/pull/1492)
 * [#1493: Pip no egg](https://github.com/UV-CDAT/uvcdat/pull/1493)
 * [#1496: Skipped some unnecessary renders](https://github.com/UV-CDAT/uvcdat/pull/1496)
 * [#1504: typo in rpy2 test](https://github.com/UV-CDAT/uvcdat/pull/1504)
 * [#1507: Fix library problem when compiling python 2.7 and using VIM 7.4. Add ...](https://github.com/UV-CDAT/uvcdat/pull/1507)
 * [#1513: Add PYPTHONPATH explicitly to cmake to make sure the right CYTHON is ...](https://github.com/UV-CDAT/uvcdat/pull/1513)
 * [#1515: Added URI to cdmsfile objects (courtesy of @doutriaux1)](https://github.com/UV-CDAT/uvcdat/pull/1515)
 * [#1518: RPM for 2.2.0](https://github.com/UV-CDAT/uvcdat/pull/1518)
 * [#1522: Force build to use our Cython](https://github.com/UV-CDAT/uvcdat/pull/1522)
 * [#1533: on the macbot it used to pick system png rather than XQuartz](https://github.com/UV-CDAT/uvcdat/pull/1533)
 * [#1534: Skip label test for redhat only](https://github.com/UV-CDAT/uvcdat/pull/1534)
 * [#1535: Pngupdate](https://github.com/UV-CDAT/uvcdat/pull/1535)
 * [#1540: issue1538 durack1 update Cython 0.22.1 to 0.23.3](https://github.com/UV-CDAT/uvcdat/pull/1540)
 * [#1541: issue1539 durack1 update iPython 3.0.0 to 4.0.0](https://github.com/UV-CDAT/uvcdat/pull/1541)
 * [#1551: Skipping this test for RH6 as well](https://github.com/UV-CDAT/uvcdat/pull/1551)
 * [#1552: Handle mercator infinity projection at 90,-90](https://github.com/UV-CDAT/uvcdat/pull/1552)
 * [#1554: adds a warning about removing .dodsrc file](https://github.com/UV-CDAT/uvcdat/pull/1554)
 * [#1558: disable testDistArray6Pes for 2.4](https://github.com/UV-CDAT/uvcdat/pull/1558)
 * [#1559: new g2clib that allows to build libcdms w/o png](https://github.com/UV-CDAT/uvcdat/pull/1559)
 * [#1560: Fix vector plots](https://github.com/UV-CDAT/uvcdat/pull/1560)
 * [#1561: Add windfield dependency to rpy2 getting rid of parallel installation...](https://github.com/UV-CDAT/uvcdat/pull/1561)
 * [#1565: Fix cmake binary download location](https://github.com/UV-CDAT/uvcdat/pull/1565)
 * [#1572: Workaround for XCode7 and 10.11 SDK](https://github.com/UV-CDAT/uvcdat/pull/1572)
 * [#1587: Flake8 thermo](https://github.com/UV-CDAT/uvcdat/pull/1587)
 * [#1596: wrong baseline src file names](https://github.com/UV-CDAT/uvcdat/pull/1596)
 * [#1600: set non parallel flag for cdscan](https://github.com/UV-CDAT/uvcdat/pull/1600)
 * [#1601: Cdmsopenparallel](https://github.com/UV-CDAT/uvcdat/pull/1601)
 * [#1602: Fixed doWrap method for vectors](https://github.com/UV-CDAT/uvcdat/pull/1602)
 * [#1604: Issue png size updated](https://github.com/UV-CDAT/uvcdat/pull/1604)
 * [#1605: Fix pattern 9](https://github.com/UV-CDAT/uvcdat/pull/1605)
 * [#1615: turned off the keep flag that prevented to test results](https://github.com/UV-CDAT/uvcdat/pull/1615)
 * [#1616: Fix TextCombined used wrong](https://github.com/UV-CDAT/uvcdat/pull/1616)
 * [#1618: Made ESMF fail the build when fortran is the wrong version](https://github.com/UV-CDAT/uvcdat/pull/1618)
 * [#1647: Fix compilation on Ubuntu with gcc 5.2.1](https://github.com/UV-CDAT/uvcdat/pull/1647)
 * [#1652: issue1549 durack1 update Matplotlib 1.4.3 to 1.5.0](https://github.com/UV-CDAT/uvcdat/pull/1652)
 * [#1653: issue1538 durack1 update Cython 0.23.3 to 0.23.4](https://github.com/UV-CDAT/uvcdat/pull/1653)
 * [#1656: Set ffmpeg root when building ffmpeg](https://github.com/UV-CDAT/uvcdat/pull/1656)
 * [#1658: load texttables and textorientations and text markers first](https://github.com/UV-CDAT/uvcdat/pull/1658)
 * [#1661: Use cmake to download uvcmetrics test data](https://github.com/UV-CDAT/uvcdat/pull/1661)
 * [#1667: Window flickering when png](https://github.com/UV-CDAT/uvcdat/pull/1667)
 * [#1670: Pattern size scaling](https://github.com/UV-CDAT/uvcdat/pull/1670)
 * [#1678: Continents & Continent Lines](https://github.com/UV-CDAT/uvcdat/pull/1678)
 * [#1689: ENH: Add the ability to write/read PNG metadata](https://github.com/UV-CDAT/uvcdat/pull/1689)
 * [#1691: Fixed cmake warning during configure step](https://github.com/UV-CDAT/uvcdat/pull/1691)
 * [#1692: fix configure arguments separator](https://github.com/UV-CDAT/uvcdat/pull/1692)
 * [#1693: Colormaps](https://github.com/UV-CDAT/uvcdat/pull/1693)
 * [#1695: Revert "Fix #1539 - Update iPython 3.0.0 to 4.0.0"](https://github.com/UV-CDAT/uvcdat/pull/1695)
 * [#1696: Now will work if there is no .uvcdat directory](https://github.com/UV-CDAT/uvcdat/pull/1696)
 * [#1697: Altered some tests to ensure geometry](https://github.com/UV-CDAT/uvcdat/pull/1697)
 * [#1699: fixed issue where old scr colormap file would not load opacity](https://github.com/UV-CDAT/uvcdat/pull/1699)
 * [#1703: fixed tag point for external repos](https://github.com/UV-CDAT/uvcdat/pull/1703)
 * [#1705: Fix rpm](https://github.com/UV-CDAT/uvcdat/pull/1705)
 * [#1708: Increased threshold for pattern tests to allow meshfill to pass](https://github.com/UV-CDAT/uvcdat/pull/1708)
 * [#1709: Fix initial size](https://github.com/UV-CDAT/uvcdat/pull/1709)
 * [#1712: Fixed some bugs with continents line](https://github.com/UV-CDAT/uvcdat/pull/1712)
 * [#1713: Fixed two bugs with matplotlib colormap import](https://github.com/UV-CDAT/uvcdat/pull/1713)
 * [#1724: Fixed setcolorcell in vcs.utils](https://github.com/UV-CDAT/uvcdat/pull/1724)
 * [#1727: Moved/renamed license](https://github.com/UV-CDAT/uvcdat/pull/1727)
 * [#1731: Issue 1730 mesh with missing vertices](https://github.com/UV-CDAT/uvcdat/pull/1731)
 * [#1736: Duplicate longitude wrap](https://github.com/UV-CDAT/uvcdat/pull/1736)
 * [#1741: Noticklabelonellipticalprojections](https://github.com/UV-CDAT/uvcdat/pull/1741)
 * [#1742: Revert "Check whether OpenSSL library and/or headers not found"](https://github.com/UV-CDAT/uvcdat/pull/1742)
 * [#1744: BUG #1739: fitToViewport uses dataset bounds instead of recomputing them](https://github.com/UV-CDAT/uvcdat/pull/1744)
 * [#1755: Fixes issue with incorrect URIs for opendap urls](https://github.com/UV-CDAT/uvcdat/pull/1755)
 * [#1757: Fixed conversion to base64 string](https://github.com/UV-CDAT/uvcdat/pull/1757)
 * [#1772: BUG: proj4 over option causes problems with polar projections](https://github.com/UV-CDAT/uvcdat/pull/1772)
 * [#1774: Revert "BUG: proj4 over option causes problems with polar projections"](https://github.com/UV-CDAT/uvcdat/pull/1774)
 * [#1778: Irregular cut wrap](https://github.com/UV-CDAT/uvcdat/pull/1778)
 * [#1793: Got rid of screen size logic from test](https://github.com/UV-CDAT/uvcdat/pull/1793)
 * [#1794: Fixed bug that was breaking continents when set at canvas level](https://github.com/UV-CDAT/uvcdat/pull/1794)
 * [#1802: Update readme master](https://github.com/UV-CDAT/uvcdat/pull/1802)

## Known Bugs

### Critical

 * [master fails some tests on RH6/CentOS6](https://github.com/UV-CDAT/uvcdat/issues/1481)
 * [creating pngs in background mode leaks memory](https://github.com/UV-CDAT/uvcdat/issues/1397)

### Other

 * [seg fault on a lambert projection](https://github.com/UV-CDAT/uvcdat/issues/1804)
 * [can't read some old vcs scr files](https://github.com/UV-CDAT/uvcdat/issues/1801)
 * [Disable projected click, fix time values](https://github.com/UV-CDAT/uvcdat/pull/1800)
 * [ratio="autot" fails to correctly generate the initial ratio](https://github.com/UV-CDAT/uvcdat/issues/1795)
 * [Fit to viewport needs updating for continent outline](https://github.com/UV-CDAT/uvcdat/issues/1786)
 * [proj4 acting up on macs and ubuntu mesa](https://github.com/UV-CDAT/uvcdat/issues/1777)
 * [Meshfill leaves extra display plots lying around](https://github.com/UV-CDAT/uvcdat/issues/1770)
 * [test_vcs_animate_projected_meshfill_mollweide.png is not wrapped](https://github.com/UV-CDAT/uvcdat/issues/1754)
 * [var.squeeze() truncates axis information](https://github.com/UV-CDAT/uvcdat/issues/1738)
 * [CDMS2/MV2.newaxis doesn't work](https://github.com/UV-CDAT/uvcdat/issues/1722)
 * [cdms2.getGrid()/setGrid() doesn't work](https://github.com/UV-CDAT/uvcdat/issues/1707)
 * [Fix memory leak in cdtime](https://github.com/UV-CDAT/uvcdat/issues/1698)
 * [Meshfill plot with Mercator projection issue](https://github.com/UV-CDAT/uvcdat/issues/1671)
 * [Weight problems in cdutil.ANNUALCYCLE.climatology (daily data)](https://github.com/UV-CDAT/uvcdat/issues/1664)
 * [projections still broken](https://github.com/UV-CDAT/uvcdat/issues/1640)
 * [MPI builds and Python multiprocessing](https://github.com/UV-CDAT/uvcdat/issues/1608)
 * [iso plot failure](https://github.com/UV-CDAT/uvcdat/issues/1594)
 * [VCS/VTK warnings and UV-CDAT logo missing in pdf/ps output files](https://github.com/UV-CDAT/uvcdat/issues/1583)
 * [cdscan hang](https://github.com/UV-CDAT/uvcdat/issues/1546)
 * [Catch cdscan errors without triggering runtime failures](https://github.com/UV-CDAT/uvcdat/issues/1512)
 * [Bad rendering of aeqd projection](https://github.com/UV-CDAT/uvcdat/issues/1462)
 * [vcs.plot(iso) creates text object that are not removed after clear](https://github.com/UV-CDAT/uvcdat/issues/1424)
 * [can't delete file attribute](https://github.com/UV-CDAT/uvcdat/issues/1398)
 * [cdms2 can only open cdscanned http files from the directory the file is at](https://github.com/UV-CDAT/uvcdat/issues/1368)



<a name="2.2"></a>

# 2.2 Changelog

## Closed Issues

### ACME

 * **Bug**: [No usch text combined](https://github.com/UV-CDAT/uvcdat/issues/1096) ([#1107](https://github.com/UV-CDAT/uvcdat/pull/1107))
 * **Bug**: [invalid framebuffer operation](https://github.com/UV-CDAT/uvcdat/issues/1100)
 * **Bug**: [average() indentation error](https://github.com/UV-CDAT/uvcdat/issues/1048) ([#1050](https://github.com/UV-CDAT/uvcdat/pull/1050))

### Build

 * **Bug**: [esmp install broken](https://github.com/UV-CDAT/uvcdat/issues/981) ([#982](https://github.com/UV-CDAT/uvcdat/pull/982))
 * **Bug**: [Pyclimate not built with build mode all](https://github.com/UV-CDAT/uvcdat/issues/1071) ([#1075](https://github.com/UV-CDAT/uvcdat/pull/1075))
 * **Bug**: [mac build broken](https://github.com/UV-CDAT/uvcdat/issues/991) ([#998](https://github.com/UV-CDAT/uvcdat/pull/998), [#995](https://github.com/UV-CDAT/uvcdat/pull/995))
 * **Bug**: [test failing because mean is different ](https://github.com/UV-CDAT/uvcdat/issues/1063) ([#1076](https://github.com/UV-CDAT/uvcdat/pull/1076))
 * **Bug**: [Building on OS X 10.10.2](https://github.com/UV-CDAT/uvcdat/issues/1012)
 * **Bug**: [git_update.sh fails if updating to a tag](https://github.com/UV-CDAT/uvcdat/issues/837)
 * **Bug**: [ctest 'fails' if python has not been run interactively at least once (anonymous logging problem)](https://github.com/UV-CDAT/uvcdat/issues/456) ([#1102](https://github.com/UV-CDAT/uvcdat/pull/1102))
 * **Bug**: [Out of source detection is broken](https://github.com/UV-CDAT/uvcdat/issues/713)
 * **Bug**: [metrics not build if CDAT_BUILD_GUI=OFF](https://github.com/UV-CDAT/uvcdat/issues/996)
 * **Bug**: [SciPy fails to build on CentOS 6.6](https://github.com/UV-CDAT/uvcdat/issues/1192)
 * **Bug**: [scipy fails to build without -D__ACCELERATE__](https://github.com/UV-CDAT/uvcdat/issues/966) ([#1165](https://github.com/UV-CDAT/uvcdat/pull/1165))
 * **Enhancement**: [try to detect protocol for user](https://github.com/UV-CDAT/uvcdat/issues/810)
 * **Enhancement**: [no need for git to check ssl](https://github.com/UV-CDAT/uvcdat/issues/924)
 * **Enhancement**: [Several warnings during the cmake stage that should be cleaned?](https://github.com/UV-CDAT/uvcdat/issues/825) ([#1062](https://github.com/UV-CDAT/uvcdat/pull/1062))
 * **Enhancement**: [Update udunits to 2.2.x branch](https://github.com/UV-CDAT/uvcdat/issues/847)
 * **Enhancement**: [Update netcdf to 4.3.2](https://github.com/UV-CDAT/uvcdat/issues/846) ([#972](https://github.com/UV-CDAT/uvcdat/pull/972))
 * **Enhancement**: [Update matplotlib to 1.4.2](https://github.com/UV-CDAT/uvcdat/issues/841) ([#921](https://github.com/UV-CDAT/uvcdat/pull/921))

### DV3D

 * **Bug**: [Slider issues with Hovmuller plot and vector slicer.](https://github.com/UV-CDAT/uvcdat/issues/1146) ([#1147](https://github.com/UV-CDAT/uvcdat/pull/1147))
 * **Bug**: [3D_Scalar Unexpected Error](https://github.com/UV-CDAT/uvcdat/issues/884)
 * **Bug**: [dv3d list broken](https://github.com/UV-CDAT/uvcdat/issues/1285) ([#1287](https://github.com/UV-CDAT/uvcdat/pull/1287))

### Documentation

 * **Bug**: [UV-CDAT docs website: cdms/cdtime manual page problem](https://github.com/UV-CDAT/uvcdat/issues/1136)
 * **Enhancement**: [Document for manual testing of GUI](https://github.com/UV-CDAT/uvcdat/issues/1215)

### UVCDAT GUI

 * **Bug**: [Traceback on cell creation](https://github.com/UV-CDAT/uvcdat/issues/1018)
 * **Bug**: [.vt doesn't have all the steps](https://github.com/UV-CDAT/uvcdat/issues/283)
 * **Bug**: [Cython classmethod_utility_code used in VisTrails vtDVD3D](https://github.com/UV-CDAT/uvcdat/issues/1056)
 * **Bug**: [GUI cannot load variable](https://github.com/UV-CDAT/uvcdat/issues/1057)
 * **Bug**: [Refresh problem with 2.1](https://github.com/UV-CDAT/uvcdat/issues/1007)
 * **Bug**: [Error while plotting meshfill plot](https://github.com/UV-CDAT/uvcdat/issues/1284)
 * **Bug**: [Deleting all variables doesn't work if one variable is derived from another (in GUI).](https://github.com/UV-CDAT/uvcdat/issues/897)
 * **Enhancement**: [animation processing message](https://github.com/UV-CDAT/uvcdat/issues/642)
 * **Enhancement**: [uvcdat "executable" should unset env or it might be using the "Wrong" python](https://github.com/UV-CDAT/uvcdat/issues/730)

### VCS

 * **Bug**: [lines drawn behind data](https://github.com/UV-CDAT/uvcdat/issues/1143)
 * **Bug**: [The plotting of 120 plots and clearing  is taking too long](https://github.com/UV-CDAT/uvcdat/issues/715)
 * **Bug**: [Cannot animate Isofill](https://github.com/UV-CDAT/uvcdat/issues/1141) ([#1142](https://github.com/UV-CDAT/uvcdat/pull/1142))
 * **Bug**: [ctest might fail because of too many digits on mean](https://github.com/UV-CDAT/uvcdat/issues/952)
 * **Bug**: [animation boxfill broken](https://github.com/UV-CDAT/uvcdat/issues/1234) ([#1236](https://github.com/UV-CDAT/uvcdat/pull/1236))
 * **Bug**: [isoline labels text color broken](https://github.com/UV-CDAT/uvcdat/issues/1230)
 * **Bug**: [wrapping labels seems to still not work](https://github.com/UV-CDAT/uvcdat/issues/1133) ([#1172](https://github.com/UV-CDAT/uvcdat/pull/1172))
 * **Bug**: [Error on meshfill](https://github.com/UV-CDAT/uvcdat/issues/1245) ([#1247](https://github.com/UV-CDAT/uvcdat/pull/1247))
 * **Bug**: [default boxfill wrong lat labels](https://github.com/UV-CDAT/uvcdat/issues/960) ([#965](https://github.com/UV-CDAT/uvcdat/pull/965), [#962](https://github.com/UV-CDAT/uvcdat/pull/962))
 * **Bug**: [in some case the continents are not plotted properly (polar proj with north pole)](https://github.com/UV-CDAT/uvcdat/issues/1020) ([#1022](https://github.com/UV-CDAT/uvcdat/pull/1022))
 * **Bug**: [boxfill plots don't pick proper interval](https://github.com/UV-CDAT/uvcdat/issues/867)
 * **Bug**: [markers not drawn if x world coordinate reversed](https://github.com/UV-CDAT/uvcdat/issues/969) ([#970](https://github.com/UV-CDAT/uvcdat/pull/970))
 * **Bug**: [Control + Click doesn't work in GUI](https://github.com/UV-CDAT/uvcdat/issues/1163) ([#1169](https://github.com/UV-CDAT/uvcdat/pull/1169))
 * **Bug**: [Ext1 and Ext2 are rendering incorrectly](https://github.com/UV-CDAT/uvcdat/issues/1204) ([#1209](https://github.com/UV-CDAT/uvcdat/pull/1209))
 * **Bug**: [clear canvas while animation running in GUI doesn't seem to stop it](https://github.com/UV-CDAT/uvcdat/issues/1197) ([#1207](https://github.com/UV-CDAT/uvcdat/pull/1207))
 * **Bug**: [animation vcs speed slider seem to have no effect](https://github.com/UV-CDAT/uvcdat/issues/1196) ([#1202](https://github.com/UV-CDAT/uvcdat/pull/1202))
 * **Bug**: [isofill masked does not align with isofill cells](https://github.com/UV-CDAT/uvcdat/issues/1170) ([#1171](https://github.com/UV-CDAT/uvcdat/pull/1171))
 * **Bug**: [Isoline labels broken](https://github.com/UV-CDAT/uvcdat/issues/1132)
 * **Enhancement**: [animate.save() print statements](https://github.com/UV-CDAT/uvcdat/issues/1085) ([#1121](https://github.com/UV-CDAT/uvcdat/pull/1121))
 * **Enhancement**: [text rotation in VTK different from vcs way](https://github.com/UV-CDAT/uvcdat/issues/503) ([#1013](https://github.com/UV-CDAT/uvcdat/pull/1013))
 * **Enhancement**: [Fix vcs interact warnings ](https://github.com/UV-CDAT/uvcdat/issues/651)
 * **Enhancement**: [mean on vcs plots should use cdutil.averager if possible](https://github.com/UV-CDAT/uvcdat/issues/1024) ([#1028](https://github.com/UV-CDAT/uvcdat/pull/1028))
 * **Enhancement**: [time slider should be disabled when running animation](https://github.com/UV-CDAT/uvcdat/issues/1195) ([#1201](https://github.com/UV-CDAT/uvcdat/pull/1201))

### VTK

 * **Bug**: [isolines labels are different between mac and linux](https://github.com/UV-CDAT/uvcdat/issues/1160)

### cdms2

 * **Bug**: [load and close with large data files doesn't work](https://github.com/UV-CDAT/uvcdat/issues/511)

### cdutil/genutil

 * **Bug**: [cdutil times criteriaargclim is useless and leads to error](https://github.com/UV-CDAT/uvcdat/issues/984) ([#985](https://github.com/UV-CDAT/uvcdat/pull/985))

## Merged Pull Requests

 * [#747: Fixing UVCDAT runtime environment](https://github.com/UV-CDAT/uvcdat/pull/747)
 * [#944: Issue942 durack1 python279 update](https://github.com/UV-CDAT/uvcdat/pull/944)
 * [#951: Vcs3D features for v2.1.1](https://github.com/UV-CDAT/uvcdat/pull/951)
 * [#971: Fixes exception from VTKVCSBackend](https://github.com/UV-CDAT/uvcdat/pull/971)
 * [#973: Build in source](https://github.com/UV-CDAT/uvcdat/pull/973)
 * [#974: System python updated](https://github.com/UV-CDAT/uvcdat/pull/974)
 * [#975: Update cmake to version 3.1 on travis before building](https://github.com/UV-CDAT/uvcdat/pull/975)
 * [#979: Line duplicate points fix](https://github.com/UV-CDAT/uvcdat/pull/979)
 * [#987: Create an option to enable vtkweb](https://github.com/UV-CDAT/uvcdat/pull/987)
 * [#988: Setting the correct PYTHON_SITE_PACKAGES_PREFIX on Apple](https://github.com/UV-CDAT/uvcdat/pull/988)
 * [#990: Merge remote-tracking branch 'origin/fix-quotes-updated' into release](https://github.com/UV-CDAT/uvcdat/pull/990)
 * [#992: Updated packages reference](https://github.com/UV-CDAT/uvcdat/pull/992)
 * [#993: Fix git clone & update helper scripts](https://github.com/UV-CDAT/uvcdat/pull/993)
 * [#994: Checking for http and https as well now](https://github.com/UV-CDAT/uvcdat/pull/994)
 * [#1005: do not turn off metrics when no GUI](https://github.com/UV-CDAT/uvcdat/pull/1005)
 * [#1014: Update background color](https://github.com/UV-CDAT/uvcdat/pull/1014)
 * [#1038: Optimize vtk](https://github.com/UV-CDAT/uvcdat/pull/1038)
 * [#1047: 1. In the section involving 'allaxesdummy', where a dummy variable is cr...](https://github.com/UV-CDAT/uvcdat/pull/1047)
 * [#1052: should address part of #729](https://github.com/UV-CDAT/uvcdat/pull/1052)
 * [#1067: Line duplicate points fix](https://github.com/UV-CDAT/uvcdat/pull/1067)
 * [#1069: Removes a warning](https://github.com/UV-CDAT/uvcdat/pull/1069)
 * [#1072: Issue421 durack1 add seawater packages](https://github.com/UV-CDAT/uvcdat/pull/1072)
 * [#1073: Issue423 durack1 add vacumm package](https://github.com/UV-CDAT/uvcdat/pull/1073)
 * [#1089: Issue423 durack1 fix vacumm dependencies](https://github.com/UV-CDAT/uvcdat/pull/1089)
 * [#1090: Remove pycharm and unnecessary README files](https://github.com/UV-CDAT/uvcdat/pull/1090)
 * [#1091: Vcs2d interactions updated](https://github.com/UV-CDAT/uvcdat/pull/1091)
 * [#1098: Fixes autot resizing when configurator instantiated](https://github.com/UV-CDAT/uvcdat/pull/1098)
 * [#1110: Now we can build on Yosemite ](https://github.com/UV-CDAT/uvcdat/pull/1110)
 * [#1113: VCS2D Animation while Interacting](https://github.com/UV-CDAT/uvcdat/pull/1113)
 * [#1114: Added files](https://github.com/UV-CDAT/uvcdat/pull/1114)
 * [#1115: adding ipython created cyclical deps](https://github.com/UV-CDAT/uvcdat/pull/1115)
 * [#1119: Isofill on pointdata struct grid](https://github.com/UV-CDAT/uvcdat/pull/1119)
 * [#1123: VTK can't seem to be able to use mac system headers](https://github.com/UV-CDAT/uvcdat/pull/1123)
 * [#1135: Workaround for #1093](https://github.com/UV-CDAT/uvcdat/pull/1135)
 * [#1138: Vcs3 d fix 2.2 interaction problems](https://github.com/UV-CDAT/uvcdat/pull/1138)
 * [#1144: Issue 587 projected ticks](https://github.com/UV-CDAT/uvcdat/pull/1144)
 * [#1145: Adding Dockerfiles for generating docker images](https://github.com/UV-CDAT/uvcdat/pull/1145)
 * [#1153: Add vcs keywords](https://github.com/UV-CDAT/uvcdat/pull/1153)
 * [#1154: Fix missing displays for animation/interaction](https://github.com/UV-CDAT/uvcdat/pull/1154)
 * [#1156: Fix error in getCoordType](https://github.com/UV-CDAT/uvcdat/pull/1156)
 * [#1157: vcs3D-return_to_shell_on_q_keypress_event](https://github.com/UV-CDAT/uvcdat/pull/1157)
 * [#1159: Fix rc1 tests](https://github.com/UV-CDAT/uvcdat/pull/1159)
 * [#1161: VCS2D Animation Speedup](https://github.com/UV-CDAT/uvcdat/pull/1161)
 * [#1164: Time slider upgrade](https://github.com/UV-CDAT/uvcdat/pull/1164)
 * [#1167: Target will now detach when configurator detaches](https://github.com/UV-CDAT/uvcdat/pull/1167)
 * [#1168: Fixes ubuntu error that showed up for charles](https://github.com/UV-CDAT/uvcdat/pull/1168)
 * [#1173: Changed 2D animation to use same type of animation speed as 3d](https://github.com/UV-CDAT/uvcdat/pull/1173)
 * [#1177: Fixed some VTK error messages that showed up when ending configure](https://github.com/UV-CDAT/uvcdat/pull/1177)
 * [#1178: Issue 1158 auto magic time labels](https://github.com/UV-CDAT/uvcdat/pull/1178)
 * [#1179: Fix ratio resizing issue](https://github.com/UV-CDAT/uvcdat/pull/1179)
 * [#1182: pickle would not work](https://github.com/UV-CDAT/uvcdat/pull/1182)
 * [#1184: 3D support for vcs.update](https://github.com/UV-CDAT/uvcdat/pull/1184)
 * [#1185: vtk_ui.Button tests](https://github.com/UV-CDAT/uvcdat/pull/1185)
 * [#1190: Fix for clear and close for DV3D plots](https://github.com/UV-CDAT/uvcdat/pull/1190)
 * [#1206: Made slider jump instead of animate, added test](https://github.com/UV-CDAT/uvcdat/pull/1206)
 * [#1216: Newdiagtest](https://github.com/UV-CDAT/uvcdat/pull/1216)
 * [#1218: New test, for spaghetti/multiline plots (plot set 3).](https://github.com/UV-CDAT/uvcdat/pull/1218)
 * [#1219: Salinity](https://github.com/UV-CDAT/uvcdat/pull/1219)
 * [#1221: Boxfill bug branch clean up](https://github.com/UV-CDAT/uvcdat/pull/1221)
 * [#1225: Unstructured plots](https://github.com/UV-CDAT/uvcdat/pull/1225)
 * [#1226: Added message in setup_runtime scripts](https://github.com/UV-CDAT/uvcdat/pull/1226)
 * [#1227: Allow open/interact without plotting anything](https://github.com/UV-CDAT/uvcdat/pull/1227)
 * [#1238: Newdiagstes charles](https://github.com/UV-CDAT/uvcdat/pull/1238)
 * [#1240: Fixes typo in CDMS raise statements](https://github.com/UV-CDAT/uvcdat/pull/1240)
 * [#1243: Fixes typo in CDMS raise statements](https://github.com/UV-CDAT/uvcdat/pull/1243)
 * [#1244: Pressing the "i" key makes button disappear (and other issues)](https://github.com/UV-CDAT/uvcdat/pull/1244)
 * [#1246: Colorpicker now uses manager correctly](https://github.com/UV-CDAT/uvcdat/pull/1246)
 * [#1249: Meshfill animation](https://github.com/UV-CDAT/uvcdat/pull/1249)
 * [#1255: Marker deletion](https://github.com/UV-CDAT/uvcdat/pull/1255)
 * [#1257: Merge colorpicker changes into release](https://github.com/UV-CDAT/uvcdat/pull/1257)
 * [#1258: Colorpicker renderer selection](https://github.com/UV-CDAT/uvcdat/pull/1258)
 * [#1261: Fix run tests buildbot](https://github.com/UV-CDAT/uvcdat/pull/1261)
 * [#1262: Update master](https://github.com/UV-CDAT/uvcdat/pull/1262)
 * [#1267: Issue 903 turn off paraview](https://github.com/UV-CDAT/uvcdat/pull/1267)
 * [#1269: Vcs3 d fix release issues](https://github.com/UV-CDAT/uvcdat/pull/1269)
 * [#1270: Fixes more typos in raise statements](https://github.com/UV-CDAT/uvcdat/pull/1270)
 * [#1273: Toolbar layout fixes](https://github.com/UV-CDAT/uvcdat/pull/1273)
 * [#1296: Sync master](https://github.com/UV-CDAT/uvcdat/pull/1296)
 * [#1298: Add lapack to libcf deps](https://github.com/UV-CDAT/uvcdat/pull/1298)
 * [#1307: Fixed the ordering of images for regression testing](https://github.com/UV-CDAT/uvcdat/pull/1307)
 * [#1316: Final commits to make buildbot pass](https://github.com/UV-CDAT/uvcdat/pull/1316)

## Known Bugs

### Critical

 * [Taylor diagrams (plot set 14)](https://github.com/UV-CDAT/uvcdat/issues/1180)
 * [Resize Window Core Dump](https://github.com/UV-CDAT/uvcdat/issues/236)

### Other

 * [gui python script extensions are written as string when they should be boolean](https://github.com/UV-CDAT/uvcdat/issues/1306)
 * [Fix vcs3d failing test ](https://github.com/UV-CDAT/uvcdat/issues/1305)
 * [dv3d cannot go back into interact mode](https://github.com/UV-CDAT/uvcdat/issues/1295)
 * [dv3d plotting ad changing attributes breaks dv3d](https://github.com/UV-CDAT/uvcdat/issues/1286)
 * [setting colormap on object seem to not be picked up](https://github.com/UV-CDAT/uvcdat/issues/1271)
 * [polar plot for sub zones seems to not work](https://github.com/UV-CDAT/uvcdat/issues/1265)
 * [ESMF regrid problem](https://github.com/UV-CDAT/uvcdat/issues/1125)
 * [Continents are off](https://github.com/UV-CDAT/uvcdat/issues/1106)
 * [x/yaxisconvert not respected anymore.](https://github.com/UV-CDAT/uvcdat/issues/1066)
 * [x.close() brokn if more than one plot on](https://github.com/UV-CDAT/uvcdat/issues/961)
 * [(q)uit does not work correctly in a DV3D interactive canvas (exits python)](https://github.com/UV-CDAT/uvcdat/issues/953)
 * [cdtime and big hours](https://github.com/UV-CDAT/uvcdat/issues/781)
 * [-DBUILD_PARALLEL=ON fails on mac (at least)](https://github.com/UV-CDAT/uvcdat/issues/667)
 * [The vectors are not drawn when using projection other than plat-caree.](https://github.com/UV-CDAT/uvcdat/issues/653)
 * [Unable to write unsigned int8 variable in netcdf4 file (non-netcdf3 type)](https://github.com/UV-CDAT/uvcdat/issues/481)
 * [Fix setup_runtime.sh script for DMG](https://github.com/UV-CDAT/uvcdat/issues/409)
 * [system picks up wrong pip when building ipython and tornado ](https://github.com/UV-CDAT/uvcdat/issues/269)

<a id="2.1"></a>

# 2.1 Changelog

## Closed Issues

### Build

 * **Bug**: [On Mac Udunits fails because of flex not found](https://github.com/UV-CDAT/uvcdat/issues/733)
 * **Bug**: [CMOR doesn't build](https://github.com/UV-CDAT/uvcdat/issues/786)
 * **Bug**: [visit_vtk failed to build: missing vtkPolyDataToPolyDataFilter.h](https://github.com/UV-CDAT/uvcdat/issues/802)
 * **Bug**: [git_update.sh fails if updating to a tag](https://github.com/UV-CDAT/uvcdat/issues/837)

### DV3D

 * **Enhancement**: [Change template name from xyt to Hovmoller-3D](https://github.com/UV-CDAT/uvcdat/issues/765)
 * **Bug**: [3D_Scalar plot (xyt) gives errors plotting 3D variable with no time dimensions.](https://github.com/UV-CDAT/uvcdat/issues/854)
 * **Bug**: [Plotted a 3D-scalar, and the vertical level reported in the heading appears to be upside-down.](https://github.com/UV-CDAT/uvcdat/issues/853)
 * **Bug**: [Two UV-CDAT Labels in the Lower Right for 3D VCS Plots](https://github.com/UV-CDAT/uvcdat/issues/858)
 * **Bug**: [ubuntu animations aren't saved](https://github.com/UV-CDAT/uvcdat/issues/799)

### UVCDAT GUI

 * **Bug**: [rename colormap does not put it in list of available colormaps](https://github.com/UV-CDAT/uvcdat/issues/829)
 * **Enhancement**: [Error messages when launching uvcdat on Rhea.](https://github.com/UV-CDAT/uvcdat/issues/727)

### VCS

 * **Bug**: [meshfill missing color not respected](https://github.com/UV-CDAT/uvcdat/issues/873)
 * ***Bug*: [Scatter plot labels](https://github.com/UV-CDAT/uvcdat/issues/716)
 * **Bug**: [x.showbg() does not work in 2.0.0](https://github.com/UV-CDAT/uvcdat/issues/863)
 * **Bug**: [x.interact() should print an error message when no canvas is open](https://github.com/UV-CDAT/uvcdat/issues/862)
 * **Bug**: [cleanup EzTemplate](https://github.com/UV-CDAT/uvcdat/issues/826)
 * **Bug**: [meshfill plot broekn with bg=0](https://github.com/UV-CDAT/uvcdat/issues/804)
 * **Bug**: [continents chopped](https://github.com/UV-CDAT/uvcdat/issues/693)
 * **Bug**: [yxvsx plot a black screen when no text and box1.priority = 0](https://github.com/UV-CDAT/uvcdat/issues/706)
 * **Bug**: [x.clear does not do anything.](https://github.com/UV-CDAT/uvcdat/issues/707)
 * **Bug**: [boxfill/isofill missing attrbute does not change coor of missing](https://github.com/UV-CDAT/uvcdat/issues/855)
 * **Bug**: [VTK not mapping?](https://github.com/UV-CDAT/uvcdat/issues/871)
 * **Bug**: [templates do not save associated texttable/orientation](https://github.com/UV-CDAT/uvcdat/issues/816)
 * **Bug**: [oned plots wrong when levels are flipped](https://github.com/UV-CDAT/uvcdat/issues/832)
 * **Bug**: [Can't load data in uvcdat 2.0.0 !](https://github.com/UV-CDAT/uvcdat/issues/843) ([#852](https://github.com/UV-CDAT/uvcdat/pull/852))
 * **Bug**: [xname and yname doesn't work](https://github.com/UV-CDAT/uvcdat/issues/710)
 * **Bug**: [boxfill leve_1 level_2 reassigned](https://github.com/UV-CDAT/uvcdat/issues/869)
 * **Bug**: [default boxfill wrong lat labels](https://github.com/UV-CDAT/uvcdat/issues/960)
 * **Bug**: [isoline pure numpy fails](https://github.com/UV-CDAT/uvcdat/issues/928) ([#929](https://github.com/UV-CDAT/uvcdat/pull/929))
 * **Bug**: [template rescale could move things too far and lead to errors](https://github.com/UV-CDAT/uvcdat/issues/805)
 * **Enhancement**: [drawing of colorbar in vcs too slow](https://github.com/UV-CDAT/uvcdat/issues/849)
 * **Enhancement**: [white bg by default](https://github.com/UV-CDAT/uvcdat/issues/817)
 * **Enhancement**: [Blank png: x.png does not set the alpha/transparency info correctly !](https://github.com/UV-CDAT/uvcdat/issues/848)

### VTK

 * **Bug**: [Contours colored wrong when data has a wide range](https://github.com/UV-CDAT/uvcdat/issues/851)

### VisTrails

 * **Bug**: [uvcdat script broken](https://github.com/UV-CDAT/uvcdat/issues/894)

### cdms2

 * **Enhancement**: [convert cdtime object to datetime](https://github.com/UV-CDAT/uvcdat/issues/771)

### cdutil/genutil

 * **Bug**: [full averaging weirdness](https://github.com/UV-CDAT/uvcdat/issues/757)

## Merged Pull Requests

 * [#748: Removes scripts from images/ directory](https://github.com/UV-CDAT/uvcdat/pull/748)
 * [#791: Fixes BUILDINSOURCE detection](https://github.com/UV-CDAT/uvcdat/pull/791)
 * [#827: Vcs dv3d separate plot constituents updated](https://github.com/UV-CDAT/uvcdat/pull/827)
 * [#828: Typo when disabling a package](https://github.com/UV-CDAT/uvcdat/pull/828)
 * [#831: Patches Python to remove global OSX packages](https://github.com/UV-CDAT/uvcdat/pull/831)
 * [#833: Makes missing GIT_PROTOCOL an error](https://github.com/UV-CDAT/uvcdat/pull/833)
 * [#835: Makes git_update.sh handle detached heads](https://github.com/UV-CDAT/uvcdat/pull/835)
 * [#836: Fixes typo in vistrails_external.cmake](https://github.com/UV-CDAT/uvcdat/pull/836)
 * [#904: Issue 898 vertical flipped monotonic decreasing](https://github.com/UV-CDAT/uvcdat/pull/904)
 * [#905: Issue 691 interact mac broken](https://github.com/UV-CDAT/uvcdat/pull/905)
 * [#907: Vcs3 d fix z axis problems](https://github.com/UV-CDAT/uvcdat/pull/907)
 * [#912: Vcs3 d fix animation exception](https://github.com/UV-CDAT/uvcdat/pull/912)
 * [#936: update images for dv3d_hovmoller_test and dv3d_slider_test](https://github.com/UV-CDAT/uvcdat/pull/936)
 * [#940: Fix error causing 3D plots to hang](https://github.com/UV-CDAT/uvcdat/pull/940)

<a id="2.0"></a>

# 2.0 Changelog

## Closed Issues

### Build

 * **Bug**: [setup_runtime.sh needs to be sourced with full path ](https://github.com/UV-CDAT/uvcdat/issues/522)
 * **Bug**: [some regrid test try to import matplotlib even though they don't really need it](https://github.com/UV-CDAT/uvcdat/issues/574)
 * **Bug**: [VTK doesn't build (freetype headers problem)](https://github.com/UV-CDAT/uvcdat/issues/594)
 * **Bug**: [Building on Mac OS X 10.9.4 doesn't locate sqlite3 (no build error)](https://github.com/UV-CDAT/uvcdat/issues/588)
 * **Bug**: [mac os 10.8/10.9](https://github.com/UV-CDAT/uvcdat/issues/562)
 * **Bug**: [CDAT_BUILD_MODE=ALL does NOT build ALL](https://github.com/UV-CDAT/uvcdat/issues/544)
 * **Bug**: [uvcdat build needs QMake even for DEFAULT and no GUI](https://github.com/UV-CDAT/uvcdat/issues/554)
 * **Enhancement**: [sciFuncs submodule needs to be put in our source code,](https://github.com/UV-CDAT/uvcdat/issues/635)
 * **Enhancement**: [Binaries release for 2.0](https://github.com/UV-CDAT/uvcdat/issues/618)

### UVCDAT GUI

 * **Bug**: [color map in GUI doesn't work](https://github.com/UV-CDAT/uvcdat/issues/640)
 * **Bug**: [uvcdat gui vcs plots do not stick in spreadsheet](https://github.com/UV-CDAT/uvcdat/issues/575)
 * **Bug**: [animation auto min/max is broken](https://github.com/UV-CDAT/uvcdat/issues/639)
 * **Bug**: [Adjusting color map is broken](https://github.com/UV-CDAT/uvcdat/issues/677)
 * **Bug**: [vcs windows do not stick in spreadsheet](https://github.com/UV-CDAT/uvcdat/issues/589)

### VCS

 * **Bug**: [possible isofill issue](https://github.com/UV-CDAT/uvcdat/issues/519)
 * **Bug**: [test set_opt_polar does not plot in bg](https://github.com/UV-CDAT/uvcdat/issues/626)
 * **Bug**: [boxfill as a .list() that needs to be removed](https://github.com/UV-CDAT/uvcdat/issues/625)
 * **Bug**: [kill uvcdat gui middle of animation generating leads to many vtk errors](https://github.com/UV-CDAT/uvcdat/issues/617)
 * **Bug**: [yx datawc_y1, y2 not respected anymore....](https://github.com/UV-CDAT/uvcdat/issues/669)
 * **Bug**: [animations now need PyQt4 old code seems broken](https://github.com/UV-CDAT/uvcdat/issues/579)
 * **Bug**: [flip does not work when missing values](https://github.com/UV-CDAT/uvcdat/issues/661)
 * **Bug**: [VCS won't plot when every value is exactly zero](https://github.com/UV-CDAT/uvcdat/issues/648)
 * **Bug**: [Close Does Not Work](https://github.com/UV-CDAT/uvcdat/issues/718)
 * **Bug**: [The "clear" does nothing. ](https://github.com/UV-CDAT/uvcdat/issues/717)
 * **Bug**: [colormap does not stick on animation](https://github.com/UV-CDAT/uvcdat/issues/676)
 * **Bug**: [VTKPlots.plotVectors points/attributes length mismatch](https://github.com/UV-CDAT/uvcdat/issues/712)
 * **Bug**: [x.show missing](https://github.com/UV-CDAT/uvcdat/issues/596)
 * **Bug**: [Isofill does not work with polar coordinates](https://github.com/UV-CDAT/uvcdat/issues/586)
 * **Bug**: [boxfill draws outside range](https://github.com/UV-CDAT/uvcdat/issues/620)
 * **Bug**: [boxfill not fully plotted (lat bit white)](https://github.com/UV-CDAT/uvcdat/issues/627)
 * **Bug**: [test_dump_json broken](https://github.com/UV-CDAT/uvcdat/issues/624)
 * **Bug**: [x.interact() fails in vcs (None object)](https://github.com/UV-CDAT/uvcdat/issues/634)
 * **Bug**: [inverted levels do not plot properly](https://github.com/UV-CDAT/uvcdat/issues/637)
 * **Bug**: [wrapping in projection not quite working](https://github.com/UV-CDAT/uvcdat/issues/566)
 * **Bug**: [Scatter plot won't plot the scatters](https://github.com/UV-CDAT/uvcdat/issues/724)
 * **Bug**: [meshfill does not seem to mask](https://github.com/UV-CDAT/uvcdat/issues/551)
 * **Bug**: [X and Y axis lables (xname, yname) won't show up on for any graphics method on the plot](https://github.com/UV-CDAT/uvcdat/issues/743)
 * **Bug**: [boxfill does NOT show all data](https://github.com/UV-CDAT/uvcdat/issues/555)
 * **Bug**: [markers are stretched too much when x and y scales are too different](https://github.com/UV-CDAT/uvcdat/issues/553)
 * **Bug**: [vcs init fails if no initial.attributes](https://github.com/UV-CDAT/uvcdat/issues/614)
 * **Bug**: [Test cdms_load_and_plot_axis_variable fails](https://github.com/UV-CDAT/uvcdat/issues/689)
 * **Enhancement**: [read new json formatted initial file attribute](https://github.com/UV-CDAT/uvcdat/issues/597)
 * **Enhancement**: [remove setcolormap warning](https://github.com/UV-CDAT/uvcdat/issues/598)
 * **Enhancement**: [easily removable error warning when saving to new json file](https://github.com/UV-CDAT/uvcdat/issues/619)

### VisTrails

 * **Bug**: [vistrails module uvcdat_cdms missing](https://github.com/UV-CDAT/uvcdat/issues/581)
 * **Bug**: [isoline plots don't plot on first try](https://github.com/UV-CDAT/uvcdat/issues/611)

### cdms2

 * **Enhancement**: [Read ACME test data](https://github.com/UV-CDAT/uvcdat/issues/658)

## Merged Pull Requests

 * [#739: Vcs3d record animation](https://github.com/UV-CDAT/uvcdat/pull/739)
