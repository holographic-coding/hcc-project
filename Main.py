#!/usr/bin/env python
# call the real shell
from os import path, getcwd, remove, makedirs
import Driver

#Ejecutamos el modulo de c++   
Driver.OdeSolver_simple()
 
#Especificamos la direccion del archivo que queremos graficar
DirRes = path.join(Driver.controlParameterList['rootDir'],Driver.controlParameterList['resultDir'])
DireResultData = path.join(DirRes,Driver.controlParameterList['resultFile'])

#Creamos el grafico
Driver.plot(DireResultData)


