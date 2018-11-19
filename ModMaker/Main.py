
import os;
import urllib.request;
import zipfile;
import subprocess;
from shutil import copy;

print("==========================================================================")
print("========== Minecraft Mod Creator By jtrent238 | Version 1.0.0.0 ==========")
print("==========================================================================")

language = 'EN'

#Get input from user
ask_userName = input("Enter your Username [NO SPACES] [Alphanumeric ONLY] : ");
ask_modName = input("Enter mod name [NO SPACES] [Alphanumeric ONLY] : ");
ask_modVersion = input("Enter mod version [NO SPACES] [Alphanumeric ONLY] : ");

ask_Create = input("Do you want to make a new Block or Item? ")
if ask_Create in ['Block', 'block', 'B', 'b']:
	ask_blockName = input("Enter a name for your new block [Alphanumeric ONLY] : ")
	# ask_blockHardness = input("Enter the hardness for your new block: ")
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
# ask_modName = 'testmod'
# ask_userName = 'testuser'
# ask_modVersion = 'testver'
# ask_blockName = 'testblock'
# ask_itemName = 'testitem'
# ask_blockHardness = '5'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
		
createFolder('./' + ask_modName + '/')

def createResFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
		
createResFolder('./' + ask_modName + '/assets/Items')
createResFolder('./' + ask_modName + '/assets/Blocks')

# def createMainClass(mainClass):
    # try:
        # if not os.path.exists(mainClass):
            # os.makedirs(mainClass)
    # except OSError:
        # print ('Error: Creating Main Classfile. ' +  mainClass)

mainClass = 'mod_' + ask_modName + 'Main'
createMainClass = open(ask_modName + '/mod_' + ask_modName + 'Main.java', 'w')
createMainClass.write('/* GENERATED BY JTRENT238 MOD MAKER */' + '\n');
createMainClass.write('' + '\n')
createMainClass.write('package com.jtrent238.modmaker.mod.' + ask_userName + '.' + ask_modName + ';' + '\n');
createMainClass.write('' + '\n')
if ask_Create in ['Block', 'block', 'B', 'b']:
	createMainClass.write('import com.jtrent238.modmaker.mod.' + ask_userName + '.' + ask_modName + '.' + ask_blockName + ';' + '\n')
	createMainClass.write('' + '\n')
# if ask_Create in ['Item', 'item', 'i']:
	# createMainClass.write('import com.jtrent238.modmaker.mod.' + ask_userName + '.' + ask_modName + '.' + ask_itemName + ';' + '\n');
	# createMainClass.write('' + '\n')
createMainClass.write('import cpw.mods.fml.common.Loader;' + '\n');
createMainClass.write('import cpw.mods.fml.common.Mod;' + '\n');
createMainClass.write('import cpw.mods.fml.common.Mod.EventHandler;' + '\n');
createMainClass.write('import cpw.mods.fml.common.Mod.Instance;' + '\n');
createMainClass.write('import cpw.mods.fml.common.ModContainer;' + '\n');
createMainClass.write('import cpw.mods.fml.common.SidedProxy;' + '\n');
createMainClass.write('import cpw.mods.fml.common.event.FMLInitializationEvent;' + '\n');
createMainClass.write('import cpw.mods.fml.common.event.FMLPostInitializationEvent;' + '\n');
createMainClass.write('import cpw.mods.fml.common.event.FMLPreInitializationEvent;' + '\n');
createMainClass.write('import cpw.mods.fml.common.event.FMLServerStartingEvent;' + '\n');
createMainClass.write('import cpw.mods.fml.common.eventhandler.EventPriority;' + '\n');
createMainClass.write('import cpw.mods.fml.common.network.IGuiHandler;' + '\n');
createMainClass.write('import cpw.mods.fml.common.network.NetworkRegistry;' + '\n');
createMainClass.write('import cpw.mods.fml.common.registry.GameRegistry;' + '\n');
createMainClass.write('import cpw.mods.fml.common.registry.LanguageRegistry;' + '\n');
createMainClass.write('import net.minecraft.block.Block;' + '\n');
createMainClass.write('import net.minecraft.command.ICommandManager;' + '\n');
createMainClass.write('import net.minecraft.creativetab.CreativeTabs;' + '\n');
createMainClass.write('import net.minecraft.entity.player.EntityPlayer;' + '\n');
createMainClass.write('import net.minecraft.init.Items;' + '\n');
createMainClass.write('import net.minecraft.item.Item;' + '\n');
createMainClass.write('import net.minecraft.item.ItemStack;' + '\n');
createMainClass.write('import net.minecraft.server.MinecraftServer;' + '\n');
createMainClass.write('import net.minecraft.util.WeightedRandomChestContent;' + '\n');
createMainClass.write('import net.minecraft.world.World;' + '\n');
createMainClass.write('import net.minecraftforge.client.event.RenderGameOverlayEvent;' + '\n');
createMainClass.write('import net.minecraftforge.common.ChestGenHooks;' + '\n');
createMainClass.write('import net.minecraft.block.Block;' + '\n');
createMainClass.write('import net.minecraft.block.material.Material;' + '\n');
createMainClass.write('' + '\n')
createMainClass.write('' + '\n')
createMainClass.write('	@Mod(modid='+ mainClass + '.MODID, name=' + mainClass + '.MODNAME, version=' + mainClass + '.MODVERSION)' + '\n');
createMainClass.write('	public class ' + mainClass + '{' + '\n');
createMainClass.write('' + '\n')
createMainClass.write("		public static final String MODID = " + '"' + ask_modName + '"' +";"+ "\n");
createMainClass.write("		public static final String MODNAME = " + '"' + ask_modName + '"' +";"+ "\n");
createMainClass.write("		public static final String MODAUTHOR = "  + '"jtrent238, ' + ask_userName + '"' +";"+ "\n");
createMainClass.write("		public static final String MODVERSION = " + '"' + ask_modVersion + '"' +";"+ "\n");
if ask_Create in ['Block', 'block', 'B', 'b']:
	createMainClass.write('' + '\n')
	createMainClass.write("		public static Block " + ask_blockName + ";"+ "\n")
if ask_Create in ['Item', 'item', 'I', 'i']:
	createMainClass.write('' + '\n')
	createMainClass.write("		public static Item " + ask_itemName + ";"+ "\n")
createMainClass.write('' + '\n')
createMainClass.write('	@Mod.EventHandler' + '\n')
createMainClass.write('	public void init(FMLInitializationEvent event) {' + '\n')
if ask_Create in ['Block', 'block', 'B', 'b']:
	# createMainClass.write(ask_blockName + ' = new Block(Material.rock).setBlockName("' + ask_blockName + '").setBlockTextureName("' + ask_blockName + '").setCreativeTab(' + mainClass + '.' + 'tab_' + mainClass + ').setHardness(' + ask_blockHardness + 'F);' + '\n')
	createMainClass.write('' + '\n')
	createMainClass.write('		' + ask_blockName + ' = new ' + ask_blockName + '(Material.rock).setBlockName("' + ask_blockName + '").setBlockTextureName("' + ask_blockName + '").setCreativeTab(''CreativeTabs.tabMisc'');' + '\n')
	# blockClass = ask_blockName
	createBlockClass = open(ask_modName + '/' + ask_blockName + '.java', 'w')
	createBlockClass.write('/* GENERATED BY JTRENT238 MOD MAKER */' + '\n');
	createBlockClass.write('' + '\n')
	createBlockClass.write('package com.jtrent238.modmaker.mod.' + ask_userName + '.' + ask_modName + ';' + '\n');
	createBlockClass.write('' + '\n')
	# createBlockClass.write('import com.jtrent238.modmaker.mod.' + ask_userName + '.' + ask_modName + ';' + '\n')
	createBlockClass.write('' + '\n')
	createBlockClass.write('import cpw.mods.fml.relauncher.Side;' + '\n')
	createBlockClass.write('import cpw.mods.fml.relauncher.SideOnly;' + '\n')
	createBlockClass.write('import net.minecraft.block.Block;' + '\n')
	createBlockClass.write('import net.minecraft.block.material.Material;' + '\n')
	createBlockClass.write('import net.minecraft.entity.player.EntityPlayer;' + '\n')
	createBlockClass.write('import net.minecraft.item.ItemStack;' + '\n')
	createBlockClass.write('import net.minecraft.util.EnumChatFormatting;' + '\n')
	createBlockClass.write('import net.minecraft.util.StatCollector;' + '\n')
	createBlockClass.write('' + '\n')
	createBlockClass.write('public class ' + ask_blockName + ' extends Block{' + '\n')
	createBlockClass.write('' + '\n')
	createBlockClass.write('	public ' + ask_blockName + '(Material p_i45394_1_) {' + '\n')
	createBlockClass.write('		super(p_i45394_1_);' + '\n')
	createBlockClass.write('	}' + '\n')
	createBlockClass.write('' + '\n')
	createBlockClass.write('}' + '\n')
	createBlockClass.close()
	print('Your new block has been created!')
if ask_Create in ['Item', 'item', 'I', 'i']:
	# createMainClass.write(ask_itemName + ' = new Item("' + ask_itemName+ '").setUnlocalizedName("' + ask_itemName + '").setTextureName("' + ask_itemName + '").setCreativeTab(' + mainClass + '.' + 'tab_' + mainClass + ');' + '\n')
	createMainClass.write('' + '\n')
	createMainClass.write('		' + ask_itemName + ' = new Item().setUnlocalizedName("' + ask_itemName + '").setTextureName("' + ask_itemName + '").setCreativeTab(''CreativeTabs.tabMisc'');' + '\n')
	print('Your new item has been created!')
createMainClass.write('' + '\n')
createMainClass.write('	}' + '\n')
# createMainClass.write('public Static CreativeTabs;' + '\n')
# createMainClass.write(mainClass + ' = new CreativeTabs("' + mainClass + '");' + '\n')
# createMainClass.write('public Item getTabIconItem() {' + '\n')
# createMainClass.write('return new ItemStack(Items.diamond).getItem();' + '\n')
# createMainClass.write('}' + '\n')
# createMainClass.write('public boolean hasSearchBar(){' + '\n')
# createMainClass.write('return false;' + '\n')
# createMainClass.write('}' + '\n')
# createMainClass.write('};' + '\n')
createMainClass.write('' + '\n')
createMainClass.write('	@Mod.EventHandler' + '\n')
createMainClass.write('	public void postInit(FMLPostInitializationEvent event) {' + '\n')
if ask_Create in ['Block', 'block', 'b']:
	createMainClass.write('' + '\n')
	createMainClass.write('		GameRegistry.registerBlock(' + ask_blockName + ', "' + ask_blockName + '");' + '\n')
if ask_Create in ['Item', 'item', 'i']:
	createMainClass.write('' + '\n')
	createMainClass.write('		GameRegistry.registerItem(' + ask_itemName + ', ' + ask_itemName + '.getUnlocalizedName().substring(5));' + '\n')
createMainClass.write('' + '\n')
# createMainClass.write('{' + '\n')
createMainClass.write('')
createMainClass.write('	}' + '\n')
# createMainClass.write('}' + '\n')
# createMainClass.write('{' + '\n')
createMainClass.write('')
createMainClass.write("}");
createMainClass.close()

createBuildScript = open(ask_modName + "/build.gradle", "w")
createBuildScript.write('buildscript {' + '\n')
createBuildScript.write('    repositories {' + '\n')
createBuildScript.write('        mavenCentral()' + '\n')
createBuildScript.write('        maven {' + '\n')
createBuildScript.write('            name = "forge"' + '\n')
createBuildScript.write('            url = "http://files.minecraftforge.net/maven"' + '\n')
createBuildScript.write('        }' + '\n')
createBuildScript.write('        maven {' + '\n')
createBuildScript.write('            name = "sonatype"' + '\n')
createBuildScript.write('            url = "https://oss.sonatype.org/content/repositories/snapshots/"' + '\n')
createBuildScript.write('        }' + '\n')
createBuildScript.write('    }' + '\n')
createBuildScript.write('    dependencies {' + '\n')
createBuildScript.write('        classpath ''net.minecraftforge.gradle:ForgeGradle:1.2-SNAPSHOT''' + '\n')
createBuildScript.write('    }' + '\n')
createBuildScript.write('}' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('apply plugin: ''forge''' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('version = "' + ask_modVersion + '"' + '\n')
createBuildScript.write('group= "com.jtrent238.modmaker.mod.' + ask_modName +'" // http://maven.apache.org/guides/mini/guide-naming-conventions.html' + '\n')
createBuildScript.write('archivesBaseName = "' + ask_modName + '"' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('minecraft {' + '\n')
createBuildScript.write('    version = "1.7.10-10.13.4.1448-1.7.10"' + '\n')
createBuildScript.write('    runDir = "eclipse"' + '\n')
createBuildScript.write('}' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('dependencies {' + '\n')
createBuildScript.write('    // you may put jars on which you depend on in ./libs' + '\n')
createBuildScript.write('    // or you may define them like so..' + '\n')
createBuildScript.write('    //compile "some.group:artifact:version:classifier"' + '\n')
createBuildScript.write('    //compile "some.group:artifact:version"' + '\n')
createBuildScript.write('      ' + '\n')
createBuildScript.write('    // real examples' + '\n')
createBuildScript.write('    //compile ''com.mod-buildcraft:buildcraft:6.0.8:dev'  '// adds buildcraft to the dev env' + '\n')
createBuildScript.write('    //compile ''com.googlecode.efficient-java-matrix-library:ejml:0.24' '// adds ejml to the dev env' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('    // for more info...' + '\n')
createBuildScript.write('    // http://www.gradle.org/docs/current/userguide/artifact_dependencies_tutorial.html' + '\n')
createBuildScript.write('    // http://www.gradle.org/docs/current/userguide/dependency_management.html' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('}' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('processResources' + '\n')
createBuildScript.write('{' + '\n')
createBuildScript.write('    // this will ensure that this task is redone when the versions change.' + '\n')
createBuildScript.write('    inputs.property "version", project.version' + '\n')
createBuildScript.write('    inputs.property "mcversion", project.minecraft.version' + '\n')
createBuildScript.write('' + '\n')
createBuildScript.write('    // replace stuff in mcmod.info, nothing else' + '\n')
createBuildScript.write('    from(sourceSets.main.resources.srcDirs) {' + '\n')
createBuildScript.write('        include ''mcmod.info''' + '\n')
createBuildScript.write('                ' + '\n')
createBuildScript.write('        // replace version and mcversion' + '\n')
createBuildScript.write('        expand ''version'':project.version, ''mcversion'':project.minecraft.version' + '\n')
createBuildScript.write('    }' + '\n')
createBuildScript.write('        ' + '\n')
createBuildScript.write('    // copy everything else, thats not the mcmod.info' + '\n')
createBuildScript.write('    from(sourceSets.main.resources.srcDirs) {' + '\n')
createBuildScript.write('        exclude ''mcmod.info''' + '\n')
createBuildScript.write('    }' + '\n')
createBuildScript.write('}' + '\n')
createBuildScript.close()

createmcModInfo= open(ask_modName + "/mcmod.info", "w")
createmcModInfo.write('[' + '\n')
createmcModInfo.write('{' + '\n')
createmcModInfo.write('  "modid": "' + ask_modName + '",' + '\n')
createmcModInfo.write('  "name": " + ask_modName + ",' + '\n')
createmcModInfo.write('  "description": "Example placeholder mod.",' + '\n')
createmcModInfo.write('  "version": "${version}",' + '\n')
createmcModInfo.write('  "mcversion": "${mcversion}",' + '\n')
createmcModInfo.write('  "url": "",' + '\n')
createmcModInfo.write('  "updateUrl": "",' + '\n')
createmcModInfo.write('  "authorList": ["jtrent238"],' + ask_userName + '\n')
createmcModInfo.write('  "credits": "Mod made by jtrent238 Mod Maker",' + '\n')
createmcModInfo.write('  "logoFile": "",' + '\n')
createmcModInfo.write('  "screenshots": [],' + '\n')
createmcModInfo.write('  "dependencies": []' + '\n')
createmcModInfo.write('}' + '\n')
createmcModInfo.write(']' + '\n')
createmcModInfo.close()

if language in ['US']:
	createENUSlangFile.open  = open(ask_modName + "/en_US.lang", "w")
	if ask_Create in ['Block', 'block', 'b']:
		createENUSlangFile.write('tile.' + ask_blockName + '.name=' + ask_blockName)
	if ask_Create in ['Item', 'item', 'i']:
		createENUSlangFile.write('item.' + ask_itemName + '.name=' + ask_itemName)
	createENUSlangFile.close()

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

ask_assets = input('Do you have any textures?: ')

if ask_assets in ['Yes', 'yes', 'y']:
	if ask_Create in ['Block', 'block', 'b']:
		print('Place them in the "assets/Blocks" folder with the name ' + ask_blockName + '.png')
	if ask_Create in ['Item', 'item', 'i']:
		print('Place them in the "assets/Items" folder with the name ' + ask_itemName+ '.png')

if ask_assets in ['No', 'no', 'n']:
	print('You said you did not have any assets... NOT adding them to the mod.')

def createMCForgeSrcFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createMCForgeSrcFolder(ask_modName + '/MinecraftForge/src/main/java/com/jtrent238/modmaker/mod')
createMCForgeSrcFolder(ask_modName + '/MinecraftForge/src/main/resources/assets/minecraft/textures/blocks')
createMCForgeSrcFolder(ask_modName + '/MinecraftForge/src/main/resources/assets/minecraft/textures/items')

copy(ask_modName + '/' + mainClass + '.java', ask_modName + '/MinecraftForge/src/main/java/com/jtrent238/modmaker/mod')	
if ask_Create in ['Block', 'block', 'b']:
	copy(ask_modName + '/' + ask_blockName + '.java', ask_modName + '/MinecraftForge/src/main/java/com/jtrent238/modmaker/mod')	
# copy(ask_modName + '/build.gradle', ask_modName + '/MinecraftForge')
copy(ask_modName + '/mcmod.info', ask_modName + '/MinecraftForge/src/main/resources/')

if ask_assets in ['Yes', 'yes', 'y']:
	if ask_Create in ['Block', 'block', 'b']:
		copy(ask_modName + '/assets/blocks/' + ask_blockName + '.png', ask_modName + '/MinecraftForge/src/main/resources/assets/minecraft/textures/blocks')	
	if ask_Create in ['Item', 'item', 'i']:
		copy(ask_modName + '/assets/items/' + ask_itemName + '.png', ask_modName + '/MinecraftForge/src/main/resources/assets/minecraft/textures/items')	

ask_delExample = input('Do you want to delete the example files provided by Forge?: ')

if ask_delExample in ['Yes', 'yes', 'y']:
	print('You choose to delete the sample files!')
	os.remove(ask_modName + "/MinecraftForge/src/main/java/com/example")
	os.remove(ask_modName + "/MinecraftForge/src/main/resources/mcmod.info")
if ask_delExample in ['No', 'no', 'n']:
	print('You chose not to delete the sample files!')

print('Setting up workspace...')

setupWorkspaceScript = open('setupWorkspaceScript.bat', 'w')
setupWorkspaceScript.write('@echo off' + '\n')
setupWorkspaceScript.write('cls' + '\n')
setupWorkspaceScript.write('cd ' + ask_modName + '\MinecraftForge/' + '\n')
setupWorkspaceScript.write('gradlew setupdecompworkspace' + '\n')
setupWorkspaceScript.close()
	
if ask_compileMod in ['Yes', 'yes', 'y']:
	print('Compileing Mod...')
	
	cleanCacheScript = open('cleanCacheScript.bat', 'w')
	cleanCacheScript.write('@echo off' + '\n')
	cleanCacheScript.write('cls' + '\n')
	cleanCacheScript.write('cd ' + ask_modName + '\MinecraftForge/' + '\n')
	cleanCacheScript.write('gradlew cleancache' + '\n')
	# cleanCacheScript.write('timeout /t 2' + '\n')
	# cleanCacheScript.write('gradlew setupdecompworkspace' + '\n')
	# cleanCacheScript.write('gradlew build' + '\n')
	cleanCacheScript.close()
	# compileScript.write('gradlew eclipse')
	# compileScript.write('gradlew idea')
	# os.system('cd ' + ask_modName + '/' + 'MinecraftForge/') 
	os.system('cd ' + ask_modName)  
	# os.system('dir')  
	
	# os.system('start cleanCacheScript.bat')  
	
	compileScript = open('compileScript.bat', 'w')
	compileScript.write('@echo off' + '\n')
	compileScript.write('cls' + '\n')
	compileScript.write('cd ' + ask_modName + '\MinecraftForge/' + '\n')
	# compileScript.write('gradlew cleancache' + '\n')
	# compileScript.write('timeout /t 2' + '\n')
	# compileScript.write('gradlew setupdecompworkspace' + '\n')
	compileScript.write('gradlew build' + '\n')
	compileScript.close()
	# compileScript.write('gradlew eclipse')
	# compileScript.write('gradlew idea')
	# os.system('cd ' + ask_modName + '/' + 'MinecraftForge/') 
	os.system('cd ' + ask_modName)  
	# os.system('dir')  
	
	os.system('start compileScript.bat')  
	# os.system('gradlew setupdecompworkspace') 
	# os.system('gradlew eclipse') 
	# os.system('gradlew idea') 
	# os.system('gradlew build') 
	# print('Mod compiled')
	ask_testMod = input('do you want to test your new mod?: ')
	if ask_testMod in ['Yes', 'yes', 'y']:
		print('testingyes')
		runScript = open('runScript.bat', 'w')
		runScript.write('@echo off' + '\n')
		runScript.write('cls' + '\n')
		runScript.write('cd ' + ask_modName + '\MinecraftForge/' + '\n')
		runScript.write('gradlew runclient' + '\n')
		runScript.close()
		# os.system('gradlew runClient') 
		# os.system('cd ' + ask_modName)  
		os.system('cd ' + ask_modName)  
		# os.system('dir')  
	
		os.system('start runScript.bat')   
	if ask_testMod in ['No', 'no', 'n']:
		print('testingno')
	
if ask_compileMod in ['No', 'no', 'n']:
	print('Mod is complete')

ask_cleanup = input('Do you want to clean up the build scripts?: ')

if ask_cleanup in ['Yes', 'yes', 'y']:
	print('Cleaning up some Junk')
	os.remove('compileScript.bat')
	os.remove('runScript.bat')
	os.remove('cleanCacheScript.bat')
if ask_cleanup in ['No', 'no', 'n']:
	print('Will NOT clean any files')
