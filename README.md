# Digital Image Processing Laboratory

A hands-on implementation of classical Digital Image Processing (DIP) algorithms from first principles using Python and NumPy.

This project is **not** intended to be another wrapper around OpenCV.

The goal is to understand **how image processing algorithms work internally** by implementing them step by step while using OpenCV only for image loading, saving, and visualization.

---

## Objectives

This project aims to answer questions such as:

- What is a digital image?
- What is a pixel?
- What is intensity?
- What is a kernel?
- What is convolution?
- How does blurring actually work?
- Why does Gaussian blur preserve edges better?
- How does sharpening work?
- How do edge detectors work?
- How are histograms computed?
- How do Fourier transforms relate to images?

Instead of treating these algorithms as black boxes, every major algorithm is implemented from scratch.

---

## Learning Philosophy

The implementation follows a progressive learning approach.

```
Image
      ↓
Pixels
      ↓
Neighborhoods
      ↓
Kernels
      ↓
Convolution
      ↓
Filtering
      ↓
Edge Detection
      ↓
Morphology
      ↓
Frequency Domain
```

Every new topic builds on the previous one.

---

## Technologies

- Python
- NumPy
- OpenCV (Image I/O and Display)
- Matplotlib (Histograms & Visualization)

---

## Project Structure

```
image_lab/

│
├── main.py
│
├── core/
│   ├── image_loader.py
│   ├── image_display.py
│   ├── image_info.py
│   └── image_saver.py
│
├── algorithms/
│   ├── convolution.py
│   │
│   ├── blur/
│   │   ├── average.py
│   │   ├── gaussian.py
│   │   └── median.py
│   │
│   ├── sharpen/
│   ├── threshold/
│   ├── histogram/
│   ├── morphology/
│   ├── edge_detection/
│   └── frequency/
│
├── kernels/
│   ├── average.py
│   ├── gaussian.py
│   ├── sobel.py
│   ├── laplacian.py
│   └── sharpen.py
│
├── images/
│   ├── original/
│   └── output/
│
└── README.md
```

---

## Development Roadmap

### Phase 1 — Image Fundamentals

- [ ] Image Loading
- [ ] Image Information
- [ ] Pixel Inspection
- [ ] Color Spaces

---

### Phase 2 — Convolution

- [ ] Neighborhoods
- [ ] Kernels
- [ ] Manual Convolution
- [ ] Generic Convolution Engine

---

### Phase 3 — Smoothing

- [ ] Average Blur
- [ ] Gaussian Blur
- [ ] Median Blur

---

### Phase 4 — Sharpening

- [ ] Laplacian Sharpening
- [ ] Unsharp Masking
- [ ] High Boost Filtering

---

### Phase 5 — Edge Detection

- [ ] Roberts
- [ ] Prewitt
- [ ] Sobel
- [ ] Laplacian
- [ ] Canny

---

### Phase 6 — Histograms

- [ ] Histogram Computation
- [ ] Histogram Equalization
- [ ] CLAHE

---

### Phase 7 — Morphology

- [ ] Dilation
- [ ] Erosion
- [ ] Opening
- [ ] Closing
- [ ] Skeletonization

---

### Phase 8 — Frequency Domain

- [ ] Fourier Transform
- [ ] Low Pass Filters
- [ ] High Pass Filters
- [ ] Band Pass Filters

---

## Design Principles

Each module has a single responsibility.

### Core

Responsible for:

- Loading images
- Displaying images
- Saving images
- Printing image information

### Algorithms

Responsible for implementing image processing algorithms only.

### Kernels

Responsible for storing and generating convolution kernels.

---

## Why implement algorithms manually?

Although OpenCV already provides highly optimized implementations, implementing the algorithms manually provides a deeper understanding of:

- Digital Images
- Pixel Operations
- Linear Filtering
- Convolution
- Signal Processing
- Computer Vision

After implementing an algorithm manually, the result is compared with OpenCV's implementation for validation.

---

## Example Workflow

```
Load Image
      ↓
Inspect Image
      ↓
Choose Algorithm
      ↓
Generate Kernel
      ↓
Apply Convolution
      ↓
Display Result
      ↓
Compare with OpenCV
```

---

## References

- Rafael C. Gonzalez & Richard E. Woods
  *Digital Image Processing*

- OpenCV Documentation

- NumPy Documentation

---

## Future Goals

- GPU Acceleration
- DICOM Support
- Interactive Visualization
- Medical Image Processing
- Napari Integration
