
import os;

print("==========================================================================")
print("======== Minecraft Mod Creator By jtrent238 | Version 1.0.0.0 =========")
print("==========================================================================")

#Get input from user
# ask_userName = input("Enter your Username [NO SPACES]: ");
# ask_modName = input("Enter mod name [NO SPACES]: ");
# ask_modVersion = input("Enter mod version [NO SPACES]: ");

ask_Create = input("Do you want to make a new Block or Item?: ")
if ask_Create in ['Block', 'block', 'B', 'b']:
	ask_blockName = input("Enter a name for your new block: ")
	ask_blockHardness = input("Enter the hardness for your new block: ")
if ask_Create in ['Item', 'item', 'I', 'i']:
	ask_itemName = input("Enter a name for your new item: ")
# else:
	# print("you have entered something incorrectly");

#FOR TESTING ONLY
ask_modName = 'testmod'
ask_userName = 'testuser'
ask_modVersion = 'testver'
ask_blockName = 'testblock'
ask_itemName = 'testitem'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
		
createFolder('./' + ask_modName + '/')

# def createMainClass(mainClass):
    # try:
        # if not os.path.exists(mainClass):
            # os.makedirs(mainClass)
    # except OSError:
        # print ('Error: Creating Main Classfile. ' +  mainClass)

mainClass = 'mod_' + ask_modName + 'Main'
createMainClass = open(ask_modName + "/mod_" + ask_modName + "Main.java", "w")
createMainClass.write("package com.jtrent238.modmaker.mod." + ask_userName + "." + ask_modName + ";" + "\n");
# createMainClass.write("@Mod(modid=" + ask_modName + ", name=" + ask_modName + ", version=" + ask_modVersion +")" + "\n");
createMainClass.write("@Mod(modid=MODID, name=MODNAME, version=MODVERSION)" + "\n");
createMainClass.write("public class "+ "mod_" + ask_modName + "{" + "\n");
createMainClass.write("public static string MODID = " + '"' + ask_modName + '"' +";"+ "\n");
createMainClass.write("public static string MODAUTHOR = "  + '"jtrent238, ' + ask_userName + '"' +";"+ "\n");
createMainClass.write("public static string MODVERSION = " + '"' + ask_modVersion + '"' +";"+ "\n");
if ask_Create in ['Block', 'block', 'B', 'b']:
	createMainClass.write("public static Block " + ask_blockName + ";"+ "\n")
	createMainClass.write(ask_blockName + ' new Block(Material.rock).setBlockName("' + ask_blockName + '").setBlockTextureName("' + ask_blockName + '").setCreativeTab(' + mainClass + mainClass + ').setHardness(' + ask_blockHardness + 'F");')
if ask_Create in ['Item', 'item', 'I', 'i']:
	createMainClass.write("public static Item " + ask_itemName + ";"+ "\n")
createMainClass.write("}");

