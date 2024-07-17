# NV12 Padding Removal Script

This script removes padded stride pixels from an NV12 YUV image.

## Description

NV12 is a YUV format commonly used in video processing. Sometimes, images in this format have padded stride pixels which need to be removed to get the original resolution. This script reads an NV12 image, removes the padded pixels, and writes the data back in the desired resolution.

## Usage

### Command Line Arguments

The script requires the following command line arguments:

1. `orig_width`: The original width of the image.
2. `orig_height`: The original height of the image.
3. `stride_width`: The stride width of the image.
4. `stride_height`: The stride height of the image.
5. `input_file`: The path to the input NV12 file.

### Example

```sh
python remove_padding_nv12.py 1920 1080 2048 1088 input_nv12.yuv
```
This command will process the input_nv12.yuv file, remove the padding, and save the output to out_input_nv12.yuv.

### Installation
Ensure you have Python installed (version 3.6 or later).
Install required packages, if not already available. This script uses numpy, which can be installed via:

```sh
pip install numpy
```