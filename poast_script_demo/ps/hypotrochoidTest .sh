cat hypotrochoid.ps > temp.ps
tail -n +2 hypotrochoidTest.ps >> temp.ps
gs -f temp.ps
