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
        beat = stage_value_handler("Beat: ")
    elif stage == 3:
        print("FPS: "+str(fps)+"  ||  Beat: "+str(beat)+"  ||  Frame: "+str((1/bpm)*beat*60*fps))
        stage = 2