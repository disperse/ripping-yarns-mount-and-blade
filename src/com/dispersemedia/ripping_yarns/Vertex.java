package com.dispersemedia.ripping_yarns;

public class Vertex {
    public int index;
    public double x;
    public double y;
    public double z;

    public Vertex (int index, double x, double y, double z) {
        this.index = index;
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public String toString() {
        return String.format( "%.6f", this.x) + " " + String.format( "%.6f", this.y) + " " + String.format( "%.6f", this.z);
    }
}

