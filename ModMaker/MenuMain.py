from tkinter import *
 
# def programVersion = '1.0.0.0'
master = Tk()
master.title('========== Minecraft Mod Creator By jtrent238 | Version 1.0.0.0 ==========')


def createNewMod():
	print(varModName)
	def createSaveFolder(directory):
		try:
			if not os.path.exists(directory):
				os.makedirs(directory)
		except OSError:
			print ('Error: Creating directory. ' +  directory)
			
		createFolder('./' + varModName + '/')

		modData = 'mod_' + varModName + 'Main'
		createmodData = open(varModName + '/mod_' + varModName + '.jtmcmm', 'w')
		createmodData.write(varModName + '\n');
		createmodData.close()
		
varModName = StringVar()

Label(master, text='Mod Name').pack(pady=2, padx=5)
textbox_ModName = Entry(master, textvariable=varModName)
textbox_ModName.focus_set()
textbox_ModName.pack(pady=10, padx=10)

button_CreateMod = Button(master, text="Create Mod", command=createNewMod)
button_CreateMod.pack()
 

mainloop()