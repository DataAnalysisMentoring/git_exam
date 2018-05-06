# kdy bude pršet? věštění z koule
import random 

vestba=['Až naprší a uschne!','Až kočička vajíčko snese!','Až se vdáš!','Až poslední plastový sáček bude vyloven z moře!','Až mi doneseš tři zlaté vlasy děda vševěda!','Hahahaha :)','Až probudíš polibkem dešťovou vílu :-*','Až porostou na stromech jitrnice a v potoku poteče pivo :)']

while True:
	dotaz=input("Chceš vědět, kdy bude pršet? ano/ne: ")
	if dotaz=='ano':
		print(" Výborně. \n Zeptáme se věštěcké koule. \n o \n o \n o \n o")
		print("", random.choice(vestba))
	else:
		print("Máš recht, déšť široko daleko nevidí ani Medard, tak co zmůže věštěcká koule :)")
		break