# WEC OpenFOAM Open Datasets
<div align="justify">
Welcome to the landing page for the Wave Energy Converter (WEC) OpenFOAM Open Datasets!

<br /> 
<br /> 
This repository is a collection of templates, examples, helper scripts, and data-sets compiled with the goal of improving the accessibility of high-fidelity CFD simulation of WECs using OpenFOAM. 

## Case types
We provide datasets for each stage of a typical WEC simulation and analysis workflow. The final stage is a 3D Reference Model 6 (RM6) configuration with optional mooring and PTO.

- **Waves-only** — 2D wave flume setups with regular or irregular seas  
- **Mesh generation** — body-fitted device meshes via `snappyHexMesh` for waves + device runs  
- **Decay testing** — free decay of a device (rigid-body dynamics + CFD, no waves)
- **Waves + floating object** - coupled rigid-body dynamics + CFD with waves
  - Example include a simple floating “rubber ducky”
- **Waves + device** — coupled rigid-body dynamics + CFD with waves + tether + PTO  
  - optional mooring  
  - optional PTO in 3D RM6 cases
  - Examples include the RM6 reference device.

<p align="middle">
  <img src="https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/blob/main/images/WEC_analysis_workflow_v3.png" height="200"/>
</p>

<p align='middle'> Figure 1 - Steps to the typical WEC analysis workflow </p>

## `template` vs `example`

Each case type has:
- **`template_*`** — baseline setup you can copy and adapt
- **`examples_*`** — built from the template; includes processed outputs and plotting scripts
  
## The All‑in‑One Control `flowParams` File

User interaction with OpenFOAM dictionaries is centralized in a single configuration file called flowParams. Most adjustable parameters are defined in this file, while advanced solver settings are pre‑configured. All other dictionaries reference flowParams, so their parameter values are read directly from it.

<p align="middle">
  <img src="https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/blob/main/images/flowParams_usage.png" height="200"/>
</p>

<p align='middle'><em>Figure 2 — Case structure with <code>flowParams</code> included by OpenFOAM dictionaries</em></p>

## Recommended workflow

Work through cases that increase in complexity:

1) **Waves-only**  
   - Templates: [`template_wave_flume/`](template_wave_flume/)  
   - Examples:  [`examples_wave_flume/`](examples_wave_flume/)

2) **Mesh generation**  
   - Templates: [`template_mesh_generation/`](template_mesh_generation/)  
   - Examples:  [`examples_mesh_generation/`](examples_mesh_generation/)

3) **Decay testing**  
   - Templates: [`template_free_decay/`](template_free_decay/)
   - Examples: [`examples_free_decay/`](examples_free_decay/)
  
4) **Prescribed oscillation**  
   - Templates: [`template_prescribed_oscillation/`](template_prescribed_oscillation/)
   - Examples: [`examples_prescribed_oscillation/`](examples_prescribed_oscillation/)

5) **Waves + device (2D/3D)**  
   - Template:  [`template_2D3D_Simulation/`](template_2D3D_Simulation/)  
   - Examples:  [`examples_2D_Simulations/`](examples_2D_Simulations/), [`examples_3D_Simulations/`](examples_3D_Simulations/)  
   - Tip: start unmoored without PTO, then add mooring, then PTO

**Final step:** 3D **RM6** with mooring and PTO (see [`examples_3D_Simulations/`](examples_3D_Simulations/)).


## Data & docs

This repository includes both **data** (processed outputs in example folders) and **documentation** to guide you through setup, execution, and analysis:

- **Quickstart**: [docs/quickstart.md](docs/quickstart.md) — clone, run, and verify a case  
- **Templates & Examples Index**: [docs/template-example-index.md](docs/template-example-index.md) — overview of all available case types  
- **flowParams Reference**: [docs/flowParams_reference.md](docs/flowParams_reference.md) — full list of configurable parameters  
- **Post‑process and Data Guide**: [docs/post_process_and_data.md](docs/post_process_and_data.md) — details on extracting, processing, and plotting results  
- **RM6 Overview**: [docs/rm6-overview.md](docs/rm6-overview.md) — background on the Reference Model 6 device  

Each example folder also includes small processed outputs and plotting scripts so you can quickly check your results against reference data.  

## About OpenFOAM and RM6

- Built and tested with **OpenFOAM v2306** and **OpenFOAM v2312**. 
- RM6 device background and figures are summarized in [`docs/rm6-overview.md`](docs/rm6-overview.md).


## License

GPL-3.0. See [`LICENSE`](LICENSE).
