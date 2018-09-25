#! /usr/bin/env python 
# Este script ejecuta el programa PseudoSP.e para resolver una ecuacion diferencial con condiciones de contorno dadas en el archivo BoundaryCond.dat. Luego grafica el resultado y guardandolo en un archivo.

from os import path, getcwd, remove, makedirs
from sys import stdout
from shutil import move, copy, rmtree
from glob import glob
from subprocess import call
import numpy as np
import matplotlib.pyplot as plt

controlParameterList = {
    'rootDir'               :   path.abspath('../hcc-project/'),
    'resultDir'             :  'results',
    'resultFile'            :  'results.dat'
}

OdeSolverControl = {
    'mainDir'		      :    'OdeSolver',
    'executable'	      :    'OdeSolver',
    'initialOdeSDir'      :    'initial',
    'resultOdeSDir'       :    'results',	
    'resultOdeSFile'      :    'results.dat'
}

PlotControl = {
    'PlotDir'             :    'Plots'
}



def OdeSolver_simple():
    #Ejecuta el programa OdeSolver con las condiciones iniciales.
    #Set directory strings
    OdeSDirectory = path.join(controlParameterList['rootDir'],OdeSolverControl['mainDir'])
    OdeSIDirectory = path.join(OdeSDirectory,OdeSolverControl['initialOdeSDir'])
    OdeSResultsDirectory = path.join(OdeSDirectory,OdeSolverControl['resultOdeSDir'])
    OdeSExecutable = OdeSolverControl['executable']

    #Check executable
    checkExistenceOfExecutable(path.join(OdeSDirectory, OdeSExecutable))
    
    # clean up initial and results folder

    # form executable string
    executableString = ("./" +OdeSExecutable)
    # run executable
    run(executableString, cwd=OdeSDirectory)
    copy(path.join(OdeSResultsDirectory,OdeSolverControl['resultOdeSFile']),path.join(controlParameterList['rootDir'],controlParameterList['resultDir']))




def cleanUpFolder(aDir):
    """ Delete all data files in the given directory. """
    if path.exists(aDir):
        try:
            run("rm -rf *", cwd=aDir, echo=False)
        except OSError:
            pass # very likely the the folder is already empty
    else:
        makedirs(aDir)


def checkExistenceOfExecutable(executableFilename):
    """ Check the existence of the executable file, and compile if not. """
    if not path.exists(executableFilename):
        # build then clean
        exec_path, exec_filename = path.split(executableFilename)
        run("make", cwd=exec_path)
        # if still cannot find the executable
        if not path.exists(executableFilename):
            raise ExecutionError(
                         "Cannot generate executable %s!" % executableFilename)

def run(command, cwd=getcwd(), echo=True):
    """ Invoke a command from terminal and wait for it to stop. """
    if echo:
        print("-"*80)
        print("In "+cwd)
        print("Executing command: "+command)
        print("-"*80)
        stdout.flush()
    return call(command, shell=True,cwd=cwd)

def plot(Dir):
# La variable Dir es una string con la direccion del archivo de datos que quiero graficar.
    Data = np.loadtxt(Dir)
    x = Data[:,0]
    y = Data[:,1]
# Crea el grafico y lo guarda en el directorio plots
    plt.figure()
    plt.plot(x,y,'b--')
    plt.xlabel('x')
    plt.ylabel('y ')
    plt.axis([0,6,0,17])
    plt.legend( ('y'), loc = 'upper right')
    plt.savefig('plots/plot1', dpi = 300)
    plt.show()
    return 0






