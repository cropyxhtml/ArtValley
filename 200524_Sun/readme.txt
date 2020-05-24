import win32gui,win32ui

uiDC  = win32ui.CreateDCFromHandle(win32gui.GetWindowDC(hwnd))
uicompatibleDC = uiDC.CreateCompatibleDC()
uibitmap = win32ui.CreateBitmap()
uibitmap.CreateCompatibleBitmap(mfcDC, w, h)
uicompatibleDC.SelectObject(saveBitMap)



※오류해결
'PhotoImage' object has no attribute 'PhotoImage photo' 원인이 파일이름에 . 이 들어가 있어서
Thread오류가 지속적으로 발생함