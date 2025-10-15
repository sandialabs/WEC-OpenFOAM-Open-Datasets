# 🚀 Quickstart

This page gets you from **clone → run → verify**.  
For the full case list, see the [Templates and Examples Index](template-example-index.md).

## 1) 📋 Prerequisites
- OpenFOAM v1906 and later (sourced into your shell)  
- Python with `numpy`, `pandas`, `glob`, `matplotlib` for plotting  

## 2) 📥 Clone
```bash
git clone https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets.git
cd WEC-OpenFOAM-Open-Datasets
```

## 3) 🌊 Start with the waves-only template
Copy the template, edit inputs in one file, and run a short smoke test:

```bash
cp -r template_wave_flume my_wave_case
cd my_wave_case
```

Edit **`flowParams`** (see [Reference on flow parameter](flowParams_reference.md) for the full list of configurable parameters):
- set `waveType` (0 for regular, 1 for irregular)  
- choose `waveModel`  
- set `waveHeight` and `wavePeriod`  
- adjust `simDuration` and `writeInterval` if needed  

Source OpenFOAM helpers:
```bash
. $OPENFOAM_INSTALL_DIR/etc/bashrc
. ${WM_PROJECT_DIR:?}/bin/tools/RunFunctions
. ${WM_PROJECT_DIR:?}/bin/tools/CleanFunctions
```

Run a serial smoke test:
```bash
./Allrun.ser
tail -f log.interFoam
```

Optional parallel run after setting `system/decomposeParDict`:
```bash
./Allrun
```

Irregular waves (only if `waveType = 1`):
```bash
cd processing_scripts
python setIrregWave.py    # writes constant/waveInput.txt
cd ..
./Allrun.ser
```

Outputs will appear in `postProcessing/` and in time folders `0, 1, 2, ...`.

## 4) 📊 Post‑process and Verification

A full description of all post‑processing and plotting scripts is provided in  
[Post‑process and Data Guide](post_process_and_data.md).

Here are a few common examples:

```bash
# Extract motion and forces
./extractMotion.sh   path/to/caseA path/to/caseB
./extractForces.sh   path/to/caseA path/to/caseB

# Plot wave gauges and motion
python plotWaves.py   path/to/caseA
python plotMotion.py  path/to/caseA
```
- ## 5) ⚠️ If results differ
- Recheck `flowParams` (H, T, duration, write interval)  
- Confirm `constant/polyMesh/` exists for device cases  
- Scan the solver log for early stops or large CFL values  
- Re-run a short serial test before long parallel runs  
- If problems persist, [create an issue](https://github.com/sandialabs/WEC-OpenFOAM-Open-Datasets/issues) with details of your case and logs  
