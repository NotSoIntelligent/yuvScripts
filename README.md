# YUV Image Averaging Tool

This Python script computes the average of all YUV images in NV12 format from a specified input folder. The resulting averaged image is saved as `avg_out.yuv` in the same input folder.

## Prerequisites

- Python 3.x
- numpy

## Installation

1. Clone this repository or download the script file.
2. Install the required Python packages using pip:
    ```sh
    pip install numpy
    ```

## Usage

Run the script from the command line with the following arguments:

```sh
python nv12_avg.py input_folder_path image_width image_height
```