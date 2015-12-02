; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{A38E2C66-A10F-4092-B169-92DB0A286E5B}
AppName=My Program
AppVersion=1.5
;AppVerName=My Program 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.example.com/
AppSupportURL=http://www.example.com/
AppUpdatesURL=http://www.example.com/
DefaultDirName={pf}\My Program
DefaultGroupName=My Program
OutputDir=C:\2DGP
OutputBaseFilename=GameInstaller
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\LG\Downloads\lab14_-_packaging\dist\MyGame.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\LG\Downloads\lab14_-_packaging\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\My Program"; Filename: "{app}\MyGame.exe"
Name: "{commondesktop}\My Program"; Filename: "{app}\MyGame.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\MyGame.exe"; Description: "{cm:LaunchProgram,My Program}"; Flags: nowait postinstall skipifsilent

