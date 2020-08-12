## This example is from the Ren'Py Patreon July update.
##
## Define an ATL transition that uses mesh, shader, and the u_whirl_angle uniform to transition from one image to another.
##
## mesh: Asks the transform to create a model out of the child of the transform, using a grid of equally spaced points as the mesh.
## This can either be a (width, height) tuple, or True for (2, 2), which creates a rectangle out of two triangles.
##
## shader: A shader or tuple of shaders to apply to the mesh. If a shader name begins with -, it’s removed.
##
## Properties beginning with u_ are now special. These are passed to the shader program as uniform variables (or uniforms),
## which is the name used for variables that can be supplied to the program from the outside. These uniform variables can be interpolated just like any other ATL property.

transform whirl(old_widget, new_widget):
    # This takes 4 seconds in total.
    delay 4

    # Start with the old child.
    old_widget

    # Describe the mesh and tell Ren'Py to use the shader
    # register above.
    mesh True
    shader "whirl_shader"

    # Start with a 0 angle.
    u_whirl_angle 0.0

    # Over 2 seconds, rotate by 720 degrees.
    # The shader takes radians, where 2 * pi radians are equal
    # to 360 degrees.
    parallel:
        ease 2.0 u_whirl_angle (4 * math.pi)
        # As we're doing that, and continuing on, spend 2 seconds
        # going back to no whirl.
        ease 2.0 u_whirl_angle 0.0

    parallel:
        pause 1.5
        # Quickly dissolve to the new child.
        new_widget with Dissolve(1.0)

transform blur:
    delay 4
    alpha 1

    mesh True
    shader "blur_shader"

    u_resolution_x 1920
    u_resolution_y 1080
    u_blur_size 0.0

    ease 2.0 u_blur_size 100.0
    ease 2.0 u_blur_size 0.0
