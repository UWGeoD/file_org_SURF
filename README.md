# Organizer for SURF Data.

## How to use the code?

### Download the repo
```
clone git@github.com:UWGeoD/file_org_SURF.git
```

The file structure would be like
├── config.txt (config for multiple folders)
├── file_org_SURF (Organizer Scripts)
├── lost+found
├── May_2022 (The folder we want to process)
├── nohup.out 
└── Organized_SURF (Organized data)

### Processing single folder
```
python file_org_SURF/run_organizer.py source_path target_path
```
then the the files under source_path will be segmented hourly into target_path.

For example,
```
python file_org_SURF/run_organizer.py May_2022/Well_-SURF\(\)__on_03052022_210040_UTC\(+0000\)/ Organized_SURF/
```

### Processing multiple folders

You can manully put the folders' names into config.txt. 
Or run the following command to write the all the names with the format "Well_-SURF()__on_03052022_203555_UTC(+0000)"
```
python file_org_SURF/create_config.py target_folder
```
For example,
```
python file_org_SURF/create_config.py May_2022
```

To process multiple folders, please run
```
nohup python file_org_SURF/run_organizer_many.py config.txt source_path target_path &
```
For example,
```
nohup python file_org_SURF/run_organizer_many.py config.txt May_2022 Organized_SURF &
```

The output in nohup.out would be like:  
(which depends on the config.txt)
```
Processed files from May_2022/Well_-SURF()__on_04052022_124314_UTC(+0000) to Organized_SURF
Processed files from May_2022/Well_-SURF()__on_04052022_123303_UTC(+0000) to Organized_SURF
Processed files from May_2022/Well_-SURF()__on_05052022_143058_UTC(+0000) to Organized_SURF
Processed files from May_2022/Well_-SURF()__on_03052022_205347_UTC(+0000) to Organized_SURF
Processed files from May_2022/Well_-SURF()__on_19052022_151612_UTC(+0000) to Organized_SURF
'
'
'
```
#### Log tracker
Look at the processed log 
```
tail Organized_SURF/Log/success.log
```
or 
```
tail Organized_SURF/Log/error.log
```

