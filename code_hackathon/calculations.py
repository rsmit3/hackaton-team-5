from settings_lidar import retrieve_settings

settings = retrieve_settings()
file_to_read = settings.file_to_visualize

def has_warning(x, y, limit_min, limit_max, threshold):
    coordinates=list(zip(x,y))
    x=[x for x,y in coordinates if y>-50 and (x>1 or x<-1) and limit_min < y < limit_max and limit_max > x and limit_min < x]
    y=[y for x,y in coordinates if y>-50 and (x>1 or x<-1) and limit_min < y < limit_max and limit_max > x and limit_min < x]

    coordinates=list(zip(x,y))
    min_y_left = min([y for x,y in coordinates if x < 0])
    max_y_right = max([y for x,y in coordinates if x > 0])

    return max_y_right - min_y_left > threshold
