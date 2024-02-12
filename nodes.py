import os
from datetime import datetime
import folder_paths


class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False


ANY = AnyType("*")


def format_date_time(string, position, datetime_format):
    today = datetime.now()
    if position == "prefix":
        return f"{today.strftime(datetime_format)}_{string}"
    if position == "postfix":
        return f"{string}_{today.strftime(datetime_format)}"


def format_variables(string, input_variables):
    if input_variables:
        variables = str(input_variables).split(",")
        return string.format(*variables)
    else:
        return string


#
class CreateProjectRoot:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "project_root_name": ("STRING", {"multiline": False, "default": ""}),
                "output_path_generation": (["relative", "absolute"],)
            }
        }

    RETURN_TYPES = ("PATH",)
    FUNCTION = "create_project_root"
    CATEGORY = "path_helper"

    def create_project_root(self, project_root_name, output_path_generation):
        if output_path_generation == "relative":
            return ("./" + project_root_name,)
        elif output_path_generation == "absolute":
            return (os.path.join(self.output_dir, project_root_name),)


class AddFolder:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("PATH",),
                "folder_name": ("STRING", {"multiline": False, "default": ""}),
            }
        }

    RETURN_TYPES = ("PATH",)
    FUNCTION = "add_folder"
    CATEGORY = "path_helper"

    def add_folder(self, path, folder_name):
        new_path = os.path.join(path, folder_name)
        return (new_path,)


class AddFolderAdvanced:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("PATH",),
                "folder_name": ("STRING", {"multiline": False, "default": ""}),
                "add_date_time": (["disable", "prefix", "postfix"],),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y_%m_%d_%H:%M:%S"}),
            },
            "optional": {
                "input_variables": (ANY,)
            }
        }

    RETURN_TYPES = ("PATH",)
    FUNCTION = "add_folder"
    CATEGORY = "path_helper"

    def add_folder(self, path, folder_name, add_date_time, date_time_format, input_variables=None):
        folder_name_parsed = format_variables(folder_name, input_variables)
        if add_date_time == "disable":
            new_path = os.path.join(path, folder_name_parsed)
        else:
            new_path = os.path.join(path, format_date_time(folder_name_parsed, add_date_time, date_time_format))
        return (new_path,)


class AddFileNamePrefix:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("PATH",),
                "file_name_prefix": ("STRING", {"multiline": False, "default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "add_filename_prefix"
    CATEGORY = "path_helper"

    def add_filename_prefix(self, path, file_name_prefix):
        new_path = os.path.join(path, file_name_prefix)
        return (new_path,)


class AddFileNamePrefixAdvanced:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("PATH",),
                "file_name_prefix": ("STRING", {"multiline": False, "default": ""}),
                "add_date_time": (["disable", "prefix", "postfix"],),
                "date_time_format": ("STRING", {"multiline": False, "default": "%Y_%m_%d_%H:%M:%S"}),
            },
            "optional": {
                "input_variables": (ANY,)
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "add_filename_prefix"
    CATEGORY = "path_helper"

    def add_filename_prefix(self, path, file_name_prefix, add_date_time, date_time_format, input_variables=None):
        filename_name_parsed = format_variables(file_name_prefix, input_variables)
        if add_date_time == "disable":
            new_path = os.path.join(path, filename_name_parsed)
        else:
            new_path = os.path.join(path, format_date_time(filename_name_parsed, add_date_time, date_time_format))
        return (new_path,)


class JoinVariables:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "var_1": (ANY,),
            },
            "optional": {
                "var_2": (ANY,),
                "var_3": (ANY,),
                "var_4": (ANY,),
            }
        }

    FUNCTION = "join_variables"
    CATEGORY = "path_helper"
    RETURN_TYPES = ("STRING",)

    def join_variables(self, var_1, var_2=None, var_3=None, var_4=None):
        variables = [var_1, var_2, var_3, var_4]
        return (','.join([str(var) for var in variables if var is not None]),)


class ShowPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("PATH",),
            },
        }

    INPUT_IS_LIST = True
    FUNCTION = "show_path"
    CATEGORY = "path_helper"
    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)

    def show_path(self, path):
        return {"ui": {"text": path}, "result": (path,)}


class ShowString:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string": ("STRING", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    FUNCTION = "show_string"
    CATEGORY = "path_helper"
    OUTPUT_NODE = True
    RETURN_TYPES = ("STRING",)

    def show_string(self, string):
        return {"ui": {"text": string}, "result": (string,)}
