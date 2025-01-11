# Comfyui-Template-Loader
The Simplest way to load Prompt Templates in ComfyUI

# Features
- Load Prompt Templates from Files
- Easy to use

# Installation
```bash
git clone https://github.com/r3dsd/comfyui-template-loader.git
```
# Usage
1. You need to create a Template File in the `custom_nodes/comfyui-template-loader/template` folder

2. the Template File should be in the following format
```json
{
    "Key1": "Prompt1, Prompt2, Prompt3",
    "Key2": "Prompt1, Prompt2, Prompt3",
    ...
}
```

3. Done! You can use the TemplateLoader Node in your workflow

# Nodes
TemplateLoader
- Source: The file Name of the Template File
- Template: The Key of the Template

return: The String of the Template