import json
import matplotlib.pyplot as plt
import numpy as np
import os
from settings_lidar import retrieve_settings
from get_data import get_data
import pathlib

settings = retrieve_settings()
file_to_read = settings.file_to_visualize
file_name_to_save=file_to_read.split('/')[-1].split('.')[0]
outputDirectory = settings.folder_to_save_plots + '/xy/'

def visualize(angles,distances,b):
    adjustment=settings.ADJUSTMENT_DEGREES

    angles=np.radians([d+adjustment if d <=360-adjustment else d-(360-adjustment) for d in angles])
    y=np.cos(angles) * distances
    x=np.sin(angles) * distances

    plt.scatter(x,y)
    limit_min=-800
    limit_max=800
    plt.xlim(limit_min,limit_max)
    plt.ylim(limit_min,limit_max)
    #offsets = np.array((angles, distances)).transpose()
    #line.set_offsets(offsets)
    pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True)
    plt.savefig(outputDirectory + file_name_to_save + '-' + str(b)+'.png')
    plt.clf()

def init():
    data= get_data(file_to_read)
    beta = np.linspace(int(list(data.keys())[0]),int(list(data.keys())[len(data)-1]),len(data))
    beta=list(beta)
    range_list_info=[]
    return data,beta,range_list_info

def run():
    data,beta, range_list_info = init()
    pathlib.Path(outputDirectory).mkdir(parents=True, exist_ok=True)
    for b in beta:
        scan = data[str(b).split('.')[0]]
        distances = []
        angles = []
        for angle, distance, quality, timestamp in scan:
            angles.append(float(angle))
            distances.append(float(distance))
        visualize(angles,distances,b)

# def adjust_json():
#     data, beta, range_list_info, line, fig = init()
#     new_data={}
#     #os.mkdir(settings.folder_to_save_plots + file_name_to_save)
#     for b in beta:
#         scan = data[str(b).split('.')[0]]
#         new_scan = []
#         for angle, distance, quality in scan:
#             if float(angle) >= 180:
#                 new_angle=(float(angle) - 180)
#             else:
#                 new_angle=(360 - (abs(float(angle) - 180)))
#             new_scan.append([new_angle,distance,quality])
#         new_data[str(b).split('.')[0]] = new_scan
#     with open(settings.file_to_visualize + 'new_json.json', 'w') as outfile:
#         json.dump(new_data, outfile)

def clean_directory(directoryName):
    folder = directoryName
    if os.path.isdir(directoryName):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

if __name__ == "__main__":
    clean_directory(outputDirectory)
    run()
