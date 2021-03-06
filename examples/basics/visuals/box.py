# -*- coding: utf-8 -*-
# Copyright (c) 2015, Vispy Development Team.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.

"""
Simple demonstration of the box geometry.
"""

import sys

from vispy import scene
from vispy import geometry

canvas = scene.SceneCanvas(keys='interactive', size=(800, 600), show=True)

view = canvas.central_widget.add_view()

vertices, faces, outline = geometry.create_box(width=2, height=4, depth=8,
                                               width_segments=4,
                                               height_segments=8,
                                               depth_segments=16)

box = scene.visuals.Box(width=4, height=4, depth=8, width_segments=4,
                        height_segments=8, depth_segments=16,
                        vertex_colors=vertices['color'],
                        edge_color='k',
                        parent=view.scene)

camera = scene.cameras.TurntableCamera(fov=45, azimuth=60, parent=view.scene)
view.camera = camera

if __name__ == '__main__' and sys.flags.interactive == 0:
    canvas.app.run()
