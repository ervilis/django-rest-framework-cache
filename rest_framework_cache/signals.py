from .utils import clear_for_instance


def clear_instance(sender, instance, **kwargs):
    """Calls cache cleaner for current instance"""
    clear_for_instance(instance)
