def rgb_to_lab(r, g, b):
    r, g, b = [x / 255. for x in [r, g, b]]

    var_r, var_g, var_b = 100 * norm(r), 100 * self.norm(g), 100 * self.norm(b),

    # Преобразование из RGB в XYZ
    x = (var_r * 0.412453 + var_g * 0.357580 + var_b * 0.180423)
    y = (var_r * 0.212671 + var_g * 0.715160 + var_b * 0.072169)
    z = (var_r * 0.019334 + var_g * 0.119193 + var_b * 0.950227)

    ref_x = 95.047
    ref_y = 100.000
    ref_z = 108.883

    # x = 4.950280289802328
    # y = 4.415476751814342
    # z = 27.025186241611866

    x /= ref_x
    y /= ref_y
    z /= ref_z

    # Преобразование из XYZ в LAB
    l = 116 * self.f_xyz(y) - 16
    a = 500 * (self.f_xyz(x) - self.f_xyz(y))
    b = 200 * (self.f_xyz(y) - self.f_xyz(z))

    # return x, y, z
    return round(l), round(a), round(b)


def f_xyz(t):
    return t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16.0 / 116.0

def norm(self, t):
        return ((t + 0.055) / 1.055) ** 2.4 if t > 0.045045 else t / 12.92