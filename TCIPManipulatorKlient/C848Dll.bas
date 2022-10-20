Attribute VB_Name = "MC848Dll"
Option Explicit

'************************************************************
'*                                                          *
'*                  Only for DLL-Version.                   *
'*                                                          *
'************************************************************


'////////////////////////////////////////////
'// DLL initialization and comm functions. //
'////////////////////////////////////////////
Public Declare Function C848_InterfaceSetupDlg Lib "C848_DLL.dll" ( _
                                ByVal szRegKeyName As String _
                                ) As Long
                                
Public Declare Function C848_ConnectRS232 Lib "C848_DLL.dll" ( _
                                ByVal nPortNr As Long, _
                                ByVal nBaudRate As Long _
                                ) As Long
                                
Public Declare Function C848_ConnectNIgpib Lib "C848_DLL.dll" ( _
                                ByVal nBoard As Long, _
                                ByVal nDevAddr As Long _
                                ) As Long
                                
Public Declare Function C848_IsConnected Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Sub C848_CloseConnection Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                )
                                
Public Declare Function C848_FindOnRS Lib "C848_DLL.dll" ( _
                                ByRef pnStartPort As Long, _
                                ByRef pnStartBaud As Long _
                                ) As Long
                                
Public Declare Function C848_GetError Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Function C848_TranslateError Lib "C848_DLL.dll" ( _
                                ByVal errNr As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                

'/////////////////////////////
'// special C848 functions. //
'/////////////////////////////
Public Declare Function C848_CLR Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_DEL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal dSeconds As Double _
                                ) As Long
                                
Public Declare Function C848_DEM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Function C848_DFF Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long
                                
Public Declare Function C848_qDFF Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_SCA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal cAxisLeftRight As Byte, _
                                ByVal cAxisUpDown As Byte _
                                ) As Long
                                
Public Declare Function C848_qSCA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal pcAxisLeftRight As String, _
                                ByVal pcAxisUpDown As String _
                                ) As Long

Public Declare Function C848_SMO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pnValarray As Long _
                                ) As Long
                                
Public Declare Function C848_qSMO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pnValarray As Long _
                                ) As Long
                                
Public Declare Function C848_SVO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_qSVO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long

Public Declare Function C848_qSTA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pnValarray_ As Long _
                                ) As Long
                                
Public Declare Function C848_qTIM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pnTime As Long _
                                ) As Long
                                
Public Declare Function C848_qSSN Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pNr As Long _
                                ) As Long

Public Declare Function C848_SystemInfoDlg Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long

Public Declare Function C848_IsReferenceOK Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_SPA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef iCmdarray As Long, _
                                ByRef dValarray As Double _
                                ) As Long
                                
Public Declare Function C848_qSPA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef iCmdarray As Long, _
                                ByRef dValarray As Double _
                                ) As Long
                                
Public Declare Function C848_ITD Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_RST Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_SAV Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long

Public Declare Function C848_STE Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal cAxis As Byte, _
                                ByVal dPos As Double _
                                ) As Long
                                
Public Declare Function C848_qSTE Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal cAxis As Byte, _
                                ByVal iOffset As Long, _
                                ByVal nrValues As Long, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_StageConfigDlg Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal cAxis As Byte _
                                ) As Long
                                
' config stages
Public Declare Function C848_SAI Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szOldAxes As String, _
                                ByVal szNewAxes As String _
                                ) As Long
                                
Public Declare Function C848_qSAI Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByVal maxlen As Long) _
                                As Long
                                
Public Declare Function C848_qTVI Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                
Public Declare Function C848_qCST Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByVal names As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                
Public Declare Function C848_qVST Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long


'//////////////
'// general. //
'//////////////
Public Declare Function C848_qVER Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long

Public Declare Function C848_qIDN Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long

Public Declare Function C848_qERR Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pnError As Long _
                                ) As Long

Public Declare Function C848_qHLP Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long

Public Declare Function C848_INI Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long

Public Declare Function C848_MOV Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_qMOV Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_MVR Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_VMO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double, _
                                ByRef pbMovePossible As Long _
                                ) As Long

Public Declare Function C848_qPOS Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long
                                
Public Declare Function C848_POS Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_qONT Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long

Public Declare Function C848_HLT Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long

Public Declare Function C848_STP Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Function C848_SystemAbort Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long

Public Declare Function C848_VEL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_qVEL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pdValarray As Double _
                                ) As Long

Public Declare Function C848_HasPosChanged Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long

Public Declare Function C848_IsMoving Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long

Public Declare Function C848_WAI Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long

Public Declare Function C848_WAA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal iWaitTmie As Long _
                                ) As Long

Public Declare Function C848_IsWaitingForAllAxes Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pbIsWaitingForAllAxes As Long _
                                ) As Long

Public Declare Function C848_GetWaaResult Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pbWaaResult As Long _
                                ) As Long




'//////////////
'// display. //
'//////////////
Public Declare Function C848_DSP Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_qDSP Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                
Public Declare Function C848_HID Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_qHID Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                
Public Declare Function C848_CLS Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Function C848_MSG Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szMessage As String _
                                ) As Long



'/////////////
'// limits. //
'/////////////
Public Declare Function C848_MNL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_MPL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_REF Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_qREF Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_GetRefResult Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pnResult As Long _
                                ) As Long
                                
Public Declare Function C848_IsReferencing Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbIsReferencing As Long _
                                ) As Long
                                
Public Declare Function C848_NLM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_qNLM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_PLM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_qPLM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_SSL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_qSSL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_LimitsDialog Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal cAxis As Byte _
                                ) As Long
                                
Public Declare Function C848_qTMN Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_qTMX Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_DFH Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long
                                
Public Declare Function C848_qDFH Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Double _
                                ) As Long
                                
Public Declare Function C848_GOH Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String _
                                ) As Long

Public Declare Function C848_qLIM Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_RON Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_qRON Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long



'/////////////////////
'// "old" commands. //
'/////////////////////
Public Declare Function C848_BRA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pbValarray As Long _
                                ) As Long
                                
Public Declare Function C848_qBRA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                

'/////////////////////
'// macro commands. //
'/////////////////////
Public Declare Function C848_IsRecordingMacro Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pbInMacroMode As Long _
                                ) As Long
                                
Public Declare Function C848_MAC_DEL Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szName As String _
                                ) As Long
                                
Public Declare Function C848_MAC_START Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szName As String _
                                ) As Long
                                
Public Declare Function C848_qMAC Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szName As String, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long
                                
Public Declare Function C848_MAC_BEG Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szName As String _
                                ) As Long
                                
Public Declare Function C848_MAC_END Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Function C848_SaveMacroToFile Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szFileName As String, _
                                ByVal szMacroName As String _
                                ) As Long
                                
Public Declare Function C848_LoadMacroFromFile Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szFileName As String, _
                                ByVal szMacroName As String _
                                ) As Long
                                
Public Declare Function C848_MacroEditor Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long
                                
Public Declare Function C848_IsRunningMacro Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef fIsMacroRunning As Long _
                                ) As Long


'///////////////////////////
'// Digital IO functions. //
'///////////////////////////
Public Declare Function C848_qTIO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pINr As Long, _
                                ByRef pONr As Long _
                                ) As Long

Public Declare Function C848_GetInputChannelNames Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByVal maxlen As Long _
                                ) As Long

Public Declare Function C848_GetOutputChannelNames Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szBuffer As String, _
                                ByRef maxlen As Long _
                                ) As Long

Public Declare Function C848_DIO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szChannels As String, _
                                ByRef bValarray As Long _
                                ) As Long

Public Declare Function C848_qDIO Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szChannels As String, _
                                ByRef bValarray As Long _
                                ) As Long


'//////////////////////////
'// GCS-String-Commands. //
'//////////////////////////
Public Declare Function C848_GcsCommandset Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szCommand As String _
                                ) As Long

Public Declare Function C848_GcsGetAnswer Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAnswer As String, _
                                ByVal bufsize As Long _
                                ) As Long

Public Declare Function C848_GcsGetAnswerSize Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef iAnswerSize As Long _
                                ) As Long




'///////////////////////
'// Joystik commands. //
'///////////////////////
Public Declare Function C848_qTNJ Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pNr As Long _
                                ) As Long

Public Declare Function C848_JEN Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal bOnOff As Long _
                                ) As Long

Public Declare Function C848_JEN_CALIB Lib "C848_DLL.dll" ( _
                                ByVal ID As Long _
                                ) As Long

Public Declare Function C848_qJEN Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByRef pbOnOff As Long _
                                ) As Long

Public Declare Function C848_SJA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByRef pJoystikAxisNr As Long _
                                ) As Long

Public Declare Function C848_qSJA Lib "C848_DLL.dll" ( _
                                ByVal ID As Long, _
                                ByVal szAxes As String, _
                                ByVal maxlen As Long _
                                ) As Long
