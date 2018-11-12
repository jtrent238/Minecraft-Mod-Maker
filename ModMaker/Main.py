
import os;

print("==========================================================================")
print("======== Minecraft Mod Creator By jtrent238 | Version 1.0.0.0 =========")
print("==========================================================================")

#Get input from user
ask_userName = input("Enter your Username [NO SPACES]: ");
ask_modName = input("Enter mod name [NO SPACES]: ");
ask_modVersion = input("Enter mod version [NO SPACES]: ");

#FOR TESTING ONLY
# ask_modName = 'testmod'
# ask_userName = 'testuser'

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
		
createMainClass = open(ask_modName + "/mod_" + ask_modName + "Main.java", "w")
createMainClass.write("package com.jtrent238.modmaker.mod." + ask_userName + "." + ask_modName + ";" + "\n");
createMainClass.write("@Mod(modid=" + ask_modName + ", name=" + ask_modName + ", version=" + ask_modVersion +")" + "\n");
createMainClass.write("public class "+ "mod_" + ask_modName + "{" "\n");
createMainClass.write("}");

