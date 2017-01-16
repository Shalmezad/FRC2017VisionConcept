import pygame
import math

DARK_BLUE = (10, 10, 35)
BLACK = (0, 0, 0)
YELLOW = (255,255,0)
GREEN = (0,255,0)
LIGHT_GRAY = (175,175,175)
PIXELS_PER_INCH = 6
camera_size = (640, 480)
screen_size = (camera_size[0] * 2, camera_size[1] * 2)
top_down_view = [0, 0, camera_size[0], camera_size[1] * 2]
camera_view = [camera_size[0], 0, camera_size[0], camera_size[1]]
debugger_view = [camera_size[0], camera_size[1], camera_size[0], camera_size[1]]

camera_position_inches = (0, 20)
camera_angle_degrees = 0 # We'll defined 0 as facing target dead on.
camera_height_inches = 10
# https://www.chiefdelphi.com/forums/showthread.php?t=144285
CAMERA_VIEW_ANGLE_WIDTH_DEGREES = 60
CAMERA_VIEW_ANGLE_WIDTH_RADIANS = math.radians(CAMERA_VIEW_ANGLE_WIDTH_DEGREES)
CAMERA_VIEW_ANGLE_HALF_WIDTH_RADIANS = CAMERA_VIEW_ANGLE_WIDTH_RADIANS/2
CAMERA_VIEW_ANGLE_HEIGHT_DEGREES = 34


# region FIELD CONSTANTS
# Page 20 of the arena manual,
# The width of the airship base (from flat side to flat side) is
# 5', 10.5"
# So:
AIRSHIP_DEPTH_INCHES = 5*12 + 10.5
AIRSHIP_HALF_DEPTH_INCHES = AIRSHIP_DEPTH_INCHES / 2
AIRSHIP_HALF_DEPTH_PIXELS = AIRSHIP_HALF_DEPTH_INCHES * PIXELS_PER_INCH

# We also need the width.
# It's a hexagon
# So with a little bit of math
# http://www.had2know.com/academics/hexagon-measurement-calculator.html
# "d" (width) = 2 "h" (depth) / Math.sqrt(3)
AIRSHIP_WIDTH_INCHES = AIRSHIP_DEPTH_INCHES * 2 / math.sqrt(3)
AIRSHIP_WIDTH_PIXELS = AIRSHIP_WIDTH_INCHES * PIXELS_PER_INCH
AIRSHIP_HALF_WIDTH_PIXELS = AIRSHIP_WIDTH_PIXELS/2
AIRSHIP_QUARTER_WIDTH_PIXELS = AIRSHIP_WIDTH_PIXELS/4

# Peg length, pg 24 of the arena manual
# Is 10.5" long:
PEG_LENGTH_INCHES = 10.5
PEG_LENGTH_PIXELS = PEG_LENGTH_INCHES * PIXELS_PER_INCH
# Had to find the field drawings for this:
PEG_WIDTH_INCHES = 0.87
PEG_WIDTH_PIXELS = PEG_WIDTH_INCHES * PIXELS_PER_INCH

# Page 37 of game manual:
VISION_FULL_WIDTH_INCHES = 10.25
SINGLE_STRIPE_WIDTH_INCHES = 2
VISION_FULL_WIDTH_PIXELS = VISION_FULL_WIDTH_INCHES * PIXELS_PER_INCH
SINGLE_STRIPE_WIDTH_PIXELS = SINGLE_STRIPE_WIDTH_INCHES * PIXELS_PER_INCH
# Bottom is 10.75 off ground:
SINGLE_STRIPE_BOTTOM_INCHES = 10.75
# And goes up 5 inches:
SINGLE_STRIPE_TOP_INCHES = 5
# endregion

def drawTopDownBase(screen, zero_x, zero_y):
    # Left side:
    left_left_x = zero_x - AIRSHIP_HALF_WIDTH_PIXELS
    left_left_y = zero_y - AIRSHIP_HALF_DEPTH_PIXELS
    left_left = [left_left_x, left_left_y]
    left_right_x = zero_x - AIRSHIP_QUARTER_WIDTH_PIXELS
    left_right_y = zero_y
    left_right = [left_right_x, left_right_y]
    pygame.draw.line(screen, YELLOW, left_left, left_right,5)
    # Center:
    center_left_x = zero_x - AIRSHIP_QUARTER_WIDTH_PIXELS
    center_left_y = zero_y
    center_left = [center_left_x, center_left_y]
    center_right_x = zero_x + AIRSHIP_QUARTER_WIDTH_PIXELS
    center_right_y = zero_y
    center_right = [center_right_x, center_right_y]
    pygame.draw.line(screen, YELLOW, center_left, center_right,5)
    # Right:
    right_left_x = zero_x + AIRSHIP_QUARTER_WIDTH_PIXELS
    right_left_y = zero_y
    right_left = [right_left_x, right_left_y]
    right_right_x = zero_x + AIRSHIP_HALF_WIDTH_PIXELS
    right_right_y = zero_y - AIRSHIP_HALF_DEPTH_PIXELS
    right_right = [right_right_x, right_right_y]
    pygame.draw.line(screen, YELLOW, right_left, right_right,5)
    # Draw our 2 vision targets
    vision_left_left_x = zero_x - VISION_FULL_WIDTH_PIXELS/2
    vision_left_left_y = zero_y
    vision_left_left = [vision_left_left_x, vision_left_left_y]
    vision_left_right_x = vision_left_left_x + SINGLE_STRIPE_WIDTH_PIXELS
    vision_left_right_y = zero_y
    vision_left_right = [vision_left_right_x, vision_left_right_y]
    pygame.draw.line(screen, GREEN, vision_left_left, vision_left_right,5)
    vision_right_right_x = zero_x + VISION_FULL_WIDTH_PIXELS/2
    vision_right_right_y = zero_y
    vision_right_right = [vision_right_right_x, vision_right_right_y]
    vision_right_left_x = vision_right_right_x - SINGLE_STRIPE_WIDTH_PIXELS
    vision_right_left_y = zero_y
    vision_right_left = [vision_right_left_x, vision_right_left_y]
    pygame.draw.line(screen, GREEN, vision_right_right, vision_right_left,5)
    # Draw the peg
    peg_top_x = zero_x
    peg_top_y = zero_y
    peg_top = [peg_top_x, peg_top_y]
    peg_bottom_x = zero_x
    peg_bottom_y = peg_top_y + PEG_LENGTH_PIXELS
    peg_bottom = [peg_bottom_x, peg_bottom_y]
    pygame.draw.line(screen, YELLOW, peg_top, peg_bottom,int(PEG_WIDTH_PIXELS))

def drawTopDown(screen):
    screen.set_clip(top_down_view)
    pygame.draw.rect(screen, DARK_BLUE, top_down_view)
    # We're going to define 0, 0 as being the BASE of the peg (right against the lifter)
    # The center of our view is 0 x:
    center_x = top_down_view[0] + (top_down_view[2]/2)
    zero_x = center_x
    # Now, as for zero y,
    # It's our y + half-depth:
    zero_y = top_down_view[1] + AIRSHIP_HALF_DEPTH_PIXELS
    # Now, let's draw our base:
    drawTopDownBase(screen, zero_x, zero_y)
    # Draw our camera:
    camera_position_pixels = (camera_position_inches[0] * PIXELS_PER_INCH, camera_position_inches[1] * PIXELS_PER_INCH)
    camera_position_view = (int(camera_position_pixels[0] + zero_x), int(camera_position_pixels[1] + zero_y))
    pygame.draw.circle(screen, LIGHT_GRAY, camera_position_view,4)
    # and the camera view:
    radians_center = math.radians(camera_angle_degrees-90)
    radians_left = radians_center+CAMERA_VIEW_ANGLE_HALF_WIDTH_RADIANS
    radians_right = radians_center-CAMERA_VIEW_ANGLE_HALF_WIDTH_RADIANS
    # We have a hypotenuse, and an angle:
    camera_radius = 240
    left_x_delta = math.cos(radians_left)
    left_y_delta = math.sin(radians_left)
    right_x_delta = math.cos(radians_right)
    right_y_delta = math.sin(radians_right)
    camera_left = (int(camera_position_view[0] + camera_radius*left_x_delta),
                   int(camera_position_view[1] + camera_radius*left_y_delta))
    camera_right = (int(camera_position_view[0] + camera_radius*right_x_delta),
                    int(camera_position_view[1] + camera_radius*right_y_delta))
    pygame.draw.line(screen, LIGHT_GRAY, camera_position_view, camera_left,2)
    pygame.draw.line(screen, LIGHT_GRAY, camera_position_view, camera_right,2)

# http://stackoverflow.com/a/39005543/978509
# Man I hope their math is right...
# z is up down (+z = up)
# x is left/right of the peg
# y is in/out of the peg ( +y = out of peg)
def get2dPoint(x,y,z, screen_width, screen_height, fov_width_degrees, fov_height_degrees):
    #x_prime = ( x * ( screen_width / 2 ) / math.tan( fov / 2 ) ) / ( z + ( ( screen_width / 2 ) / math.tan( fov / 2 ) ) )
    #y_prime = ( y * ( screen_height / 2 ) / math.tan( fov / 2 ) ) / ( z + ( ( screen_height / 2 ) / math.tan( fov / 2 ) ) )
    #return (x_prime, y_prime)
    # Math shouldn't be that bad, we should be able to handle this
    delta_x = x-camera_position_inches[0]
    delta_y = y-camera_position_inches[1]
    delta_z = z-camera_height_inches
    # So, we have our camera position/angle
    # What we need is to figure out the angle between the point, and our camera center
    # So, find the angle to the camera:
    angle_x = math.degrees(math.atan2(delta_y, delta_x))+90
    # Adjust based on camera angle:
    angle_x -= camera_angle_degrees
    # And based on our fov...
    x = screen_width * (angle_x/fov_width_degrees)

    # Find the angle to our camera:
    # In order to do this, we need the distance to the point from a top down perspective:
    distance = math.sqrt(math.pow(delta_y,2) + math.pow(delta_x,2))
    angle_y = math.degrees(math.atan2(z-camera_height_inches,distance))
    #print "Distance = " + str(distance)
    #print "Angle y = " + str(angle_y)
    y = screen_height * (angle_y / fov_height_degrees)

    #y = 0
    return (x,y)

def drawPoint(screen,point, view):
    # So, the points are such that 0,0 is center...
    center_x = view[0] + view[2]/2
    center_y = view[1] + view[3]/2
    point2 = (int(center_x + point[0]), int(center_y + point[1]))
    pygame.draw.circle(screen, LIGHT_GRAY, point2,4)


def drawCamera(screen):
    screen.set_clip(camera_view)
    pygame.draw.rect(screen, BLACK, camera_view)
    # Figure out where our rects are in 3d space:
    # LEFT
    left_target_top_left_x = -1 * VISION_FULL_WIDTH_INCHES/2
    left_target_top_left_y = 0
    left_target_top_left_z = SINGLE_STRIPE_TOP_INCHES
    left_target_top_left = (left_target_top_left_x, left_target_top_left_y,left_target_top_left_z)
    left_target_top_right_x = left_target_top_left_x + SINGLE_STRIPE_WIDTH_INCHES
    left_target_top_right_y = 0
    left_target_top_right_z = left_target_top_left_z
    left_target_top_right = (left_target_top_right_x,left_target_top_right_y,left_target_top_right_z)
    left_target_bottom_left_x = left_target_top_left_x
    left_target_bottom_left_y = 0
    left_target_bottom_left_z = SINGLE_STRIPE_BOTTOM_INCHES
    left_target_bottom_left = (left_target_bottom_left_x,left_target_bottom_left_y,left_target_bottom_left_z)
    left_target_bottom_right_x = left_target_top_right_x
    left_target_bottom_right_y = 0
    left_target_bottom_right_z = left_target_bottom_left_z
    left_target_bottom_right = (left_target_bottom_right_x, left_target_bottom_right_y, left_target_bottom_right_z)

    # RIGHT
    right_target_top_right_x = VISION_FULL_WIDTH_INCHES/2
    right_target_top_right_y = 0
    right_target_top_right_z = SINGLE_STRIPE_TOP_INCHES
    right_target_top_right = (right_target_top_right_x,right_target_top_right_y,right_target_top_right_z)
    right_target_top_left_x = right_target_top_right_x - SINGLE_STRIPE_WIDTH_INCHES
    right_target_top_left_y = 0
    right_target_top_left_z = right_target_top_right_z
    right_target_top_left = (right_target_top_left_x,right_target_top_left_y,right_target_top_left_z)
    right_target_bottom_right_x = right_target_top_right_x
    right_target_bottom_right_y = 0
    right_target_bottom_right_z = SINGLE_STRIPE_BOTTOM_INCHES
    right_target_bottom_right = (right_target_bottom_right_x, right_target_bottom_right_y, right_target_bottom_right_z)
    right_target_bottom_left_x = right_target_top_left_x
    right_target_bottom_left_y = 0
    right_target_bottom_left_z = right_target_bottom_right_z
    right_target_bottom_left = (right_target_bottom_left_x,right_target_bottom_left_y,right_target_bottom_left_z)

    points = [left_target_top_left, left_target_top_right, left_target_bottom_left, left_target_bottom_right,
              right_target_top_left, right_target_top_right,right_target_bottom_left, right_target_bottom_right]
    # Get their 2d points:
    for point in points:
        new_point = get2dPoint(point[0],point[1],point[2], camera_size[0], camera_size[1], CAMERA_VIEW_ANGLE_WIDTH_DEGREES, CAMERA_VIEW_ANGLE_HEIGHT_DEGREES)
        drawPoint(screen, new_point, camera_view)


def drawDebugger(screen, font):
    screen.set_clip(debugger_view)
    x = debugger_view[0] + 4
    y = debugger_view[1] + 4
    text = font.render("Debugger", True, (0, 128, 0))
    screen.blit(text, (x, y))
    y += text.get_height() + 2
    camera_position_text = "Position: ("
    camera_position_text += str(round(camera_position_inches[0],2))
    camera_position_text += ","
    camera_position_text += str(round(camera_position_inches[1],2))
    camera_position_text += ")"
    text = font.render(camera_position_text, True, (0,128,0))
    screen.blit(text, (x, y))
    y += text.get_height() + 2
    camera_angle_text = "Angle: "
    camera_angle_text += str(round(camera_angle_degrees,2))
    camera_angle_text += " degrees"
    text = font.render(camera_angle_text, True, (0,128,0))
    screen.blit(text, (x, y))



def main():
    pygame.init()

    font = pygame.font.SysFont("comicsansms", 12)

    screen = pygame.display.set_mode(screen_size)

    done = False
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Handle input:
        keys=pygame.key.get_pressed()
        global camera_angle_degrees
        global camera_position_inches
        turn_speed_degrees = 0.6
        move_speed_inches = 0.3
        if keys[pygame.K_LEFT]:
            camera_angle_degrees -= turn_speed_degrees
        if keys[pygame.K_RIGHT]:
            camera_angle_degrees += turn_speed_degrees
        if keys[pygame.K_DOWN]:
            camera_angle_radians = math.radians(camera_angle_degrees + 90)
            x_delta = math.cos(camera_angle_radians)
            y_delta = math.sin(camera_angle_radians)
            new_x = camera_position_inches[0] + move_speed_inches * x_delta
            new_y = camera_position_inches[1] + move_speed_inches * y_delta
            camera_position_inches = (new_x, new_y)
        if keys[pygame.K_UP]:
            camera_angle_radians = math.radians(camera_angle_degrees + 90)
            x_delta = math.cos(camera_angle_radians)
            y_delta = math.sin(camera_angle_radians)
            new_x = camera_position_inches[0] + move_speed_inches * x_delta * -1
            new_y = camera_position_inches[1] + move_speed_inches * y_delta * -1
            camera_position_inches = (new_x, new_y)

        screen.fill((255, 255, 255))
        # Drawing code here:
        # Draw our top down view:
        drawTopDown(screen)
        # Draw our camera picture
        drawCamera(screen)
        # Draw debug information
        drawDebugger(screen, font)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()