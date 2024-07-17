import os
import numpy as np
import glob
import argparse

def read_nv12_image(file_path, width, height):
    with open(file_path, 'rb') as f:
        y_plane = np.frombuffer(f.read(width * height), dtype=np.uint8).reshape((height, width))
        uv_plane = np.frombuffer(f.read(width * height // 2), dtype=np.uint8).reshape((height // 2, width))
        u_plane = uv_plane[:, 0::2]
        v_plane = uv_plane[:, 1::2]
    return y_plane, u_plane, v_plane

def write_nv12_image(file_path, y_plane, u_plane, v_plane):
    height, width = y_plane.shape
    uv_plane = np.zeros((height // 2, width), dtype=np.uint8)
    uv_plane[:, 0::2] = u_plane
    uv_plane[:, 1::2] = v_plane
    with open(file_path, 'wb') as f:
        f.write(y_plane.tobytes())
        f.write(uv_plane.tobytes())

def average_images(image_paths, width, height):
    avg_y = np.zeros((height, width), dtype=np.float32)
    avg_u = np.zeros((height // 2, width // 2), dtype=np.float32)
    avg_v = np.zeros((height // 2, width // 2), dtype=np.float32)
    
    for image_path in image_paths:
        y, u, v = read_nv12_image(image_path, width, height)
        avg_y += y
        avg_u += u
        avg_v += v

    avg_y /= len(image_paths)
    avg_u /= len(image_paths)
    avg_v /= len(image_paths)

    avg_y = avg_y.astype(np.uint8)
    avg_u = avg_u.astype(np.uint8)
    avg_v = avg_v.astype(np.uint8)

    return avg_y, avg_u, avg_v

def main():
    parser = argparse.ArgumentParser(description='Average YUV images in a folder.')
    parser.add_argument('input_folder', type=str, help='Input folder containing .yuv files')
    parser.add_argument('width', type=int, help='Width of the images')
    parser.add_argument('height', type=int, help='Height of the images')

    args = parser.parse_args()

    if not os.path.exists(args.input_folder):
        print(f"Folder {args.input_folder} does not exist. Please try again.")
        return

    image_paths = glob.glob(os.path.join(args.input_folder, '*.yuv'))
    if not image_paths:
        print(f"No .yuv files found in folder {args.input_folder}. Please try again.")
        return

    avg_y, avg_u, avg_v = average_images(image_paths, args.width, args.height)
    output_path = os.path.join(args.input_folder, 'avg_out.yuv')
    write_nv12_image(output_path, avg_y, avg_u, avg_v)

if __name__ == '__main__':
    main()
