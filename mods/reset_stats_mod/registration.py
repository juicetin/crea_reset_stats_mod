from siege import game


def register():
    game.onUnregistration.listen(systemUnregistration)
    # Register anything you need to here! Be sure to import it above and unregister it below!


def systemUnregistration():
    game.onUnregistration.remove(systemUnregistration)
    # Unregister everything that you have registered above!
