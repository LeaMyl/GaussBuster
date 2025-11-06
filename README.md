# GaussBuster: Audio Enhancement Framework

## Overview
GaussBuster is an audio enhancement framework designed to improve the quality of degraded audio recordings using various denoising and restoration techniques. The project uses the ESC-50 dataset (Environmental Sound Classification) as a diverse testing ground for audio enhancement algorithms.

## Project Goals
- Develop robust audio enhancement techniques for various types of degradation
- Test enhancement methods across different environmental sounds and noise conditions
- Provide metrics-based evaluation of audio quality improvement
- Create a pipeline for processing and restoring degraded audio files

## Features
- Support for multiple types of audio degradation:
  - Environmental noise
  - Old recording artifacts
  - Low-quality compression artifacts
  - Background noise
  - Reverberation
- Quality metrics evaluation:
  - PESQ (Perceptual Evaluation of Speech Quality)
  - STOI (Short-Time Objective Intelligibility)
  - SNR (Signal-to-Noise Ratio)
- Batch processing capabilities
- Support for various audio formats

## Dataset
The project uses the ESC-50 dataset which provides:
- 2000 environmental recordings (5 seconds each)
- 50 classes of sounds
- High-quality source material for testing enhancement algorithms
- Diverse sound types including:
  - Natural sounds
  - Human non-speech sounds
  - Domestic sounds
  - Urban noises

## Installation
```bash
# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Usage
1. Prepare the dataset:
```python
python prepare_dataset.py
```

2. Process audio files:
```python
python enhance_audio.py --input_dir "path/to/input" --output_dir "path/to/output"
```

3. Evaluate results:
```python
python evaluate_results.py --enhanced "path/to/enhanced" --original "path/to/original"
```

## Quality Metrics
- PESQ: Target > 3.0 (Higher is better)
- STOI: Target > 0.9 (Higher is better)
- SNR: Target > 20dB (Higher is better)

## Project Structure
```
GaussBuster/
├── data/
│   ├── ESC-50-master/      # Original dataset
│   └── ESC-50-processed/   # Processed files
├── notebooks/
│   └── prepare_voxceleb_dataset.ipynb
├── src/
│   ├── enhancement/        # Enhancement algorithms
│   ├── evaluation/         # Metrics calculation
│   └── utils/             # Helper functions
├── requirements.txt
└── README.md
```

## Future Work
- Implement additional enhancement algorithms
- Add real-time processing capabilities
- Develop a web interface for audio enhancement
- Support for longer audio files
- Integration with other datasets

## Acknowledgments
- ESC-50 dataset creators
- PESQ and STOI implementation authors
- The audio processing community

## Contact
- Project Link: [https://github.com/LeaMyl/GaussBuster](https://github.com/LeaMyl/GaussBuster)