# Devon Clark
# Quaternion

import math

class Quaternion:
    scalar = 0
    x = 0
    y = 0
    z = 0

    def __init__(self, x, y, z, scalar=None):
        if scalar != None:
            self.scalar = scalar
            self.x = x
            self.y = y
            self.z = z
        else:
            x *= 0.5
            y *= 0.5
            z *= 0.5

            c1 = math.cos(z)
            c2 = math.cos(y)
            c3 = math.cos(x)

            s1 = math.sin(z)
            s2 = math.sin(y)
            s3 = math.sin(x)

            self.scalar = (c1 * c2 * c3 - s1 * s2 * s3)
            self.x = (c1 * s2 * c3 - s1 * c2 * s3)
            self.y = (s1 * s2 * c3 + c1 * c2 * s3)
            self.z = (s1 * c2 * c3 + c1 * s2 * s3)

    def toEuler(self):
        sqw = math.pow(self.scalar, 2)
        sqx = math.pow(self.x, 2)
        sqy = math.pow(self.y, 2)
        sqz = math.pow(self.z, 2)
        yaw = 0.0
        roll = 0.0
        pitch = 0.0
        retv = [0]*3
        unit = sqx + sqy + sqz + sqw

        test = self.scalar * self.x + self.y * self.z
        if unit == 0:
            return [pitch, roll, yaw]
        elif test > 0.499 * unit:
            yaw = 2.0 * math.atan2(self.y, self.scalar)
            pitch = 1.570796326794897
            roll = 0.0
        elif test < -0.499 * unit:
            yaw = -2.0 * math.atan2(self.y, self.scalar)
            pitch = -1.570796326794897
            roll = 0.0
        else:
            yaw = math.atan2(2.0 * (self.scalar * self.z - self.x * self.y), 1.0 - 2.0 * (sqz + sqx))
            roll = math.asin(2.0 * test / unit)
            pitch = math.atan2(2.0 * (self.scalar * self.y - self.x * self.z), 1.0 - 2.0 * (sqy + sqx))
        
        retv[0] = pitch
        retv[1] = roll
        retv[2] = yaw
        return retv

    def conjugate(self):
        return Quaternion(-self.x, -self.y, -self.z, self.scalar)

    def times(self, b):
        y0 = self.scalar * b.scalar - self.x * b.x - self.y * b.y - self.z * b.z
        y1 = self.scalar * b.x + self.x * b.scalar + self.y * b.z - self.z * b.y
        y2 = self.scalar * b.y - self.x * b.z + self.y * b.scalar + self.z * b.x
        y3 = self.scalar * b.z + self.x * b.y - self.y * b.x + self.z * b.scalar
        return Quaternion(y1, y2, y3, y0)







