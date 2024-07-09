# Organizer for SURF Data.

## How to use the code?

### For single folder
```
python file_org_SURF/run_organizer.py source_path target_path
```
then the the files under source_path will be segmented hourly into target_path.

### For multiple folders

Put the folders' names into config.txt
```
python file_org_SURF/run_organizer_many.py config.txt
```
The output of the command line would be like:  
(which depends on the config.txt)
```
May_2022/Well_-SURF()__on_04052022_124314_UTC(+0000): Done
May_2022/Well_-SURF()__on_04052022_123303_UTC(+0000): Done
May_2022/Well_-SURF()__on_05052022_143058_UTC(+0000): Done
May_2022/Well_-SURF()__on_03052022_205347_UTC(+0000): Done
'
'
'
```
