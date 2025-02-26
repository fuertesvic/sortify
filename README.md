# sortify
Desktop App used to sort and classify images -- based on tags stored in metadata  

Currently works with PNG images only.  
User can define tags and add then to img metadata and then find images with a specific tag.  

-- Work In Progress --  

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
