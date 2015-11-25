package com.dispersemedia.ripping_yarns;

public class Hex {
    /*
      1___2
     /     \
    6   0   3
     \     /
      5___4
    */

    public Face[] faces;
    public Vertex[] vertices;

    public Hex(Vertex[] vertices, Face[] faces) {
        this.vertices = vertices;
        this.faces = faces;
    }
}
