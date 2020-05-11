For /f "tokens=1-5" %%1 in (tellog.txt) do (
	if %%3 equ Denied echo Denied> Tellog.txt
	if %%3 equ Granted echo Granted> Tellog.txt
)