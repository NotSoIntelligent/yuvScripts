import sys
import numpy as np
import os

def remove_padding_nv12(orig_width, orig_height, stride_width, stride_height, input_file):
    # Read the NV12 image data from file
    with open(input_file, 'rb') as f:
        nv12_data = f.read()
    
    # Calculate the sizes of Y and UV planes
    y_plane_size = stride_width * stride_height
    uv_plane_size = stride_width * stride_height // 2

    # Extract the Y and UV planes
    y_plane = nv12_data[:y_plane_size]
    uv_plane = nv12_data[y_plane_size:y_plane_size + uv_plane_size]

    # Reshape Y plane to remove padding
    y_plane_reshaped = np.frombuffer(y_plane, dtype=np.uint8).reshape((stride_height, stride_width))
    y_plane_orig = y_plane_reshaped[:orig_height, :orig_width]

    # Reshape UV plane to remove padding
    uv_plane_reshaped = np.frombuffer(uv_plane, dtype=np.uint8).reshape((stride_height // 2, stride_width))
    uv_plane_orig = uv_plane_reshaped[:orig_height // 2, :orig_width]

    # Flatten the original Y and UV planes
    y_plane_orig_flat = y_plane_orig.flatten()
    uv_plane_orig_flat = uv_plane_orig.flatten()

    # Construct the output file name
    input_file_name = os.path.basename(input_file)
    output_file = f'out_{input_file_name}'

    # Write the processed data to the output file
    with open(output_file, 'wb') as f:
        f.write(y_plane_orig_flat.tobytes())
        f.write(uv_plane_orig_flat.tobytes())
    
    print(f'Successfully wrote the output to {output_file}')

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print(f'Usage: {sys.argv[0]} <orig_width> <orig_height> <stride_width> <stride_height> <input_file>')
        sys.exit(1)

    orig_width = int(sys.argv[1])
    orig_height = int(sys.argv[2])
    stride_width = int(sys.argv[3])
    stride_height = int(sys.argv[4])
    input_file = sys.argv[5]

    remove_padding_nv12(orig_width, orig_height, stride_width, stride_height, input_file)
