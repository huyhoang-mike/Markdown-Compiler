from DeepImageSearch import Load_Data, Search_Setup
def findSimilar():
    # Load images from a folder
    image_list = Load_Data().from_folder(['images'])
    # Set up the search engine, You can load 'vit_base_patch16_224_in21k', 'resnet50' etc more then 500+ models 
    st = Search_Setup(image_list=image_list, model_name='vgg19', pretrained=True, image_count=100)
    # Index the images
    st.run_index()
    # Get metadata
    metadata = st.get_image_metadata_file()
    # Plot similar images
    st.plot_similar_images(image_path='images/Experimental Cocktail Club/Image_4.jpg', number_of_images=1)
    return None