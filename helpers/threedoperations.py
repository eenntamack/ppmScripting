
class Intersection:
    def __init__(self, t, object):
        self.t = t
        self.object = object

    def __str__(self):
        return self.object.id

    def __repr__(self):
        return f"Intersection(t={self.t}, object={self.object})"

    def __lt__(self, other):
        return self.t < other.t


class Intersections:
    def __init__(self, *inters: Intersection):
        self.inters = list(inters)
        self.count = len(self.inters)
        self.inters.sort()

    def add_intersect(self, inter: Intersection):
        self.inters.append(inter)
        self.count += 1
        self.inters.sort()

    def __getitem__(self, index):
        return self.inters[index]

    def hit(self):
        valid = [inter for inter in self.inters if inter.t >= 0]

        if not valid:
            return None

        return min(valid, key=lambda inter: inter.t)

    def __str__(self):
        return "\n".join(str(inter) for inter in self.inters)