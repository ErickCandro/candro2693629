class vehiculo:
    pass
class landvehiculo:
    pass
class trackedvehiculo:
    pass
for cls1 in [vehiculo, landvehiculo, trackedvehiculo]:
    for cls2 in [vehiculo, landvehiculo, trackedvehiculo]:
        print (issubclass (cls1,cls2),end="/t")
    print ()