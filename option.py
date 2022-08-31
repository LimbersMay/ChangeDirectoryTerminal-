class Option:
    
    def __init__(self, switch, name, path, delete, list_paths, register):
        self.switch = switch # Path to switch to
        self.name = name # Name to the path to register
        self.path = path # Path to register
        self.delete = delete # Name of the path to delete
        self.list_paths = list_paths # Check if the user want to list all the paths in the json 
        
        self.register = register # Check if the user want to register the actual path

    def getSwitch(self):
        return self.switch

    def getName(self):
        return self.name

    def getPath(self):
        return self.path 
    
    def getDelete(self):
        return self.delete

    def getListPaths(self):
        return self.list_paths
    
    def getRegister(self):
        return self.register
