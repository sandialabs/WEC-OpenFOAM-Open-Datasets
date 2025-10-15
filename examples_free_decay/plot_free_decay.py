#!/usr/bin/env python3
#--------------------------------------------------------------------------------#
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation
from scipy.signal import find_peaks

#--------------------------------------------------------------------------------#
# Settings
nCycles = 4
roundN = 4

#--------------------------------------------------------------------------------#
def readData(filename, pitch_offset=0.0, roll_offset=0.0):
    """Reads Motion.txt and extracts time, roll, heave, and pitch."""
    ufData = pd.read_csv(filename, sep=r"\s+|\t,", header=None, skiprows=6,
                         names=range(100), engine="python")

    time = ufData[0]
    heave = ufData[3]

    Xr = np.array([[ufData[4], ufData[5], ufData[6]],
                   [ufData[7], ufData[8], ufData[9]],
                   [ufData[10], ufData[11], ufData[12]]])

    roll = []
    pitch = []
    for i in range(len(time)):
        rotM = np.array([[Xr[0][j][i] for j in range(3)],
                         [Xr[1][j][i] for j in range(3)],
                         [Xr[2][j][i] for j in range(3)]])
        euler = Rotation.from_matrix(rotM).as_euler("zyx", degrees=True)
        roll.append(euler[2])
        pitch.append(euler[1])

    heave -= heave[0]
    roll = np.array(roll) - roll_offset
    pitch = np.array(pitch) - pitch_offset

    return time.values, heave.values, pitch, roll

#--------------------------------------------------------------------------------#
def getNaturalFreq(times, Z, min_peak_spacing=0.5):
    """Computes damping ratio and natural frequency from peaks, with filtering."""
    raw_peaks, _ = find_peaks(-Z)
    raw_peaks = np.insert(raw_peaks, 0, 0)  # include initial point

    # Filter peaks based on minimum time spacing
    filtered_peaks = [raw_peaks[0]]
    for idx in raw_peaks[1:]:
        if times[idx] - times[filtered_peaks[-1]] >= min_peak_spacing:
            filtered_peaks.append(idx)
    peaks = np.array(filtered_peaks)

    if len(peaks) < nCycles + 1:
        print("Not enough valid peaks after filtering.")
        return None, None, None, peaks

    # Periods between peaks
    periods = [times[peaks[i+1]] - times[peaks[i]] for i in range(nCycles-1)]

    # Logarithmic decrement and damping ratio
    deltaV = []
    zetaV = []
    for i in range(nCycles-1):
        temp = np.log(Z[peaks[i]] / Z[peaks[i+1]])
        deltaV.append(temp)
        zetaV.append(temp / np.sqrt(4 * np.pi**2 + temp**2))

    RMS = round(np.sqrt(np.mean([Z[p]**2 for p in peaks[:nCycles]])), roundN)
    zeta = round(np.mean(zetaV), roundN)

    wn = [np.sqrt((2*np.pi/p)**2 - z**2) for p, z in zip(periods, zetaV)]
    wn = round(np.mean(wn), roundN)
    wd = 2 * np.pi / np.mean(periods)

    return zeta, wd, wn, peaks

#--------------------------------------------------------------------------------#
def detect_signal_type(case_name):
    """Detects whether the case is pitch, heave, or roll based on folder name."""
    name = case_name.lower()
    if "pitch" in name:
        return "pitch"
    elif "heave" in name:
        return "heave"
    elif "roll" in name:
        return "roll"
    else:
        return "pitch"  # default

#--------------------------------------------------------------------------------#
def main():
    if len(sys.argv) < 2:
        print("Usage: python plot_decay_response.py caseA caseB ...")
        sys.exit(1)

    plt.figure(figsize=(12, 4))
    last_signal_type = "Response"

    for case in sys.argv[1:]:
        folder = os.path.abspath(case)
        data_file = os.path.join(folder, "Motion.txt")

        if not os.path.exists(data_file):
            print(f"Skipping {case}: Motion.txt not found.")
            continue

        signal_type = detect_signal_type(case)
        last_signal_type = signal_type
        time, heave, pitch, roll = readData(data_file, pitch_offset=10.0, roll_offset=0.0)

        if signal_type == "pitch":
            Z = pitch
        elif signal_type == "heave":
            Z = heave
        elif signal_type == "roll":
            Z = roll
        else:
            raise ValueError(f"Unknown signal type: {signal_type}")

        # Peak-based
        if signal_type == "heave":
            zeta_p, wd_p, wn_p, peaks = getNaturalFreq(time, Z, min_peak_spacing=2.5)
        else:
            zeta_p, wd_p, wn_p, peaks = getNaturalFreq(time, Z, min_peak_spacing=0.0)

        # Plot
        label = f"{os.path.basename(os.path.normpath(case))}\n$T_d$: {round(2*np.pi/wd_p, 2)} s"
        plt.plot(time, Z, label=label)
        plt.plot(time[peaks], Z[peaks], '*')

    plt.xlabel("Time (s)")
    if signal_type == "heave":
        plt.ylabel(f"{last_signal_type.capitalize()} (m)")
    else:
        plt.ylabel(f"{last_signal_type.capitalize()} (degrees)")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

#--------------------------------------------------------------------------------#
if __name__ == "__main__":
    main()

