init python:
    ## Import the Python math module, so that the number pi is available to us.

    import math

    ## This example is from the Ren'Py Patreon July update.
    ##
    ## Define the fragment shader, using the renpy.register_shader function. This takes the variables that the shader uses as parameters,
    ## and takes shader source code at different priority levels. Ren’Py will figure out which shaders are active and string the different
    ## sections of code together from lowest to highest priority number, to compute a full program.

    renpy.register_shader("whirl_shader", variables="""
        uniform float u_whirl_angle;
    """, fragment_250="""

        // Convert the texture coordinate range from
        // (0 to 1) to (-1 to 1), which makes the math
        // easier.
        vec2 tex_coord = v_tex_coord * 2 - 1;

        // Figure out how far the coordinate is from the center.
        float l = length(tex_coord);

        // Compute the sin (ws) and cosine (wc) of the angle
        // we whirl this pixel by.
        float ws = sin(l * u_whirl_angle);
        float wc = cos(l * u_whirl_angle);

        // Rotate the coordinates.
        tex_coord.xy = vec2(
            tex_coord.x * wc + tex_coord.y * ws,
            tex_coord.x * -ws + tex_coord.y * wc);

        // Convert back to (0 to 1).
        tex_coord = (tex_coord / 2) + 0.5;

        // Look up the coordinate, to find the actual color.
        gl_FragColor = texture2D(tex0, tex_coord);
    """)

    renpy.register_shader("blur_shader", variables="""
        uniform float u_blur_size;
        uniform float u_resolution_x;
        uniform float u_resolution_y;
    """, fragment_250="""
        float Pi = 6.28318530718; // Pi*2

        // GAUSSIAN BLUR SETTINGS {{{
        float Directions = 32.0; // BLUR DIRECTIONS (Default 16.0 - More is better but slower)
        float Quality = 8.0; // BLUR QUALITY (Default 4.0 - More is better but slower)
        // GAUSSIAN BLUR SETTINGS }}}

        vec2 Resolution = vec2(u_resolution_x, u_resolution_y);
        vec2 Radius = u_blur_size/Resolution.xy;

        // Pixel colour
        vec4 Color = texture2D(tex0, v_tex_coord);

        // Blur calculations
        float Count = 1;
        for( float d=0.0; d<Pi; d+=Pi/Directions)
        {
    		for(float i=1.0/Quality; i<=1.0; i+=1.0/Quality)
            {
    			Color += texture2D(tex0, v_tex_coord+vec2(cos(d),sin(d))*Radius*i);
                Count++;
            }
        }

        // Output to screen
        Color /= Count;
        gl_FragColor =  Color;
    """)

    renpy.register_shader("multiply_shader", variables="""
        uniform float u_multiply_r;
        uniform float u_multiply_g;
        uniform float u_multiply_b;
        uniform float u_multiply_a;
    """, fragment_250="""
        vec4 Color = texture2D(tex0, v_tex_coord);
        gl_FragColor = vec4(Color.r * u_multiply_r, Color.g * u_multiply_g, Color.b * u_multiply_b, Color.a * u_multiply_a);
    """)
