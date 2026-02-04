Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")
batPath = fso.GetParentFolderName(WScript.ScriptFullName) & "\\run_panel.bat"
shell.Run Chr(34) & batPath & Chr(34), 0, False
