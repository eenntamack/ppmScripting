from helpers.material import Material
from helpers.color import Color
from helpers.ray_functions import Ray_OP

class Lighting:
    @staticmethod
    def lighting(m: Material, light, position, eyev, normalv, in_shadow = False):

        effective_color = m.color * light.intensity

        lightv = (light.position - position).normalize()

        ambient = effective_color * m.ambient

        light_dot_normal = lightv.dot(normalv)

        if light_dot_normal < 0:
            diffuse = Color(0, 0, 0)
            specular = Color(0, 0, 0)

        else:
            diffuse = effective_color * m.diffuse * light_dot_normal

            reflectv = Ray_OP.reflect(-lightv, normalv)

            reflect_dot_eye = reflectv.dot(eyev)

            if reflect_dot_eye <= 0:
                specular = Color(0, 0, 0)
            else:
                factor = pow(reflect_dot_eye, m.shininess)
                specular = light.intensity * m.specular * factor
        if in_shadow :
            diffuse = Color(0,0,0)
            specular = Color(0,0,0)
        return ambient + diffuse + specular