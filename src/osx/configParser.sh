IFS=$'\n'
CONF=`grep -v \# conf/client/osx.cfg`

confNum=0
echo "$CONF"
echo "Entering loop"
for line in `echo "$CONF"`
do 
    if [[ $line == HEADER\=* ]]; then
        IFS='=' read -r -a array <<< "$line"
        IFS=$'\n'
        HEADER=${array[1]}
    else
        confDb[confNum]=$line
        let "confNum+=1"
    fi 
done

echo $confDB