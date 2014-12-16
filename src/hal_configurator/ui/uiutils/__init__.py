def layout_widgets(layout):
  return (layout.itemAt(i) for i in range(layout.count()))

class UIVisibilitySettings(object):
  show_admin_vars = False
  show_not_editable_vars = False
  def __init__(self):
    pass

  @staticmethod
  def settings_for_mode(mode):
    res = UIVisibilitySettings()
    if mode == 'admin':
      res.show_admin_vars = True
      res.show_not_editable_vars = True
    elif mode == 'moderator':
      res.show_admin_vars = True
      res.show_not_editable_vars = False
    return res



