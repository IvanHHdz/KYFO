/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.kyfo;

import java.nio.file.Path;
import java.nio.file.Paths;

/**
 *
 * @author herni
 */
public class Commands {
    public static String getRute(){
        Path jarPath = Paths.get("").toAbsolutePath();
        return String.valueOf(jarPath);
    }
}
