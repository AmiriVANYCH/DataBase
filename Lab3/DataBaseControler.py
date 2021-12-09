import view
import model_sqlalchemy
import controller



c = controller.Controller(model_sqlalchemy.ModelBasic(), view.View())
c.run()



