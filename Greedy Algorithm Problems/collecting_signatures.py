from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    segments.sort(key= lambda x: x[1])
    points=[]
    while len(segments) != 0:
        p = segments[0].end
        for i in segments[:]:
            if i.start <= p <= i.end:
                segments.remove(i)
        points.append(p)       
    return points

if __name__ == '__main__':
    n = int(input())
    segments = []
    for i in range(n):
        a, b = map(int, input().split())
        segments.append(Segment(a, b))
    points = optimal_points(segments)
    print(len(points))
    print(*points)