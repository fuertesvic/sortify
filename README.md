# sortify
 
 --- WORK IN PROGRESS --- 

Desktop app used to manage, sort and classify locally stored images.
It works with PNG images only currently, and it reads Metadata in PngInfo Plugin from Pillow
It has a GUI which allows the user to:  

	- Navigate a folder and view metadata tags  
	- Select one/multiple file(s) in the folder and add a tag.  
	- Select all files in the folder to perform a further action  
	- Remove a specific tag from a single image  
	- Remove all tags from the selected image(s)  
	- Search in a specific folder for image(s) containing a specific tag.  


The user can define tags and add then to img metadata and then perform actions such as searching all images with a specific tag.  

  

# Development Log
 some tasks for the future me:   
 
- [x] Code a basic metadata input/read, logic functionality and GUI implementation (done - 27th feb '25)
- [x] Setup executables with PyInstaller so the user doesn't need to have Python installed.
- [x] Allow the user to remove a single tag within an image (done - 6th march)  
- [ ] Implement searching for images with multiple matching tags
- [ ] Allow to the user to work within multiple folders at once & creating new folders based on tags  
- [ ] Improve performance within a large dataset  
- [ ] Improve visual GUI -- Stop using TkInter and migrate to PyQt
- [ ] Add keybindings   
- [ ] Add Image recogtnition to automatically add tags to images.  
 



# Steps to reproduce with example dataset  

Pokemon images in [this Kaggle dataset](https://www.kaggle.com/datasets/kvpratama/pokemon-images-dataset/data)  
1) Install requirements (Kaggle, Pillow):  
	pip install -r requirements.txt

2) Download and unzip dataset:  
	kaggle datasets download -d kvpratama/pokemon-images-dataset  
	unzip pokemon-images-dataset.zip -d dataset/  
    rm pokemon-images-dataset.zip  
	rm -r dataset/pokemon_jpg  
	mv dataset/pokemon/pokemon/* dataset/pokemon   
	rm -r dataset/pokemon/pokemon   

3) Sample dataset-- Get the first 100 images and discard the rest.  
    ./sample_dataset.sh
