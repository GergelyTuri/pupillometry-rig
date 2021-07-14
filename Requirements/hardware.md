lens 
----
[Tamron 1:1.4](https://www.bhphotovideo.com/c/product/414378-REG/Tamron_23FM25SP_23FM25SP_2_3_25mm_F1_4.html) 25mm filter size: 30.5 mm (metric);

camera
------
Chameleon3 USB3; Model: [CM3-U3-13Y3M-CS](https://www.flir.com/products/chameleon3-usb3/?model=CM3-U3-13Y3M-CS): 1.3 MP, 149 FPS, PYTHON 1300, Mono (CM3-U3-13Y3C-CSRoHS 1.3MP Color Chameleon USB 3.0 Camera 1/2" CMOS CS-Mount [CE][KCC])
_Note_: this is kinda overkill for this. Your target frame rate for pupillometry is in the 5-10 fps range and this camera :point_up: can do up to 150. 

camera accesories
-----------------
1. ACC-01-3002RoHS 7PIN Prewired GPIO JST Connector 
2. ACC-01-0003RoHS Tripod Adapter-3
3. ACC-01-2301RoHS 5 METER USB3.0 CABLE, TYPE-A to MICRO-B (LOCKING) 
see the camera link -> accessories

cs-c adapter
------------
[Fujinon C to CS-Mount 5mm Adapter Ring](https://www.bhphotovideo.com/c/product/1013088-REG/fujinon_c_cs_c_mount_lens_to_cs_mount.html)
_Note_: the camera here is a CS model while the lens has C-mount. This converter is needed to make the two compatible.

IR filter
---------
[FB850-10 Bandpass filter](https://www.thorlabs.com/thorproduct.cfm?partnumber=FB850-10), this only comes in 1" diameter so an adapter is needed for it (see 3d print file). Alternaively one can order a custom cut from Semrock. 

This one did not work for me with 940 nm imaging :point_right: : [NIR Bandpass Filter](https://machinevisionstore.com/catalog/details/898), 30.5 mm Thread Midwest Optical Filters 

IR filter "adapter"
-------------------
see `.stl` file. Optimized for our TAZ filament printer loaded with ABS.

IR light source
---------------
[850 nm LED board](https://www.amazon.com/uxcell-Infrared-Degree-Illuminator-Security/dp/B07PVP57QJ/ref=sr_1_155?dchild=1&keywords=850nm+LED&qid=1605105725&sr=8-155). uxcell 12 LEDs 850nm IR Infrared Board 60 Degree Round Plate IR Illuminator Board Bulb for CCTV Security Camera (or equivalent)

visible light source
--------------------
i used plane blue LED (whatever i found) and an Arduino pin to drive it. The LED was covered with black tape and only a small hole on the tape let through light. 
_Note_: most of the time 2p imaging is done in total darkness (except VR environments) which makes the pupil dilate completely. The visible light pre-constricts it. It is a problem if the visible light hits the detectors so make sure that the objective is shielded. 
      
optional
--------
[2x extender](https://www.edmundoptics.com/p/2x-cs-mount-fixed-focal-length-lens-extenders/13776/) 2X CS-Mount Fixed Focal Length Lens Extenders; Edmund Optics Stock #56-822                       
