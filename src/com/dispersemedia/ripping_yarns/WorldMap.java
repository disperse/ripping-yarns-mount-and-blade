package com.dispersemedia.ripping_yarns;

import java.util.*;

public class WorldMap {
    private List<Hex> hexes = new ArrayList<Hex>();

    private Map<String, Vertex> vertices;
    private HexFactory hexFactory;

    public WorldMap(int x, int y, int r) {
        vertices = new HashMap<String, Vertex>();
        hexFactory = new HexFactory(vertices);

        double h = (Math.sqrt(3.0) / 2) * r;
        double startY = -((y / 2) * h * 2);
        double startX = -((x / 2) * 1.5 * r);

        for (int curX = 0; curX < x; curX++) {
            for (int curY = 0; curY < y; curY++) {
                double xPos = startX + (curX * 1.5 * r);
                double yPos = startY + (curY * h * 2) + ((curX % 2 == 0) ? 0 : h);
                hexes.add(hexFactory.createHex(r, xPos, yPos));
            }
        }
    }

    @Override
    public String toString() {
        String returnString = "";
        SortedSet<Vertex> vertices = new TreeSet<Vertex>(new Comparator<Vertex>() {
            public int compare(Vertex a, Vertex b) {
                return a.index - b.index;
            }
        });

        for (Hex hex : hexes) {
            for (int i = 0; i < 7; i++) {
                vertices.add(hex.vertices[i]);
            }
        }

        Set<Face> faces = new HashSet<Face>();
        for (Hex hex : hexes) {
            for (int i = 0; i < 6; i++) {
                faces.add(hex.faces[i]);
            }
        }
        returnString += vertices.size() + System.getProperty("line.separator");

        for (Vertex v : vertices) {
            returnString += v.toString() + System.getProperty("line.separator");
        }

        returnString += faces.size() + System.getProperty("line.separator");

        for (Face f : faces) {
            returnString += f.toString() + System.getProperty("line.separator");
        }

        return returnString;
    }
}
