def main():
	print("_" * 78)
	print("|~~~>                       Welcome to Intake 0.1!                       <~~~|")
	print("|~~~~~~>         The Simple Python Repair Intake Application          <~~~~~~|")
	print("|~~~~~~~~~>                                                        <~~~~~~~~~|")
	print("|~~~~~~~~~~~>                     Enjoy! :)                     <~~~~~~~~~~~~|")
	print("|____________________________________________________________________________|")

	# Menu
	print("|_____________________________> Intake Home <________________________________|")
	print("| 1.) Start Device Inspection                2.) View Old Device Inspections |")
	print("|____________________________________________________________________________|")
	print("| ")

	select = input("| Make selction using numbers, then press enter: ")
	print("|____________________________________________________________________________|")    
 

	# Selection
	if select == "1":
		intake_start()
	elif select == "2":
		intake_old()
	else:
		print("Please choose a valid option...")
		print("_" * 78)
		main()

main()
