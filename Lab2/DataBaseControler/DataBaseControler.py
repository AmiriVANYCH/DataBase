import view
import model
import controller


c = controller.Controller(model.ModelBasic(), view.View())
c.show_make()
#c.create_make("Lanos")
#c.update_make(17,"Mersedez","Mersedez")
#c.del_make(18)
#c.show_make()

