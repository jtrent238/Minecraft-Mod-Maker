
import os;
import urllib.request;
import zipfile;
import subprocess;
from shutil import copy;

print("==========================================================================")
print("======== Minecraft Mod Creator By jtrent238 | Version 1.0.0.0 =========")
print("==========================================================================")


#Get input from user
# ask_userName = input("Enter your Username [NO SPACES] [Alphanumeric ONLY] : ");
# ask_modName = input("Enter mod name [NO SPACES] [Alphanumeric ONLY] : ");
# ask_modVersion = input("Enter mod version [NO SPACES] [Alphanumeric ONLY] : ");

ask_Create = input("Do you want to make a new Block or Item? ")
if ask_Create in ['Block', 'block', 'B', 'b']:
	ask_blockName = input("Enter a name for your new block [Alphanumeric ONLY] : ")
	ask_blockHardness = input("Enter the hardness for your new block: ")
	# try:
		# blockHardness = int(ask_blockHardness)
		# print('valid')
	# except ValueError:
		# print('invalid')
if ask_Create in ['Item', 'item', 'I', 'i']:
	ask_itemName = input("Enter a name for your new item [Alphanumeric ONLY] : ")
# else:
	# print("you have entered something incorrectly");

#FOR TESTING ONLY
ask_modName = 'testmod'
ask_userName = 'testuser'
ask_modVersion = 'testver'
ask_blockName = 'testblock'
ask_itemName = 'testitem'
ask_blockHardness = '5'

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
createMainClass.write("public static string MODNAME = " + '"' + ask_modName + '"' +";"+ "\n");
createMainClass.write("public static string MODAUTHOR = "  + '"jtrent238, ' + ask_userName + '"' +";"+ "\n");
createMainClass.write("public static string MODVERSION = " + '"' + ask_modVersion + '"' +";"+ "\n");
createMainClass.write('@Mod.EventHandler' + '\n')
createMainClass.write('public void init(FMLInitializationEvent event)' + '\n')
createMainClass.write('{' + '\n')
if ask_Create in ['Block', 'block', 'B', 'b']:
	createMainClass.write("public static Block " + ask_blockName + ";"+ "\n")
	createMainClass.write(ask_blockName + ' = new Block(Material.rock).setBlockName("' + ask_blockName + '").setBlockTextureName("' + ask_blockName + '").setCreativeTab(' + mainClass + '.' + 'tab_' + mainClass + ').setHardness(' + ask_blockHardness + 'F);' + '\n')
	print('Your new block has been created!')
if ask_Create in ['Item', 'item', 'I', 'i']:
	createMainClass.write("public static Item " + ask_itemName + ";"+ "\n")
	createMainClass.write(ask_itemName + ' = new Item().setUnlocalizedName("' + ask_itemName + '").setTextureName("' + ask_itemName + '").setCreativeTab(' + mainClass + '.' + 'tab_' + mainClass + ');' + '\n')
	print('Your new item has been created!')
createMainClass.write('public static CreativeTabs ' + mainClass + ' = new CreativeTabs("' + mainClass + '")' + '\n')
createMainClass.write('public Item getTabIconItem() {' + '\n')
createMainClass.write('return new ItemStack(Items.diamond).getItem();' + '\n')
createMainClass.write('}' + '\n')
createMainClass.write('public boolean hasSearchBar(){' + '\n')
createMainClass.write('return false;' + '\n')
createMainClass.write('}' + '\n')
createMainClass.write('};' + '\n')
createMainClass.write('@Mod.EventHandler' + '\n')
createMainClass.write('public void postInit(FMLPostInitializationEvent event) {' + '\n')
createMainClass.write('{' + '\n')
createMainClass.write('}' + '\n')
createMainClass.write('}' + '\n')
# createMainClass.write('{' + '\n')
createMainClass.write("}");
createMainClass.close()

print("==========================================================================")
print("========WARNING IF YOU RE RUN THIS PROGRAM IT WILL OVERWRITE DATA=========")
print("==========================================================================")

ask_compileMod = input('Do you want to compile your new mod?: ')

mcForgezip = 'forge-1.7.10-10.13.4.1448-1.7.10-src.zip'
url = 'https://files.minecraftforge.net/maven/net/minecraftforge/forge/1.7.10-10.13.4.1448-1.7.10/forge-1.7.10-10.13.4.1448-1.7.10-src.zip'

exists = os.path.isfile('/' + mcForgezip)
if exists:
    print('file already exist skipping download')
else:
    print('Beginning download of Minecraft Forge 10.13.4.1448 for 1.7.10...');
urllib.request.urlretrieve(url, ask_modName + '/' + mcForgezip);
print('Minecraft Forge 10.13.4.1448 for 1.7.10 downloaded!');

def createMCForgeFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createMCForgeFolder(ask_modName + '/MinecraftForge/')

mcForgezip = zipfile.ZipFile(ask_modName + '/' + mcForgezip)
mcForgezip.extractall(ask_modName + '/MinecraftForge/')
 
mcForgezip.close()

def createMCForgeSrcFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createMCForgeSrcFolder(ask_modName + '/MinecraftForge/src/main/java/com/jtrent238/modmaker/mod')

copy(ask_modName + '/' + mainClass + '.java', ask_modName + '/MinecraftForge/src/main/java/com/jtrent238/modmaker/mod')	
	
if ask_compileMod in ['Yes', 'yes', 'y']:
	print('Compileing Mod...')
	compileScript = open(ask_modName + '/MinecraftForge/compileScript.bat', 'w')
	compileScript.write('@echo off' + '\n')
	compileScript.write('cls' + '\n')
	compileScript.write('gradlew setupdecompworkspace' + '\n')
	compileScript.write('gradlew build' + '\n')
	compileScript.close()
	# compileScript.write('gradlew eclipse')
	# compileScript.write('gradlew idea')
	# os.system('cd ' + ask_modName + '/' + 'MinecraftForge/') 
	os.system('cd ' + ask_modName)  
	os.system('dir')  
	
	os.system('start compileScript.bat')  
	# os.system('gradlew setupdecompworkspace') 
	# os.system('gradlew eclipse') 
	# os.system('gradlew idea') 
	# os.system('gradlew build') 
	print('Mod compiled')
	ask_testMod = input('do you want to test your new mod?')
	if ask_testMod in ['Yes', 'yes', 'y']:
		print('testingyes')
		runScript.open = (ask_modName + '/MinecraftForge/runScript.bat', 'w')
		runScript.write('@echo off' + '\n')
		runScript.write('cls' + '\n')
		runScript.write('gradlew runClient' + '\n')
		runScript.close()
		# os.system('gradlew runClient') 
		os.system('cd ' + ask_modName)  
		os.system('start runScript.bat')  
	if ask_testMod in ['No', 'no', 'n']:
		print('testingno')
	
if ask_compileMod in ['No', 'no', 'n']:
	print('Mod is complete')