import json
import matplotlib.pyplot as plt
import numpy as np
import os
from settings_lidar import retrieve_settings
import shutil

settings = retrieve_settings()
file_to_read = settings.file_to_visualize
file_name_to_save=file_to_read.split('/')[-1].split('.')[0]

def visualize(angles,distances,line,b):
    offsets = np.array((angles, distances)).transpose()
    line.set_offsets(offsets)
    plt.savefig(settings.folder_to_save_plots + '/' + file_name_to_save + '-' + str(b)+'.png')

def get_data():
    with open(file_to_read) as json_file:
        data = json.load(json_file)
        keysToDelete=[]
    for key,value in data.items():
        if int(key) < int(0.0*len(data)) or int(key) > int(1*len(data)):
            keysToDelete.append(str(key))
    for key in keysToDelete:
        del data[key]
    return data

def init():
    data= get_data()
    beta = np.linspace(int(list(data.keys())[0]),int(list(data.keys())[len(data)-1]),len(data))
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=10, c=[settings.imin, settings.imax],
                               cmap=plt.cm.Blues_r, lw=0)
    ax.set_rmax(settings.dmax)
    ax.grid(True)
    beta=list(beta)
    range_list_info=[]
    return data,beta,range_list_info,line,fig

def run(adjustment):
    data,beta, range_list_info, line, fig = init()
    #os.mkdir(settings.folder_to_save_plots + '/' + file_name_to_save)
    for b in beta:
        scan = data[str(b).split('.')[0]]
        distances = []
        angles = []
        for angle, distance, quality, timestamp in scan:
            angles.append(np.round(float(angle),2))
            distances.append(float(distance))

        angles=np.radians([d+adjustment if d <=360-adjustment else d-(360-adjustment) for d in angles])
        visualize(angles,distances,line,b)

def adjust_json():
    data, beta, range_list_info, line, fig = init()
    new_data={}
    os.mkdir(settings.folder_to_save_plots + file_name_to_save)
    for b in beta:
        scan = data[str(b).split('.')[0]]
        new_scan = []
        for angle, distance, quality in scan:
            if float(angle) >= 180:
                new_angle=(float(angle) - 180)
            else:
                new_angle=(360 - (abs(float(angle) - 180)))
            new_scan.append([new_angle,distance,quality])
        new_data[str(b).split('.')[0]] = new_scan
    with open(settings.file_to_visualize + 'new_json.json', 'w') as outfile:
        json.dump(new_data, outfile)

def clean_directory(directoryName):
    folder = directoryName
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
    clean_directory(settings.folder_to_save_plots)
    run(85)