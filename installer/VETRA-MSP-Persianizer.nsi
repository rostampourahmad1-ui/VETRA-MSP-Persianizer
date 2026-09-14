Unicode True
RequestExecutionLevel admin
Name "VETRA MSP Persianizer"
OutFile "VETRA-MSP-Persianizer-Setup.exe"
InstallDir "$PROGRAMFILES\VETRA\MSP Persianizer"

!include "MUI2.nsh"
!include "LogicLib.nsh"
!define MUI_ABORTWARNING
!define MUI_ICON ""

Var PowerShell

Function .onInit
  StrCpy $PowerShell "$WINDIR\System32\WindowsPowerShell\v1.0\powershell.exe"
  IfFileExists "$PowerShell" +3 0
    MessageBox MB_ICONSTOP "Windows PowerShell was not found."
    Abort
FunctionEnd

Section "VETRA MSP Persianizer" SecMain
  SetOutPath "$INSTDIR\installer"
  File "Install-Vetra.ps1"
  File "Uninstall-Vetra.ps1"
  SetOutPath "$INSTDIR"
  File /r "..\src"
  File /r "..\docs"
  File "..\pyproject.toml"
  ExecWait '"$PowerShell" -NoProfile -ExecutionPolicy Bypass -File "$INSTDIR\installer\Install-Vetra.ps1" -InstallRoot "$INSTDIR"'
  WriteUninstaller "$INSTDIR\Uninstall.exe"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VETRA-MSP-Persianizer" "DisplayName" "VETRA MSP Persianizer"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VETRA-MSP-Persianizer" "UninstallString" '"$INSTDIR\Uninstall.exe"'
SectionEnd

Section "Uninstall"
  ExecWait '"$PowerShell" -NoProfile -ExecutionPolicy Bypass -File "$INSTDIR\installer\Uninstall-Vetra.ps1" -InstallRoot "$INSTDIR"'
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\VETRA-MSP-Persianizer"
SectionEnd
