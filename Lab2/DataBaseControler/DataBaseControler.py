import view
import model
import controller



c = controller.Controller(model.ModelBasic(), view.View())
c.run()



