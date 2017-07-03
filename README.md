# Automation of Parameter Variation and Real time Plotting for OpenFOAM using PyFOAM


## Table Of Content



1. Introduction

2. Getting started(Installation)

    1. Requirements
    
	2. Setting-up script in your local machine
		1.  Setup using sources
		2.  Setup using pip

	3. How to use the script
3. Special Mention 


## 1. Introduction

Many a times one may want to change the value of a certain CFD system parameter over a given range of values and observe the behavior of the system.

[OpenFOAM](https://openfoam.org/) provides a rich set of numerical solvers which can be used to simulate the system for given values of its parameters.

[PyFOAM](https://openfoamwiki.net/index.php/Contrib/PyFoam)(very much different from pythonFlu) provides many facilites like plotting the state of variables in parallel to simulation, manipulating a set of dictionary files, plotting results from the OpenFOAM logs and more.

But what if one needs to save the plots for different multiple values(100's or 1000's) of a single parameter and wants to save those plots for future reference?

That is where our script comes in handy which has following capabilities:

1) Can simulate the same system, but for different values of parameter automatically.

2) Saving the plots of results generated for each simulation

3) Append all the plots to a .tex file which can be later compiled to .pdf format for analysis



The ```src``` package in this repository contains all the source code and also you can find about implementation and using those modules in README file there.





## 2. Getting Started(Installation)

Follow the steps below to use the script

### 2.1 Requirements

For the script to run in your machine, following must be present in your machine

1) Ensure Python is installed

2) Ensure [pip](https://pip.pypa.io/en/latest/installing.html) is installed.

 - Type following command to install pip
       ```sudo apt-get install python-pip python-dev build-essential```

3) Ensure OpenFOAM is installed.

The detailed instructions on how to install OpenFOAM can be found [here](https://openfoamwiki.net/index.php/Installation/Linux/OpenFOAM-4.1/Ubuntu)

4) Ensure python package [numpy](https://www.numpy.org) is installed

 - You can type following commad to install numpy: 
 
 ```sudo pip install numpy```

5) Ensure gnuplot is installed

 - You can type following command to install gnuplot:

	``` sudo apt-get install gnuplot-x11 ```

6) Ensure PyFOAM is installed

 - You can type following command to install gnuplot:

	``` sudo pip install PyFoam ```



### 2.2 Setting Up the Script in your machine

### 2.2.1 Setup using sources 

Extract it and make sure that you have all the requirements satisfied

Now type following command in terminal to setup the script

```sudo python setup.py install```



### 2.2.2 Setup using pip

In this method, you don't need to download sources

Just type following command and all the scripts will be installed automatically

 - ```sudo pip install git+https://github.com/b282022/Parameter-Variation-In-PyFoam```

### 2.3 How to use the script

In a OpenFOAM case directory, one can use this script with following four command line arguments:
1. The path_of_dictionary_file
2. The parameter name with its full path
3. The range in which parameter is to be updated
4. The OpenFOAM solver which is to be used for the case

For example, if we want to change the tolerance of p of an icoFoam OpenFOAM case from 1e-5 to 1e-4 at the intervals of 1e-5, stored in system sub-directory's fvSolution file then we will provide following command-line arguments 
1. Path of dictionary file ./system/fvSolution
2. Parameter name with its full path: solvers/p/tolerance
3. Range of parameter: 1e-5:1e-5:1e-4
4. OpenFOAM solver: icoFoam

So the command would look like:
```pyfoam_automated.py ./system/fvSolution solvers/p/tolerance 1e-5:1e-5:1e-4 icoFoam```

The help can be also found by typing following command in terminal:
```pyfoam_automated.py --help```

Also the detailed documentation can be found in the src sub-directory of this repository.

## 3. Special Mention
All this would not have been possible without support of
1. OpenFOAM
2.  PyFOAM
3. And other packages required to build

