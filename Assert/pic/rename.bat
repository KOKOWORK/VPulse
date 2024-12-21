@echo off  
setlocal enabledelayedexpansion  
  
set count=0  
  
for %%f in (*) do (  
    set "ext=%%~xf"  
    if /i not "!ext!"==".bat" if /i not "!ext!"==".cmd" (  
        set "filename=%%~nf"  
        set "newname=!count!!ext!"  
          
        :checkName  
        if exist "!newname!" (  
            set /a count+=1  
            set "newname=!count!!ext!"  
            goto :checkName  
        )  
          
        ren "%%f" "!newname!"  
        set /a count+=1  
    )  
)  
  
echo Renaming completed.  
pause