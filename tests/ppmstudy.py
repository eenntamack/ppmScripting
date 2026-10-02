
# # this example  1. cuts a hole in a square, 2. creates a path, 3. shows a point compared to its origin


# #example 1
# import random
# width, height = 100, 100

# xOffset = 40
# yOffset = 15
# widthscaler = 4

# # Create a black canvas
# canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]

# xPoint , yPoint = 10, 10

# epsilon = 5

# invert = 1
# transX, transY = random.randint(1,50),random.randint(1,50)
# for i in range(width):
#     for j in range(height):
#         if (( i <= xPoint + epsilon ) and (i >= xPoint - epsilon ))and (( j <= yPoint + epsilon ) and (j >= yPoint - epsilon )):
#             if (( i <= xPoint + epsilon - invert ) and (i >= xPoint - epsilon + invert ))and (( j <= yPoint + epsilon - invert ) and (j >= yPoint - epsilon + invert)):
#                 canvas[i][j] = [0,0,0]
#             else:
#                 canvas[i][j] = [255,0,0]

            
#         if i == (xPoint + transX) and j == (yPoint + transY):
#             canvas[i][j] = [0,255,0]

# # Write PPM
# with open("projectile_path.ppm", "w") as f:
#     f.write(f"P3\n{width} {height}\n255\n")

#     for row in canvas:
#         for r, g, b in row:
#             f.write(f"{r} {g} {b} ")
#         f.write("\n")


#example 2

# width, height = 100, 100

# xOffset = 40
# yOffset = 15
# widthscaler = 4

# # Create a black canvas
# canvas = [[[0, 0, 0] for _ in range(width)] for _ in range(height)]

# for i in range(width * 10):
#     x = i / 10

#     curveY = ((x - xOffset) / widthscaler) ** 2 + yOffset

#     px = round(x)
#     py = round(curveY)

#     if 0 <= px < width and 0 <= py < height:
#         canvas[py][px] = [255, 0, 0]

# # Write PPM
# with open("projectile_path.ppm", "w") as f:
#     f.write(f"P3\n{width} {height}\n255\n")

#     for row in canvas:
#         for r, g, b in row:
#             f.write(f"{r} {g} {b} ")
#         f.write("\n")

#example 3 generates multiple images ,a video that displays ray traced sphere
# import math

# # --- 3D Vector Math Helpers ---
# def subtract(v1, v2):
#     return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

# def dot(v1, v2):
#     return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

# def normalize(v):
#     length = math.sqrt(dot(v, v))
#     return [v[0] / length, v[1] / length, v[2] / length] if length > 0 else [0, 0, 0]

# # --- Scene Configuration ---
# sphere_pos = [0, 0, -5]
# sphere_radius = 1.2
# sphere_color = [1.0, 0.2, 0.2]  # Red sphere
# ambient_light = 0.15
# bg_color = "135 206 235 "  # Sky blue background

# width, height = 200, 200  # Smaller size so it renders quickly
# camera_pos = [0, 0, 0]
# total_frames = 30

# # --- Animation Loop ---
# for frame in range(total_frames):
#     # Calculate an orbiting angle for the light based on the current frame
#     angle = (frame / total_frames) * 2.0 * math.pi
    
#     # Light moves in a circle along the X and Z axes
#     light_x = math.cos(angle) * 2.0
#     light_y = 1.0  # Keep light slightly elevated
#     light_z = -5.0 + math.sin(angle) * 2.0  # Orbit around the center of the sphere
    
#     light_pos = normalize([light_x, light_y, light_z])
#     filename = f"ray_frame_{frame:02d}.ppm"
    
#     with open(filename, "w") as f:
#         f.write(f"P3\n{width} {height}\n255\n")
        
#         for y in range(height):
#             for x in range(width):
#                 screen_x = (x / width) * 2.0 - 1.0
#                 screen_y = 1.0 - (y / height) * 2.0
                
#                 ray_dir = normalize([screen_x, screen_y, -1.0])
                
#                 oc = subtract(camera_pos, sphere_pos)
#                 b = 2.0 * dot(ray_dir, oc)
#                 c = dot(oc, oc) - (sphere_radius * sphere_radius)
#                 discriminant = (b * b) - (4.0 * c)
                
#                 if discriminant > 0:
#                     t = (-b - math.sqrt(discriminant)) / 2.0
#                     if t > 0:
#                         # Find surface point and normal vector
#                         hit_point = [camera_pos[0] + ray_dir[0]*t, camera_pos[1] + ray_dir[1]*t, camera_pos[2] + ray_dir[2]*t]
#                         normal = normalize(subtract(hit_point, sphere_pos))
                        
#                         # Recalculate light direction relative to this specific hit point
#                         to_light = normalize(subtract([light_x, light_y, light_z], hit_point))
                        
#                         diffuse = max(0.0, dot(normal, to_light))
#                         brightness = ambient_light + (1.0 - ambient_light) * diffuse
                        
#                         r = int(sphere_color[0] * brightness * 255)
#                         g = int(sphere_color[1] * brightness * 255)
#                         b_ch = int(sphere_color[2] * brightness * 255)
                        
#                         f.write(f"{r} {g} {b_ch} ")
#                     else:
#                         f.write(bg_color)
#                 else:
#                     f.write(bg_color)
#             f.write("\n")



 # if (
            #     targetX - epsilon <= x <= targetX + epsilon
            #     and targetY - epsilon <= y <= targetY + epsilon
            # ):
            #     f.write("255 0 0 ")
            # else:
            #     f.write("0 0 0 ")


#example displaying raytraced sphere

import math

# --- 3D Vector Math Helpers ---
def subtract(v1, v2):
    return [v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]]

def dot(v1, v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def normalize(v):
    length = math.sqrt(dot(v, v))
    return [v[0] / length, v[1] / length, v[2] / length] if length > 0 else [0, 0, 0]

# --- 3D Scene Configurations ---
# Define a sphere: [X, Y, Z, Radius, [R, G, B color ratios]]
sphere_pos = [0, 0, -5]
sphere_radius = 1.2
sphere_color = [1.0, 0.2, 0.2]  # Red sphere

# Light source position and background color
light_pos = normalize([2, 4, 0])
ambient_light = 0.2
bg_color = "135 206 235 "  # Sky blue background string

# --- Rendering Core ---
width, height = 4000, 4000
camera_pos = [0, 0, 0]

with open("raytrace.ppm", "w") as f:
    # Write the PPM Header
    f.write(f"P3\n{width} {height}\n255\n")
    
    # Nested Pixel Loops (Screen Grid)
    for y in range(height):
        for x in range(width):
            
            # 1. Map pixel grid coordinates to 3D space (-1.0 to 1.0)
            screen_x = (x / width) * 2.0 - 1.0
            screen_y = 1.0 - (y / height) * 2.0  # Flip Y so positive is up
            
            # 2. Fire a ray from camera forward into the scene
            ray_dir = normalize([screen_x, screen_y, -1.0])
            
            # 3. Ray-Sphere Intersection Math (Quadratic Equation)
            oc = subtract(camera_pos, sphere_pos)
            b = 2.0 * dot(ray_dir, oc)
            c = dot(oc, oc) - (sphere_radius * sphere_radius)
            discriminant = (b * b) - (4.0 * c)
            
            # 4. Color Assignment based on hit status
            if discriminant > 0:
                # Find the closest intersection point
                t = (-b - math.sqrt(discriminant)) / 2.0
                
                if t > 0:
                    # Calculate exact intersection point and its surface surface normal
                    hit_point = [camera_pos[0] + ray_dir[0]*t, camera_pos[1] + ray_dir[1]*t, camera_pos[2] + ray_dir[2]*t]
                    normal = normalize(subtract(hit_point, sphere_pos))
                    
                    # Calculate Diffuse Shading (Lambertian Reflection)
                    diffuse = max(0.0, dot(normal, light_pos))
                    brightness = ambient_light + (1.0 - ambient_light) * diffuse
                    
                    # Convert to final 0-255 RGB integers
                    r = int(sphere_color[0] * brightness * 255)
                    g = int(sphere_color[1] * brightness * 255)
                    b_ch = int(sphere_color[2] * brightness * 255)
                    
                    f.write(f"{r} {g} {b_ch} ")
                else:
                    f.write(bg_color)
            else:
                # Ray missed the sphere, paint background sky color
                f.write(bg_color)
                
        f.write("\n")





