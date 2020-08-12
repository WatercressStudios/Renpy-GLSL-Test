# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    scene black

    menu:
        "Choose a shader demo scene."

        "Whirl":
            jump whirl_test

        "Blur":
            jump blur_test

        "Multiply":
            jump multiply_test

        "Multiple shader test":
            jump multiple_shader_test

        "Cancel":
            # This ends the game.
            return

label whirl_test:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    e "Hello! I'm going to be shown with the whirl transition!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy
    with whirl

    e "ahhhh time and space is bending!"

    # Return to the shader selection scene.

    jump start

label blur_test:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    show eileen happy:
        xalign 0.5
    e "Hello! I'm going to be blurred in and out!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at blur(2.0, 100.0)
    pause 2.0
    show eileen at blur(2.0, 0.0)

    e "ahhhh time and space is bending!"

    # Return to the shader selection scene.

    jump start

label multiply_test:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    show eileen happy:
        xalign 0.5
    e "Hello! I'm going to be coloured in and out!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at multiply(0.0, color("#fff"))
    show eileen at multiply(1.0, color("#17f"))
    pause 1.0
    show eileen at multiply(1.0, color("#fff"))

    e "ahhhh time and space is bending!"

    # Return to the shader selection scene.

    jump start

label multiple_shader_test:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # These display lines of dialogue.

    show eileen happy at blur(0.0, 0.0), multiply(0.0, color("#ffff")):
        xalign 0.5
    e "Hello! I'm going to be coloured in and out!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen at multiply(1.0, color("#7cf1")), blur(2.0, 100)
    pause 2
    show eileen at multiply(1.0, color("#fff")),  blur(2.0, 0)

    e "ahhhh time and space is bending!"

    # Return to the shader selection scene.

    jump start
