path="dataset/pokemon/"
for img in `ls -v $path | tail -n +100`
do
    rm $path/$file/$img
done
