---VERTEX SHADER-------------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

uniform mat4 modelview_matrix;
uniform mat4 projection_matrix;

in vec3 in_position;
in vec3 in_normal;
in vec2 in_texture;

varying out vec2 v_tex;

void main(void)
{
    v_tex = in_texture;
	gl_Position = projection_matrix * modelview_matrix * vec4(in_position, 1);
}

---FRAGMENT SHADER-----------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

in vec2 v_tex;

uniform sampler2D texture0;

void main() {
	gl_FragColor = texture2D(texture0, v_tex);
	gl_FragColor.a = 1.0;
}