package com.jtrent238.modmaker.mod.testuser.testmod;
@Mod(modid=MODID, name=MODNAME, version=MODVERSION)
public class mod_testmod{
public static string MODID = "testmod";
public static string MODAUTHOR = "jtrent238, testuser";
public static string MODVERSION = "testver";
public static Block testblock;
testblock new Block(Material.rock).setBlockName("testblock").setBlockTextureName("testblock").setCreativeTab(mod_testmodMain.tab_mod_testmodMain).setHardness(5F);
}