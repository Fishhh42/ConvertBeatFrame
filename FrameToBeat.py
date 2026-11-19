stage = 0
def stage_value_handler(prompt):
    global stage
    try:
        value = float(input(prompt))
        if value > 0:
            stage += 1
            return value
        else:
            stage -= 1
            return -1
    except ValueError:
        print("Incorrect variable type, please try again")
while stage >= 0:
    if stage == 0:
        fps = stage_value_handler("Frames per second: ")
    elif stage == 1:
        bpm = stage_value_handler("BPM: ")
    elif stage == 2:
        frame = stage_value_handler("Frame: ")
    elif stage == 3:
        print("FPS: "+str(fps)+"  ||  Frame: "+str(frame)+"  ||  Beat: "+str((frame*bpm)/(60*fps)))
        stage = 2