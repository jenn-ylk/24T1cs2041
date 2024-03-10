#! /bin/dash

for image_file in ~/friends/*; do
    echo $image_file
    ln -s "$image_file" .
    # Or - take the env variable for HOME 
    # (if using ls command - not recommented)
    # ln -s "$HOME/friends/$image_file" .
done