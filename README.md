# GaussBuster: Speech/Voice Enhancement Framework

## Overview
GaussBuster is a speech and voice enhancement framework focused on improving the listenability and perceptual quality of spoken audio. The repository contains tools and notebooks to prepare speech datasets (small LibriSpeech subsets, VoxCeleb preparations) and evaluate enhancement results using objective speech-quality metrics.

## Project Goals
- Improve speech listenability and intelligibility for degraded recordings.
- Develop and evaluate denoising/restoration methods specifically for speech.
- Provide a reproducible pipeline for preparing speech datasets and generating a high-quality subset for model training or evaluation.
- Evaluate outputs using perceptual and intelligibility metrics.

## Features
- Targeted speech enhancement algorithms (denoising, dereverberation, artifact removal).
- Dataset preparation notebooks and scripts for speech corpora (e.g., LibriSpeech subset, VoxCeleb preprocessing).
- Quality metrics evaluation: PESQ, STOI, and SNR.
- Batch processing and metadata generation for selected high-quality speech samples.

## Dataset
This project focuses on speech datasets rather than environmental sounds. Example data sources you may see in the repo or notebooks:
- LibriSpeech (small subsets used for quick experiments)
- VoxCeleb (preparation scripts/notebooks exist to extract and evaluate speech samples)

The included notebook `prepare_metadata_dataset.ipynb` demonstrates downloading or sampling speech corpora, extracting WAV files, computing PESQ/STOI/SNR, and saving a metadata CSV plus a `high_quality_audio/` folder.

## Installation
Create and activate a virtual environment and install required Python packages. A minimal set of packages used by the notebooks:

```powershell
# Create and activate virtual environment
python -m venv .venv; .venv\Scripts\Activate.ps1

# Install common requirements (adjust as needed)
pip install -r requirements.txt
```

If you use the notebooks directly, the cells install packages such as `torchaudio`, `librosa`, `pesq`, `pystoi`, `pandas`, `tqdm`, and `soundfile`.

## Usage
1) Prepare a speech dataset (example: run the notebook to sample LibriSpeech or prepare VoxCeleb-derived audio):

Open `prepare_metadata_dataset.ipynb` with Jupyter/VS Code and run the cells. The notebook will:
- download or sample a speech corpus (or use an existing local copy),
- resample and save WAV files,
- compute PESQ/STOI/SNR for each file,
- write a `metadata.csv` and copy high-quality WAV files to `data/librispeech_subset/high_quality_audio/` (paths depend on notebook config).

2) Run enhancement scripts (if available in `src/enhancement/`) against the `high_quality_audio/` or other input directories.

3) Evaluate results using the evaluation utilities (PESQ/STOI/SNR) in `src/evaluation/` or the notebook cells.

## Quality Metrics (guidelines)
- PESQ: higher is better; typical target > 3.0 for good perceptual quality (depends on content).
- STOI: closer to 1.0 is better for intelligibility; target values depend on dataset and noise conditions.
- SNR: higher dB indicates less noise; target depends on use-case (listenability may improve markedly above ~10–20 dB).

## Project Structure
```
GaussBuster/
├── data/                        # Raw and prepared data (LibriSpeech/VoxCeleb subsets)
│   └── librispeech_subset/
│       ├── raw/
│       └── high_quality_audio/
├── notebooks/
│   └── prepare_metadata_dataset.ipynb
├── src/

```

## Next steps & notes
- If you want the README to include exact install pins, I can generate a `requirements.txt` from the notebook's pip installs.
- If you have a preferred dataset (VoxCeleb vs LibriSpeech), tell me and I'll tailor the README and notebook docstrings to that choice.

## Contact
Project Link: https://github.com/LeaMyl/GaussBuster