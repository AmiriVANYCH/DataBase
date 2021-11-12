import view
import model
import controller



c = controller.Controller(model.ModelBasic(), view.View())
c.show_CarType()
c.run()

def clear():
    print("\n"*40)




def select_from_contract ( CarNumber = None, ContractEnd = None, ContractID =None , ContractStart = None , ParkingID = None, PersonID = None):
    query ='select 	"CarNumber", "ContractEnd", "ContractID", "ContractStart", "ParkingID", "PersonID" from public."Contract" where '
    curt=''
    if CarNumber:
        curt = curt + '"CarNumber" = ' + "'" + CarNumber + "'" 

    if ContractEnd:
        curt = curt + '"ContractEnd" = ' + "'" + ContractEnd + "'" 
        
    if ContractID:
        curt = curt + '"ContractID" = ' +   ContractID 
        
    if ContractStart:
        curt = curt + '"ContractStart" = ' + "'" + ContractStart + "'"
        
    if ParkingID:
        curt = curt + '"ParkingID" = '  + ParkingID 

    if PersonID:
        curt = curt + '"PersonID" = '  + PersonID 




