#from ui.lib.dragable_list import DraggableList
#globals()["DraggableList"] = DraggableList

import sys
import hal_configurator.ui.custom_widgets.dragable_list as dlv
import hal_configurator.ui.custom_widgets.dropable_line_edit as dtxt
import hal_configurator.ui.custom_widgets.resources_list as rl
sys.modules["dragable_list"] = dlv
sys.modules["dropable_line_edit"]= dtxt
sys.modules["resources_list"] = rl