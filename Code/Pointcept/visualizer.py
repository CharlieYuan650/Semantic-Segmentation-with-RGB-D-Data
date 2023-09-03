import open3d as o3d
import numpy as np
import sys

# Check if a file path argument is provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py <path_to_ply_file>")
    sys.exit()

# Provide the file path to the PLY file you want to read
# file_path = "/home/yukun/Documents/Dissertation/ScanNet/output_folder/scans/scene0000_00/scene0000_00_vh_clean_2.labels.ply"
# file_path = "/home/yukun/Documents/Dissertation/ScanNet/output_folder/scans/scene9998_88/scene9998_88_vh_clean_2.ply"

# Get the file path from the command line argument
file_path = sys.argv[1]

# Load the point cloud data from the .ply file
pcd = o3d.io.read_point_cloud(file_path)
print(pcd)

# Convert the colors to a NumPy array
colors_np = np.asarray(pcd.colors)

# Print out all the labels
print(colors_np)

# Visualize the point cloud with colored labels
o3d.visualization.draw_geometries([pcd],
                                  zoom=0.7,
                                  front=[0, 0, 1],
                                  lookat=[4, 4, 1],
                                  up=[0, 1, 0])