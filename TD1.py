coord_a = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2)]
coord_b = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
coord_c = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
coord_d = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (2, 2)]

coord = coord_d

size = len(coord)
max_ = max(max(coord))

cpt = 0

for i in range(0, size-1):
    for x in range(coord[i][0]+1, max_+1):
        for y in range(coord[i][1]+1, max_+1):
            if (x, coord[i][1]) in coord and (coord[i][0], y) in coord and (x, y) in coord:
                cpt += 1

print("Nb de rectangles :", cpt)


