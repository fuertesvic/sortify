# sortify
Desktop App used to sort, classify and manage images based on user-inputted tags  

The user can define tags and add then to img metadata and then perform actions such as searching all images with a specific tag.  

 --- WORK IN PROGRESS ---   

 some tasks for the future me:   
 
- [x] Code the most basic metadata input/read and logic functionality  
- [ ] Allow the user to remove a single tag within an image  
- [ ] Allow to the user to work within multiple folders at once & creating new folders based on tags  
- [ ] Improve performance within a large dataset  
- [ ] Improve visuals  
- [ ] Add Image recogtnition to automatically add tags to images.  
 

Steps to reproduce with example dataset (Pokemon images in https://www.kaggle.com/datasets/kvpratama/pokemon-images-dataset/data):  
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
