## 2D/3D OpenFOAM Mesh Generation Example Cases

### Cases
- 2D Reference Model 6 (RM6) with no PTO
- 2D Ducky Drop
- 3D Reference Model 6 (RM6) with no PTO
- 3D Reference Model 6 (RM6) with PTO
- 3D Ducky Drop

### Setup
- **CAD model**: Included in each of the sample case.
- **Single Processor**: Use the `Allrun.ser` script in each case to run on a single processing unit.
- **Multiple Processors**: Use the `Allrun` script in each case to run on multiple processing units.
    - For parallel runs, the number and type of domain decompositions can be adjusted in `<caseMesh>/background/system/decomposeDict`.

