import pyautogui
import time

#Find each tile's position
def find_positions(top_left, bottom_right):
    width = (bottom_right[0] - top_left[0]) // 2
    height = (bottom_right[1] - top_left[1]) // 2

    tile_positions = [
        (top_left[0], top_left[1]),
        (top_left[0] + width, top_left[1]),
        (bottom_right[0], top_left[1]),
        (top_left[0], top_left[1] + height),
        (top_left[0] + width, top_left[1] + height),
        (bottom_right[0], top_left[1] + height),
        (top_left[0], bottom_right[1]),
        (top_left[0] + width, bottom_right[1]),
        (bottom_right[0], bottom_right[1])
    ]
    
    return tile_positions

#Ordered list of tiles that flashed
flash_list = []
last_flash_time = None

#Set based on screen size
top_left = (1136, 327)
bottom_right = (1398, 589)

positions = find_positions(top_left, bottom_right)

try:
    while True:
        for idx, pos in enumerate(positions):
            #Check if color is white
            if pyautogui.pixelMatchesColor(pos[0], pos[1], (255, 255, 255)):
                #Check to see if tile was already added
                if len(flash_list) == 0 or flash_list[-1] != idx:
                    flash_list.append(idx)
                    last_flash_time = time.time()
                    
        #Check if 3 seconds has passed without flashes to see if sequence is over
        if last_flash_time and (time.time() - last_flash_time) >= 3:
            for idx in flash_list:
                pyautogui.click(positions[idx][0], positions[idx][1])

            flash_list.clear()
            last_flash_time = None

        time.sleep(0.15)

except KeyboardInterrupt:
    print("Script terminated by the user.")