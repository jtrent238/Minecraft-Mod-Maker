@echo off
cls
cd testmod\MinecraftForge/
timeout /t 2
gradlew setupdecompworkspace
gradlew build
