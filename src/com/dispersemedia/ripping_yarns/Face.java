package com.dispersemedia.ripping_yarns;

import java.util.Random;

public class Face {
/*
    0
   / \
  /   \
 2_____1

rt_water                = 0
rt_mountain             = 1
rt_steppe               = 2
rt_plain                = 3
rt_snow                 = 4
rt_desert               = 5
rt_bridge               = 7
rt_river                = 8
rt_mountain_forest      = 9
rt_steppe_forest        = 10
rt_forest               = 11
rt_snow_forest          = 12
rt_desert_forest        = 13
rt_deep_water           = 15 --unofficial
*/
    public Vertex[] vertices = new Vertex[3];
    public int terrain;

    public Face(int terrain, Vertex vertex0, Vertex vertex1, Vertex vertex2) {
        vertices[0] = vertex0;
        vertices[1] = vertex1;
        vertices[2] = vertex2;
        this.terrain = terrain;
    }

    @Override
    public String toString() {
        return terrain + " 0 3 " + vertices[0].index + " " + vertices[1].index + " " + vertices[2].index;
    }

}
