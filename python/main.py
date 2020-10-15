from graham_scan import *

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

npoints = 8
pts = create_points_3d(npoints, 10, 15)

xs, ys, zs = zip(*pts)
ax.scatter(xs, ys, zs, c='r')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

i_id = None
j_id = None
max_dist = -1
for i in range(npoints):
    pt_i = pts[i]
    for j in range(i + 1, npoints):
        pt_j = pts[j]
        dist = (pt_i[0]-pt_j[0]) * (pt_i[0]-pt_j[0])
        dist += (pt_i[1]-pt_j[1]) * (pt_i[1]-pt_j[1])
        dist += (pt_i[2]-pt_j[2]) * (pt_i[2]-pt_j[2])
        dist = sqrt(dist)
        if dist > max_dist:
            max_dist = dist
        print(pt_i, pt_j, dist)

print(max_dist)
#pts = create_points_3d(10, 0, 20 * 10)
#print(pts)
#scatter_plot_3d(pts)

# hull = graham_scan(pts, False)
#
# min_square_len = 0
# i_min = 0
# for ptid in range(len(hull)):
#     pt0 = hull[ptid % len(hull)]
#     pt1 = hull[(ptid + 1) % len(hull)]
#     dy = pt1[1] - pt0[1]
#     dx = pt1[0] - pt0[0]
#     theta = -atan2(dy, dx)
#     c = cos(theta)
#     s = sin(theta)
#
#     rotated_pt = [None] * 2
#     rotated_hull = []
#     for j in range(len(hull)):
#         ptj = hull[j]
#         rotated_pt[0] = pt0[0] + (ptj[0] - pt0[0]) * c - (ptj[1] - pt0[1]) * s
#         rotated_pt[1] = pt0[1] + (ptj[0] - pt0[0]) * s + (ptj[1] - pt0[1]) * c
#         rotated_hull.append(rotated_pt[:])
#
#     xs, ys = zip(*pts)  # unzip into x and y coord lists
#     plt.scatter(xs, ys, color='grey')  # plot the data points
#
#     xs, ys = zip(*rotated_hull)  # unzip into x and y coord lists
#     plt.scatter(xs, ys, color='green')  # plot the data points
#
#     min_x = None
#     min_y = None
#     max_x = None
#     max_y = None
#     for i in range(len(hull)):
#         if i == 0:
#             min_x = rotated_hull[i][0]
#             min_y = rotated_hull[i][1]
#             max_x = rotated_hull[i][0]
#             max_y = rotated_hull[i][1]
#         if rotated_hull[i][0] < min_x:
#             min_x = rotated_hull[i][0]
#         if rotated_hull[i][1] < min_y:
#             min_y = rotated_hull[i][1]
#         if rotated_hull[i][0] > max_x:
#             max_x = rotated_hull[i][0]
#         if rotated_hull[i][1] > max_y:
#             max_y = rotated_hull[i][1]
#
#     dx = max_x - min_x
#     dy = max_y - min_y
#     min_square_i = max(dx, dy)
#     if ptid == 0:
#         min_square_len = min_square_i
#     elif min_square_i < min_square_len:
#         min_square_len = min_square_i
#         i_min = ptid
#
#     print("Point: ", ptid, " MinSquareLenght: ", min_square_i)
#
#     plt.scatter([min_x, min_x, max_x, max_x], [min_y, max_y, min_y, max_y], color='red')  # plot the data points
#
#     if hull is not None:
#         # plot the convex hull boundary, extra iteration at
#         # the end so that the bounding line wraps around
#         for i in range(1, len(hull) + 1):
#             if i == len(hull): i = 0  # wrap
#             c0 = hull[i - 1]
#             c1 = hull[i]
#             plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'grey')
#
#     if rotated_hull is not None:
#         # plot the convex hull boundary, extra iteration at
#         # the end so that the bounding line wraps around
#         for i in range(1, len(rotated_hull) + 1):
#             if i == len(rotated_hull): i = 0  # wrap
#             c0 = rotated_hull[i - 1]
#             c1 = rotated_hull[i]
#             plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'green')
#
#     plt.plot((min_x, min_x), (min_y, max_y), 'red')
#     plt.plot((min_x, max_x), (min_y, min_y), 'red')
#     plt.plot((max_x, max_x), (min_y, max_y), 'red')
#     plt.plot((min_x, max_x), (max_y, max_y), 'red')
#
#     plt.axis('equal')
#     plt.show()
#
# print("The minimum square containing the points is: ", min_square_len, ", at Point: ", i_min)
