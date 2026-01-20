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
