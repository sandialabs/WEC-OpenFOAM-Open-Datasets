# Templates and Examples Index

Start with the template for each case type, then open the matching examples to compare outputs and run post-processing.

## Waves-only
- **Template:** [template_wave_flume](../template_wave_flume/)  
  2D wave flume with regular or irregular seas. Edit `flowParams` (wave model, H, T, probes). Irregular waves use `processing_scripts/setIrregWave.py`.
  
- **Examples:** [examples_wave_flume](../examples_wave_flume/)  
  Reference runs with processed outputs and plots for “check your work”.

## Mesh generation
- **Template:** [template_mesh_generation](../template_mesh_generation/)  
  Creating background, body fitted mesh, and refinement zones using `snappyHexMesh`. 

- **Examples:** [examples_mesh_generation](../examples_mesh_generation/)  
  Sample meshes and checks.

## Free-decay (no waves)
- **Template:** [template_free_decay](../template_free_decay/)  
  Free-decay tests for heave, pitch, and roll. Used to estimate natural periods and damping.

## Waves + device (2D and 3D)
- **Template:** [template_2D3D_Simulation](../template_2D3D_Simulation/)  
  Common setup for 2D and 3D cases where waves interact with the body. Requires `constant/polyMesh/` from mesh generation. Optional mooring and PTO.
  
- **2D Examples:** [examples_2D_Simulations](../examples_2D_Simulations/)  
  Includes cases like 2D “ducky drop” and 2D RM6 variants. 
  
- **3D Examples:** [examples_3D_Simulations](../examples_3D_Simulations/)  
  Includes 3D “ducky drop” and 3D RM6 with optional mooring and PTO. 

## Notes
- All cases read user inputs from `flowParams`.
- For parallel runs, set the number of processors in `system/decomposeParDict` and use `./Allrun`.
- Examples folders include processed datasets (for example `Motion.txt`, `Forces.txt`, and `Tensions.txt` when moorings are enabled) and plotting scripts.
