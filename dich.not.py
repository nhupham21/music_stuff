import re
notes=[
		"C2","C2#","D2","D2#","E2","F2","F2#","G2","G2#","A2","A2#","B2",
		"C3","C3#","D3","D3#","E3","F3","F3#","G3","G3#","A3","A3#","B3",
		"C4","C4#","D4","D4#","E4","F4","F4#","G4","G4#","A4","A4#","B4",
		"C5","C5#","D5","D5#","E5","F5","F5#","G5","G5#","A5","A5#","B5",
		"C6","C6#","D6","D6#","E6","F6","F6#","G6","G6#","A6","A6#","B6",
		"C7","C7#","D7","D7#","E7","F7","F7#","G7","G7#","A7","A7#","B7"
		]
#print(len(notes))
#print(notes)

#check="C2"
#if check in notes:
#	print(notes.index(check))

def checkstep(note1,note2):
	if note1 in notes:
		step_note1=notes.index(note1)
	else:
		print(note1 + " not found\n");
		return 0;
	if note2 in notes:
		step_note2=notes.index(note2)
	else:
		print(note2 + " not found\n");
		return 0;
	return step_note2 - step_note1

step=checkstep("C4","A3#")
#step=4
print("step: "+str(step))
duration=0.3
break_duration=0.25

file=open('tab.txt','r', encoding="utf-8")
lines=file.readlines()

for line in lines:
	if line.strip() == "":
		print("")
	elif line.startswith("#"):
		print(line,end='')
	else:
		for char in line.split():
			print(notes[notes.index(char)+step],end=" ")			
		print("")