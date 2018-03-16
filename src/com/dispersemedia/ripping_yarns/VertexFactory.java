package com.dispersemedia.ripping_yarns;

import java.util.Map;

public class VertexFactory {
    private int nextIndex;
    private Map<String, Vertex> vertices;
    public VertexFactory(Map<String, Vertex> vertices) {
        this.vertices = vertices;
        this.nextIndex = 0;
    }

    public Vertex createVertex(double x, double y, double z) {
        if (vertices.containsKey(x + "-" + y)) {
            return vertices.get(x + "-" + y);
        } else {
            Vertex vertex = new Vertex(nextIndex, x, y, z);
            nextIndex++;
            vertices.put((x + "-" + y), vertex);
            return vertex;
        }
    }

    public Vertex createVertex(double x, double y) {
      return createVertex(x, y, -0.000002);
    }
}
