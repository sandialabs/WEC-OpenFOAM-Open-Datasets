# Wave Tank and Simulation Setup Parameters

This section explains the parameters defined in the flowParams file.

## 🌊 Inlet Flow Parameters
- **`Umean`**: Mean inlet velocity (m/s).  
  - Typically set to `0.0` for wave-only cases without background current.

## 🌊 Wave Parameters
- **`sim3D`**: Simulation dimensionality.  
  - `0` → 2D simulation (x–z plane).  
  - `1` → 3D simulation (x–y–z domain).

- **`waterDepth`**: Still water depth in meters.

- **`waveType`**: Type of wave field.  
  - `0` → Regular (single frequency).  
  - `1` → Irregular (spectrum-based).

- **`waveModel`**: Wave theory/model used.  
  - Options: `StokesI` (Airy), `StokesII`, `StokesV`, `Boussinesq`, `Cnoidal`, `Grimshaw`, `streamFunction`.  
  - For irregular waves: specify spectrum (e.g., `Jonswap(freq_min,freq_max,numbers_of_bins)`).

- **`waveHeight`**: Wave height (crest-to-trough) in meters.

- **`wavePeriod`**: Wave period in seconds.

- **`waveAngle`**: Wave incidence angle (degrees).  
  - `0.0` means waves propagate along the x-axis.

- **`wavePhase`**: Initial phase shift of the wave (degrees).

- **`simType`**: Flow regime.  
  - Options: `laminar` or `RAS` (Reynolds-Averaged Simulation).

- **`turbModel`**: Turbulence model used when `simType = RAS`.  
  - Options: `kEpsilon`, `kOmegaSST`, `realizableKE`, etc.

## 📐 Wave Tank Dimensions
- **`tankLength`**: Tank length in meters.  
  - If set to `0`, it is parameterized as `lengthContr * waveLength`.

- **`tankHeight`**: Tank height in meters.  
  - If set to `0`, defaults to `2 × waterDepth`.

- **`tankWidth`**: Tank width in meters.  
  - Only relevant for 3D simulations.

- **`lengthContr`**: Length control factor.  
  - Defines tank length as a multiple of the wave length.

## ⏱️ Time Control
- **`startTime`**: Simulation start time (s).

- **`endTime`**: Simulation end time (s).  
  - If set to `0`:  
    - Regular waves → `20T` (20 wave periods).  
    - Irregular waves → `500T`.

- **`writeElev`**: Output interval for wave elevation probes (s).

- **`writeVTK`**: Output interval for VTK visualization files (s).

## 📊 Wave Probe Locations
Probe positions are defined as multiples of the wave length from the inlet:

- **`Probe1`**: `0.1 × waveLength`  
- **`Probe2`**: `0.5 × waveLength`  
- **`Probe3`**: `1.0 × waveLength`  
- **`Probe4`**: `1.5 × waveLength`  
- **`Probe5`**: `2.0 × waveLength`

## ⚙️ Model Definition (WEC Properties)
- **`objName`**: CAD file name of the device (e.g., `rm6.stl`). Only used for meshing case. 
- **`mass`**: Mass of the object (scaled value).  
- **`objCG`**: Center of gravity coordinates relative to CAD origin.  
- **`gyRad`**: Radii of gyration (x, y, z).  
- **`translate`**: Initial translation vector (scaled).  
- **`objScale`** *(optional)*: Scaling factor for the CAD model.  
- **`rotate`** *(optional)*: Rotation axis and angle (degrees).  
- **`hinge`** *(optional)*: Hinge/rotation point coordinates.

## 🧩 Grid Control (Meshing)
- **`xContr`**: Number of cells per wave length (controls horizontal resolution).  
- **`zContr`**: Number of cells per wave height (controls vertical resolution).  
- **`hContr`**: Height of refinement zone above wave crest (in multiples of wave height).  
- **`nRefineZones`**: Number of refinement levels near the WEC.  
- **`zoneHeightRatio`**: Growth ratio of refinement zone heights.  
- **`zoneWidthRatio`**: Growth ratio of refinement zone widths.  
- **`nLayerOverlap`**: Number of overlapping cell layers around the WEC wall.

## ⏳ Time Step Control
- **`maxCo`**: Maximum Courant number allowed.  
- **`maxDeltaT`**: Maximum time step size (s).

---
