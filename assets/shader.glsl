---VERTEX SHADER-------------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

attribute vec3 v_position;
attribute vec3 v_normal;
attribute vec2 v_texture;

uniform mat4 modelview_matrix;
uniform mat4 projection_matrix;

varying vec2 v_tex;

void main()
{
    v_tex = v_texture;
	gl_Position = projection_matrix * modelview_matrix * vec4(v_position, 1);
}

---FRAGMENT SHADER-----------------------------------------------------
#ifdef GL_ES
    precision highp float;
#endif

varying vec2 v_tex;

uniform sampler2D texture0;

void main() {
	gl_FragColor = texture2D(texture0, v_tex);
}