# WEC OpenFOAM Open Datasets
<div align="justify">
Welcome to the landing page for the Wave Energy Converter (WEC) OpenFOAM Open Datasets!

<br /> 
This repository is a collection of templates, examples, helper scripts, and data-sets compiled with the goal of improving the accessibility of high-fidelity CFD simulation of WECs using OpenFOAM. 

### Case types
This repository's goal is to provide datasets related to each stage of the WEC simulation and analysis workflow (shown below in Figure 1). At the end, users will find a simulation setup for the Reference Model 6, with mooring and a Power Take-Off model.  
<br />

As such, the case types provided in this directory are: 
* waves-only: set-ups needed to simulate a wave flume with either regular or irregular waves.  
* mesh generation: this specifically features the steps needed to generate body-fitted device meshes using <tt>snappyHexMesh</tt>, which can then be merged with the simulation domain mesh and used in waves + device simulations 
* decay testing: Free decay of a given device -- coupled simulations of rigid body dynamics + CFD, without waves. 
* waves + device: Coupled simulations of rigid body dynamics + CFD with waves. 
  * With or without mooring 
  * In 3D for the RM6, there is an option to additionally model the RM6's Power Take-Off (PTO) system. 

For each case featuring device geometry, two options are provided: a rubber ducky geometry (for a more light-hearted introductory example), or the Reference Model 6 (to see what the set-ups look like for a real WEC device).

<p align="middle">
  <img src="https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/images/WEC_analysis_workflow_v3.png" height="200"/>
</p>

<p align='middle'> Figure 1 - Steps to the typical WEC analysis workflow </p>



### <tt>template</tt> vs <tt>example</tt>
In this repository, you will encounter two kinds of directories per case type: template, and example. 

A <tt>template</tt> is a baseline case setup (for each case type) that provides a generic guide for how to set up that kind of case. The interested user can make modifications to a given <tt>template</tt> case to adapt it to their own needs. 

The <tt>example</tt> cases provided are all built off the <tt>template</tt> case of the same type, and therefore provide examples for how a given <tt>template</tt> may be modified to produce different results. 

As such, the README files for the <tt>template</tt> directories will provide more basic information about their given case type, while the READMEs for the <tt>example</tt> may provide more information about the specific examples being presented, analysis of those example data sets, etc. 

### The <tt>flowParams</tt> text file
To simplify and centralize the user's interaction with the OpenFOAM dictionary files, a text-based user interface is provided in the form of a text file named <tt>flowParams</tt>. The provided simulation set-ups in this repository have been developed such that most settings a user might want to modify can be adjusted by editing the <tt>flowParams</tt> file. Other more advanced settings (such as solver settings) have been pre-selected for the user. This is done by providing the <tt>flowParams</tt> file as an <tt>include</tt> to the rest of the relevant OpenFOAM dictionary files, so that they read settings from <tt>flowParams</tt>.

<p align="middle">
  <img src="https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/images/flowParams_usage.png" height="200"/>
</p>

<p align='middle'> Figure 2 - Case structure for provided simulation setups, with <tt>flowParams</tt> serving as an interface for the user with the rest of the OpenFOAM dictionary files.</p>


### Pre-packaged simulation data
In order to provide the user with a way to "check their work" and give a sense of what output data for a certain case should look like, pre-packaged simulation data of some form is often provided with the <tt>example</tt> cases. As the raw output data from OpenFOAM can be quite large, the datasets typically provided are created from post-processing the raw OpenFOAM output in some form. The auxiliary scripts needed to do this post-processing are provided. These are typically a combination of bash and python scripts.  

### Recommended work-flow
The simulation set-ups and datasets provided here have been developed such that a user may work their way through cases that successively increase in complexity, and work their way piece-by-piece through the typical WEC simulation & analysis work-flow. The recommended order is as follows: 
* Begin with waves-only setups found in [template_wave_flume](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/template_wave_flume) and [examples_wave_flume](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/examples_wave_flume)
* Review mesh generation for body-fitted meshes in [template_mesh_generation](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/template_mesh_generation) and [examples_mesh_generation](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/examples_mesh_generation)
* Review decay tests as found in [template_free_decay](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/template_free_decay)
* Work through the waves + device cases (for both 2D and 3D) provided in [template_2D3D_Simulation](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/template_2D3D_Simulation), [examples_2D_Simulations](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/examples_2D_Simulations), and [examples_3D_Simulations](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/examples_3D_Simulations)
  * Note: It is within these example directories that the user will find some decay test examples as well (i.e. "ducky drop" examples)
  * Here, it is advised to start with unmoored cases without PTO, before advancing to cases with mooring and/or PTO modeling 

The final case (of most complexity) at the end of this work-flow is the Reference Model 6 in 3D, with mooring and a PTO model. 

Of course, users are free to engage in whatever order suits their level and interest. 

### About OpenFOAM 
OpenFOAM is a free, open-source, CFD software. Simulation setups are designed and run using text-based dictionary files. The datasets provided in this repository assume the user's awareness of OpenFOAM, and a basic understanding of how OpenFOAM simulation setups are put together and run. For more information on OpenFOAM, the interested user is referred to https://www.openfoam.com/documentation/overview . For instructions on building OpenFOAM (for linux), please see https://develop.openfoam.com/Development/openfoam/-/blob/master/doc/Build.md . 

The datasets provided in this repository were put together using OpenFOAM v2312. 


### About the Reference Model 6
The Reference Model 6 (RM6) is a Backward Bent Duct Buoy (BBDB), a type of oscillating water column wave energy converter. The BBDB consists of an air chamber, an L-shaped duct, bow and stern buoyancy modules, and a power take-off (PTO) system composed of a Wells air turbine and a generator, as shown in Figure 1. This L-shaped device opens to the ocean downstream from the wave propagation direction. Power is generated by the motion of the wave, which causes variations in the ambient pressure within the air chamber, forcing air to flow through the Wells turbine. Figure 3 illustrates the main components and dimensions of a BBDB. For more information on the Reference Model 6, go to https://openei.org/wiki/PRIMRE/Signature_Projects/Reference_Model_6:_Oscillating_Water_Column
</div>
&nbsp;

<p align="middle">
  <img src="https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/images/rm6.png" height="200"/>
  <img src="https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/tree/main/images/rm6-dimensions.png" height="200"/>
</p>

<p align='middle'> Figure 3 - RM6 BBDB Device Design and Dimensions</p>



## References


