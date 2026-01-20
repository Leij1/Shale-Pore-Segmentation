# Shale-Pore-Segmentation
Quantitative pore statistics derived from SEM images
 Resolution-Sensitive Shale Pore Segmentation Using FOV FE-SEM Images

This repository provides the open-source implementation used in the manuscript:

**“Resolution Sensitivity of Image-Based Shale Pore Statistics Derived from Multi-Resolution FOV FE-SEM Images Using Deep Learning”**

The code supports deep learning–based semantic segmentation of shale pores and fractures from large-field-of-view (FOV) FE-SEM images and subsequent image-based pore statistics analysis.

---

## Overview

Quantitative pore statistics derived from SEM images are strongly influenced by image resolution (pixel size) and segmentation consistency.  
This repository implements a reproducible workflow that integrates:

- Multi-resolution FOV FE-SEM image datasets  
- Deep learning–based semantic segmentation using PaddleSeg  
- Post-processing and image-based pore statistics extraction  

The workflow is designed to enable **resolution-sensitivity analysis under a constant field of view**, with an emphasis on **consistency, reproducibility, and scalability** rather than geological interpretation.

All analyses are based on **two-dimensional (2D) images**. Three-dimensional pore connectivity is **not inferred**.

---

## Software and Frameworks

- **Deep learning framework:** PaddleSeg (version 2.9)  
  https://github.com/PaddlePaddle/PaddleSeg  
- **Image analysis software:** ImageJ (version 1.54f)  
  https://imagej.nih.gov/ij/

Both PaddleSeg and ImageJ are open-source software.


## Scripts (Brief Description)

- `roi_image_cropper.py`  
  **Purpose:** Crop a fixed ROI from FE-SEM images.  
  **Input:** One image path + ROI coordinates (left, top, right, bottom).  
  **Output:** Cropped image file(s).

- `excel_psd_histogram_plotter.py`  
  **Purpose:** Plot a log-scale distribution histogram from Excel-exported pore/fracture statistics.  
  **Input:** `data.xlsx` (user-defined sheet/range).  
  **Output:** Histogram figure (shown/saved).

- `segmentation_threshold_benchmark.py`  
  **Purpose:** Compare conventional segmentation strategies and compute area fraction (black-pixel ratio).  
  **Input:** A folder of grayscale images.  
  **Output:** Binary masks saved into method-specific folders + a summary `.txt` file.

- `boxcount_fractal_dimension_batch.py`  
  **Purpose:** Batch compute fractal dimension (FD) using the box-counting method from binary masks.  
  **Input:** A folder of images (converted to binary using Otsu in the script).  
  **Output:** `fractal_dimensions.csv`.

> Note: Some scripts contain hard-coded local paths. Please update file paths before running.
