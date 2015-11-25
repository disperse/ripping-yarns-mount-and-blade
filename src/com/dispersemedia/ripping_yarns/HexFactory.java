package com.dispersemedia.ripping_yarns;

import java.util.Map;
import java.util.Random;

public class HexFactory {
    private Map<String, Vertex> vertices;
    private VertexFactory vertexFactory;
    public HexFactory(Map<String, Vertex> vertices) {
        this.vertices = vertices;
        this.vertexFactory = new VertexFactory(vertices);
    }

    public Hex createHex(double r, double x, double y) {
        Face[] faces = new Face[6];
        Vertex[] vertices = new Vertex[7];
        double h = (Math.sqrt(3.0) / 2) * r;
        vertices[0] = vertexFactory.createVertex(x, y);
        vertices[1] = vertexFactory.createVertex(x - (r/2), y - h);
        vertices[2] = vertexFactory.createVertex(x + (r/2), y - h);
        vertices[3] = vertexFactory.createVertex(x + r, y);
        vertices[4] = vertexFactory.createVertex(x + (r/2), y + h);
        vertices[5] = vertexFactory.createVertex(x - (r/2), y + h);
        vertices[6] = vertexFactory.createVertex(x - r, y);

        // Random terrain per hex
        int t = (new Random().nextInt(10) + 1);
        if (t > 5) t += 3;

        faces[0] = new Face(t, vertices[1], vertices[2], vertices[0]);
        faces[1] = new Face(t, vertices[2], vertices[3], vertices[0]);
        faces[2] = new Face(t, vertices[0], vertices[3], vertices[4]);
        faces[3] = new Face(t, vertices[0], vertices[4], vertices[5]);
        faces[4] = new Face(t, vertices[6], vertices[0], vertices[5]);
        faces[5] = new Face(t, vertices[1], vertices[0], vertices[6]);
        Hex hex = new Hex(vertices, faces);
        return hex;
    }
}
