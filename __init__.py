from .nodes import *

NODE_CLASS_MAPPINGS = {
    "Create Project Root": CreateProjectRoot,
    "Add Folder": AddFolder,
    "Add Folder Advanced": AddFolderAdvanced,
    "Add File Name Prefix": AddFileNamePrefix,
    "Add File Name Prefix Advanced": AddFileNamePrefixAdvanced,
    "Join Variables": JoinVariables,
    "Show Path": ShowPath,
    "Show String": ShowString,
}

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]
print("\033[34mComfyUI Path Helper Nodes: \033[92mLoaded\033[0m")
