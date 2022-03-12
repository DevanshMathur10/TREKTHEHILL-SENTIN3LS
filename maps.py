import gmplot
coords=(26.936549, 75.789425,18)
def map():
    
    gmap=gmplot.GoogleMapPlotter(26.936549, 75.789425,18)
    gmap.marker(26.936549, 75.789425, color='cornflowerblue')

    safelats, safelngs = zip(*[
    (26.9362125,75.7865287),
    (26.9354473,75.7855417),
    (26.9309804,75.7827414),
    (26.9316686,75.7817973),
    (26.9316686,75.7817973),
    (26.9361331,75.7889802)
    ])
    gmap.scatter(safelats, safelngs, color='red', size=40)

    safearea = zip(*[
    (26.93656499588353, 75.79018627048376),
    (26.937349310820757, 75.78890953900668),
    (26.936928459581516, 75.78852330091279),
    (26.937052802156604, 75.78753624800613),
    (26.936679774019993, 75.78749333266236),
    (26.936608037698402, 75.78797613027974),
    (26.936196748573646, 75.78794394377192),
    (26.935938496496032, 75.7898268544797)
    ])
    gmap.polygon(*safearea, color='green', edge_width=5)

    gmap.draw('map.html')
