@echo off
cls
cd testmod\MinecraftForge/
gradlew cleancache
timeout /t 2
gradlew setupdecompworkspace
gradlew build
