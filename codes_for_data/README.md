# Codes for data
### voc_label.py
- Use to change the Pascal label to YOLO label
	- **if you already label the data in with YOLO label format, you don't need this.**

### replace_path.py
- Use to change the path in name.list
	- **if you can get the path with correct format, you don't need this.**

## Before you run the voc_label.py
- Run the following codes in terminal to get name.list
	```bash
	find `pwd`/img -name \*.jpg > name.list
	find `pwd`/img -name \*.JPG >> name.list
	```