package com.jtrent238.modmaker.mod.testuser.testmod;
import cpw.mods.fml.common.Loader;
import cpw.mods.fml.common.Mod;
import cpw.mods.fml.common.Mod.EventHandler;
import cpw.mods.fml.common.Mod.Instance;
import cpw.mods.fml.common.ModContainer;
import cpw.mods.fml.common.SidedProxy;
import cpw.mods.fml.common.event.FMLInitializationEvent;
import cpw.mods.fml.common.event.FMLPostInitializationEvent;
import cpw.mods.fml.common.event.FMLPreInitializationEvent;
import cpw.mods.fml.common.event.FMLServerStartingEvent;
import cpw.mods.fml.common.eventhandler.EventPriority;
import cpw.mods.fml.common.network.IGuiHandler;
import cpw.mods.fml.common.network.NetworkRegistry;
import cpw.mods.fml.common.registry.GameRegistry;
import cpw.mods.fml.common.registry.LanguageRegistry;
import net.minecraft.block.Block;
import net.minecraft.command.ICommandManager;
import net.minecraft.creativetab.CreativeTabs;
import net.minecraft.entity.player.EntityPlayer;
import net.minecraft.init.Items;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.server.MinecraftServer;
import net.minecraft.util.WeightedRandomChestContent;
import net.minecraft.world.World;
import net.minecraftforge.client.event.RenderGameOverlayEvent;
import net.minecraftforge.common.ChestGenHooks;
@Mod(modid=mod_testmodMain.MODID, name=mod_testmodMain.MODNAME, version=mod_testmodMain.MODVERSION)
public class mod_testmodMain{
public static final String MODID = "testmod";
public static final String MODNAME = "testmod";
public static final String MODAUTHOR = "jtrent238, testuser";
public static final String MODVERSION = "testver";
public static Block testblock;
testblock = new Block(Material.rock).setBlockName("testblock").setBlockTextureName("testblock").setCreativeTab(mod_testmodMain.tab_mod_testmodMain).setHardness(5F);
@Mod.EventHandler
public void init(FMLInitializationEvent event)
{
public Static CreativeTabs;
mod_testmodMain = new CreativeTabs("mod_testmodMain");
public Item getTabIconItem() {
return new ItemStack(Items.diamond).getItem();
}
public boolean hasSearchBar(){
return false;
}
};
@Mod.EventHandler
public void postInit(FMLPostInitializationEvent event) {
{
}
}
{
}