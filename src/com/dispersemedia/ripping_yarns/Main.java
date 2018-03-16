package com.dispersemedia.ripping_yarns;

import org.apache.commons.io.FileUtils;

import java.io.File;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        WorldMap map = new WorldMap(80, 80, 3);
        File inFile = new File("default/map.txt");
        File outFile = new File("C:/Program Files (x86)/Steam/steamapps/common/MountBlade Warband/Modules/RippingYarns/map.txt");
        try {
            FileUtils.forceDelete(outFile);
            FileUtils.touch(outFile);
            FileUtils.writeStringToFile(outFile, map.toString());
            // Restore to default
            // FileUtils.copyFile(inFile, outFile);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
