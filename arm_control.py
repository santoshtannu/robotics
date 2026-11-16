from robotarm_move_pkg.move import RobotActionExecutor
import time
executor = RobotActionExecutor()
executor.execute_action(action_name="move") ## Default move action
print(f"✅ END")
